from antlr4 import *
from MiLenguajeListener import MiLenguajeListener
from MiLenguajeParser import MiLenguajeParser
from symbol_table import SymbolTable, SemanticError, FunctionSymbol

class SemanticAnalyzer(MiLenguajeListener):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.current_function_type = None  # Para verificar el tipo de retorno
        self.has_return = False  # Para verificar si una función tiene retorno

    def get_errors(self):
        return self.errors

    def add_error(self, ctx, message):
        line = ctx.start.line
        column = ctx.start.column
        self.errors.append(SemanticError(message, line, column))

    def get_type_compatibility(self, type1, type2):
        """Verifica la compatibilidad de tipos para operaciones."""
        # Si ambos tipos son el mismo, son compatibles
        if type1 == type2:
            return type1
        
        # Reglas de conversión
        numeric_types = ["ent", "flt", "lg"]
        
        # Si ambos son tipos numéricos, el resultado es el tipo más "amplio"
        if type1 in numeric_types and type2 in numeric_types:
            if "lg" in [type1, type2]:
                return "lg"
            elif "flt" in [type1, type2]:
                return "flt"
            else:
                return "ent"
        
        # String con cualquier otro tipo es error
        if "str" in [type1, type2] and type1 != type2:
            return None
        
        return None  # Tipos incompatibles

    def get_expression_type(self, ctx):
        """Determina el tipo de una expresión de forma genérica."""
        # Si es una referencia a una variable
        if isinstance(ctx, MiLenguajeParser.Expr_primContext) and ctx.ID():
            symbol = self.symbol_table.lookup(ctx.ID().getText())
            if symbol is None:
                self.add_error(ctx, f"Variable '{ctx.ID().getText()}' no declarada")
                return None
            return symbol.type
            
        # Si es un número
        elif isinstance(ctx, MiLenguajeParser.Expr_primContext) and ctx.NUMERO_VALORES():
            num_text = ctx.NUMERO_VALORES().getText()
            if 'l' in num_text:
                return "lg"
            elif '.' in num_text:
                return "flt"
            else:
                return "ent"
                
        # Si es una cadena
        elif isinstance(ctx, MiLenguajeParser.Expr_primContext) and ctx.STRING():
            return "str"
            
        # Si es una llamada a función
        elif isinstance(ctx, MiLenguajeParser.Expr_primContext) and ctx.llamadaFuncion():
            function_name = ctx.llamadaFuncion().ID().getText()
            function = self.symbol_table.lookup(function_name)
            if function is None:
                self.add_error(ctx, f"Función '{function_name}' no declarada")
                return None
            return function.type
            
        # Si es una expresión entre paréntesis
        elif isinstance(ctx, MiLenguajeParser.Expr_primContext) and ctx.expresion():
            return self.get_expression_type(ctx.expresion())
            
        # Si es una expresión de multiplicación/división
        elif isinstance(ctx, MiLenguajeParser.Expr_multContext):
            # Si solo hay un término primario
            if len(ctx.expr_prim()) == 1:
                return self.get_expression_type(ctx.expr_prim(0))
            
            # Si hay operadores
            expr_types = []
            for expr_prim in ctx.expr_prim():
                expr_type = self.get_expression_type(expr_prim)
                if expr_type is None:
                    return None
                expr_types.append(expr_type)
            
            # Verificar compatibilidad
            result_type = expr_types[0]
            for i in range(1, len(expr_types)):
                result_type = self.get_type_compatibility(result_type, expr_types[i])
                if result_type is None:
                    self.add_error(ctx, f"Operación aritmética entre tipos incompatibles")
                    return None
                
                # Verificar división por cero
                if i*2-1 < len(ctx.children) and ctx.children[i*2-1].getText() == '/':
                    if self.is_zero_literal(ctx.expr_prim(i)):
                        self.add_error(ctx, "División por cero")
            
            return result_type
            
        # Si es una expresión de suma/resta
        elif isinstance(ctx, MiLenguajeParser.Expr_sumaContext):
            # Si solo hay un término multiplicativo
            if len(ctx.expr_mult()) == 1:
                return self.get_expression_type(ctx.expr_mult(0))
            
            # Si hay operadores
            expr_types = []
            for expr_mult in ctx.expr_mult():
                expr_type = self.get_expression_type(expr_mult)
                if expr_type is None:
                    return None
                expr_types.append(expr_type)
            
            # Verificar compatibilidad
            result_type = expr_types[0]
            for i in range(1, len(expr_types)):
                result_type = self.get_type_compatibility(result_type, expr_types[i])
                if result_type is None:
                    self.add_error(ctx, f"Operación aritmética entre tipos incompatibles")
                    return None
            
            return result_type
            
        # Si es una expresión general
        elif isinstance(ctx, MiLenguajeParser.ExpresionContext):
            return self.get_expression_type(ctx.expr_suma())
            
        # Para otros tipos de nodos
        return None

    def is_zero_literal(self, ctx):
        """Determina si una expresión es literalmente cero."""
        if hasattr(ctx, 'NUMERO_VALORES') and ctx.NUMERO_VALORES():
            return ctx.NUMERO_VALORES().getText() == '0'
        return False

    # Visitar declaraciones
    def enterDeclaracion(self, ctx):
        name = ctx.ID().getText()
        type_name = ""
        
        # Obtener el tipo
        if ctx.tipo().kwEnt():
            type_name = "ent"
        elif ctx.tipo().kwFlt():
            type_name = "flt"
        elif ctx.tipo().kwLg():
            type_name = "lg"
        elif ctx.tipo().kwStr():
            type_name = "str"
        
        # Verificar si es constante
        is_constant = ctx.kwUnmutable() is not None
        
        # Verificar si ya existe en el ámbito actual
        if name in self.symbol_table.get_current_scope_symbols():
            self.add_error(ctx, f"Variable '{name}' ya declarada en este ámbito")
            return
        
        # Agregar a la tabla de símbolos
        value = None
        if ctx.expresion():
            # Si hay una inicialización, verificar compatibilidad de tipos
            expr_type = self.get_expression_type(ctx.expresion())
            if expr_type is None:
                self.add_error(ctx, f"Error en la expresión de inicialización para '{name}'")
                return
            
            # Verificar compatibilidad de tipos
            compatible_type = self.get_type_compatibility(type_name, expr_type)
            if compatible_type is None:
                self.add_error(ctx, f"Tipo incompatible: no se puede asignar '{expr_type}' a '{type_name}'")
                return
            
            # En este caso no calculamos el valor real, sólo indicamos que tiene un valor
            value = "initialized"
        
        # Declarar la variable
        self.symbol_table.declare(name, type_name, is_constant, value)

    # Visitar asignaciones
    def enterAsignacion(self, ctx):
        name = ctx.ID().getText()
        symbol = self.symbol_table.lookup(name)
        
        # Verificar si la variable existe
        if symbol is None:
            self.add_error(ctx, f"Variable '{name}' no declarada")
            return
        
        # Verificar si es constante
        if symbol.is_constant:
            self.add_error(ctx, f"No se puede modificar la constante '{name}'")
            return
        
        # Verificar compatibilidad de tipos
        expr_type = self.get_expression_type(ctx.expresion())
        if expr_type is None:
            self.add_error(ctx, f"Error en la expresión para asignar a '{name}'")
            return
        
        compatible_type = self.get_type_compatibility(symbol.type, expr_type)
        if compatible_type is None:
            self.add_error(ctx, f"Tipo incompatible: no se puede asignar '{expr_type}' a '{symbol.type}'")
            return
        
        # Actualizar el valor (aquí solo marcamos que tiene un valor)
        self.symbol_table.update(name, "modified")

    # Entrar a un nuevo ámbito (función, if, ciclos)
    def enterFuncionConRetorno(self, ctx):
        name = ctx.ID().getText()
        
        # Obtener el tipo de retorno
        return_type = ""
        if ctx.tipo().kwEnt():
            return_type = "ent"
        elif ctx.tipo().kwFlt():
            return_type = "flt"
        elif ctx.tipo().kwLg():
            return_type = "lg"
        elif ctx.tipo().kwStr():
            return_type = "str"
        
        # Verificar si ya existe
        if self.symbol_table.lookup(name) is not None:
            self.add_error(ctx, f"Función '{name}' ya declarada")
            return
        
        # Declarar la función en el ámbito actual
        self.symbol_table.declare_function(name, return_type)
        
        # Obtener el símbolo de la función que acabamos de crear
        function_symbol = self.symbol_table.lookup(name)
        
        # Crear un nuevo ámbito para los parámetros y variables locales
        self.symbol_table.enter_scope()
        self.current_function_type = return_type
        self.has_return = False
        
        # Procesar parámetros si los hay
        if ctx.parametros():
            param_ctx = ctx.parametros()
            param_types = param_ctx.tipo()
            param_names = param_ctx.ID()
            
            for i in range(len(param_types)):
                param_type = ""
                if param_types[i].kwEnt():
                    param_type = "ent"
                elif param_types[i].kwFlt():
                    param_type = "flt"
                elif param_types[i].kwLg():
                    param_type = "lg"
                elif param_types[i].kwStr():
                    param_type = "str"
                
                param_name = param_names[i].getText()
                
                # Verificar si ya existe en el ámbito actual
                if param_name in self.symbol_table.get_current_scope_symbols():
                    self.add_error(param_ctx, f"Parámetro '{param_name}' duplicado")
                    continue
                
                # Añadir información de parámetro a la función
                function_symbol.add_parameter(param_name, param_type)
                
                # Declarar el parámetro en el ámbito de la función
                self.symbol_table.declare(param_name, param_type, False, "parameter")

    def exitFuncionConRetorno(self, ctx):
        # Verificar si la función tiene un retorno
        if not self.has_return:
            self.add_error(ctx, f"La función '{ctx.ID().getText()}' debe tener una sentencia de retorno")
        
        # Salir del ámbito
        self.symbol_table.exit_scope()
        self.current_function_type = None
        self.has_return = False

    def enterFuncionSinRetorno(self, ctx):
        name = ctx.ID().getText()
        
        # Verificar si ya existe
        if self.symbol_table.lookup(name) is not None:
            self.add_error(ctx, f"Función '{name}' ya declarada")
            return
        
        # Declarar la función en el ámbito actual (tipo void)
        self.symbol_table.declare_function(name, "void")
        
        # Obtener el símbolo de la función que acabamos de crear
        function_symbol = self.symbol_table.lookup(name)
        
        # Crear un nuevo ámbito para los parámetros y variables locales
        self.symbol_table.enter_scope()
        
        # Procesar parámetros si los hay
        if ctx.parametros():
            param_ctx = ctx.parametros()
            param_types = param_ctx.tipo()
            param_names = param_ctx.ID()
            
            for i in range(len(param_types)):
                param_type = ""
                if param_types[i].kwEnt():
                    param_type = "ent"
                elif param_types[i].kwFlt():
                    param_type = "flt"
                elif param_types[i].kwLg():
                    param_type = "lg"
                elif param_types[i].kwStr():
                    param_type = "str"
                
                param_name = param_names[i].getText()
                
                # Verificar si ya existe en el ámbito actual
                if param_name in self.symbol_table.get_current_scope_symbols():
                    self.add_error(param_ctx, f"Parámetro '{param_name}' duplicado")
                    continue
                
                # Añadir información de parámetro a la función
                function_symbol.add_parameter(param_name, param_type)
                
                # Declarar el parámetro en el ámbito de la función
                self.symbol_table.declare(param_name, param_type, False, "parameter")

    def exitFuncionSinRetorno(self, ctx):
        # Salir del ámbito
        self.symbol_table.exit_scope()

    # Entrar a un ciclo o un if
    def enterEstructuraIf(self, ctx):
        self.symbol_table.enter_scope()

    def exitEstructuraIf(self, ctx):
        self.symbol_table.exit_scope()

    def enterCicloFor(self, ctx):
        self.symbol_table.enter_scope()

    def exitCicloFor(self, ctx):
        self.symbol_table.exit_scope()

    def enterCicloWhile(self, ctx):
        self.symbol_table.enter_scope()

    def exitCicloWhile(self, ctx):
        self.symbol_table.exit_scope()

    # Verificar expresión lógica
    # Verificar expresión lógica
    def enterExpresionLogica(self, ctx):
        left_expr = ctx.expresion(0)
        right_expr = ctx.expresion(1)
        
        left_type = self.get_expression_type(left_expr)
        right_type = self.get_expression_type(right_expr)
        
        if left_type is None or right_type is None:
            return  # Ya se reportó el error
        
        # Verificar compatibilidad
        compatible_type = self.get_type_compatibility(left_type, right_type)
        if compatible_type is None:
            self.add_error(ctx, f"Comparación entre tipos incompatibles: '{left_type}' y '{right_type}'")

    # Verificar retorno
    def enterRetornoSentencia(self, ctx):
        if self.current_function_type is None:
            self.add_error(ctx, f"Sentencia de retorno fuera de función")
            return
        
        expr_type = self.get_expression_type(ctx.expresion())
        if expr_type is None:
            self.add_error(ctx, "Error en la expresión de retorno")
            return
        
        compatible_type = self.get_type_compatibility(self.current_function_type, expr_type)
        if compatible_type is None:
            self.add_error(ctx, f"Tipo de retorno incompatible: '{expr_type}' no se puede convertir a '{self.current_function_type}'")
            return
        
        self.has_return = True

    # Verificar llamada a función
    def enterLlamadaFuncion(self, ctx):
        function_name = ctx.ID().getText()
        function = self.symbol_table.lookup(function_name)
        
        # Verificar si la función existe
        if function is None:
            self.add_error(ctx, f"Función '{function_name}' no declarada")
            return
        
        # Verificar si el símbolo es realmente una función
        if not isinstance(function, FunctionSymbol):
            self.add_error(ctx, f"'{function_name}' no es una función")
            return
        
        # Verificar número de argumentos
        arguments = ctx.expresion()
        if len(arguments) != len(function.param_types):
            self.add_error(ctx, f"Número incorrecto de argumentos: esperados {len(function.param_types)}, encontrados {len(arguments)}")
            return
        
        # Verificar tipos de argumentos
        for i, arg in enumerate(arguments):
            arg_type = self.get_expression_type(arg)
            if arg_type is None:
                # Ya se reportó un error en la expresión
                continue
                
            param_type = function.param_types[i]
            compatible_type = self.get_type_compatibility(param_type, arg_type)
            
            if compatible_type is None:
                param_name = function.param_names[i] if i < len(function.param_names) else f"#{i+1}"
                self.add_error(ctx, f"Tipo incompatible en argumento {param_name}: esperado '{param_type}', encontrado '{arg_type}'")