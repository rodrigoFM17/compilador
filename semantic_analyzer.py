from antlr4 import *
from MiLenguajeListener import MiLenguajeListener
from MiLenguajeParser import MiLenguajeParser
from symbol_table import SymbolTable, SemanticError


class SemanticAnalyzer(MiLenguajeListener):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.current_function_type = None  # Para verificar el tipo de retorno
        self.has_return = False  # Para verificar si una función tiene retorno

    def get_param_type(self, tipo_ctx):
        """Obtiene el tipo de un parámetro a partir de su contexto"""
        if tipo_ctx.kwEnt():
            return "ent"
        elif tipo_ctx.kwFlt():
            return "flt"
        elif tipo_ctx.kwLg():
            return "lg"
        elif tipo_ctx.kwStr():
            return "str"
        return None

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

    def evaluate_expression(self, ctx):
        """Evalúa una expresión y retorna su valor si es posible."""
        # Si solo hay un término sin operadores
        if len(ctx.termino()) == 1 and not ctx.operadoresAritmeticos():
            return self.evaluate_term(ctx.termino(0))
            
        # Si hay operadores aritméticos
        if ctx.operadoresAritmeticos():
            # Evaluar el primer término
            result = self.evaluate_term(ctx.termino(0))
            
            # Si no se pudo evaluar el primer término, no podemos seguir
            if result is None:
                return None
            
            # Aplicar operaciones
            for i, op in enumerate(ctx.operadoresAritmeticos()):
                term = ctx.termino(i + 1)
                term_value = self.evaluate_term(term)
                
                # Si algún término no se puede evaluar, no podemos seguir
                if term_value is None:
                    return None
                
                # Realizar la operación con prioridad
                op_text = op.getText()
                if op_text == '*':
                    result *= term_value
                elif op_text == '/':
                    # Evitar división por cero
                    if term_value == 0:
                        self.add_error(ctx, "División por cero")
                        return None
                    result /= term_value
                elif op_text == '%':
                    # Evitar módulo por cero
                    if term_value == 0:
                        self.add_error(ctx, "Módulo por cero")
                        return None
                    result %= term_value
                elif op_text == '+':
                    result += term_value
                elif op_text == '-':
                    result -= term_value
            
            return result
        
        return None

    
    def evaluate_additive_expression(self, ctx):
        """Evalúa una expresión aditiva."""
        # Evaluar primera expresión multiplicativa
        result = self.evaluate_multiplicative_expression(ctx.expresionMultiplicativa(0))
        if result is None:
            return None
        
        # Aplicar operadores aditivos
        for i, op in enumerate(ctx.operadoresAditivos()):
            term_value = self.evaluate_multiplicative_expression(ctx.expresionMultiplicativa(i + 1))
            if term_value is None:
                return None
            
            if op.getText() == '+':
                result += term_value
            elif op.getText() == '-':
                result -= term_value
        
        return result
    
    def evaluate_multiplicative_expression(self, ctx):
        """Evalúa una expresión multiplicativa."""
        # Evaluar primer término
        result = self.evaluate_term(ctx.termino(0))
        if result is None:
            return None
        
        # Aplicar operadores multiplicativos
        for i, op in enumerate(ctx.operadoresMultiplicativos()):
            term_value = self.evaluate_term(ctx.termino(i + 1))
            if term_value is None:
                return None
            
            if op.getText() == '*':
                result *= term_value
            elif op.getText() == '/':
                if term_value == 0:
                    self.add_error(ctx, "División por cero")
                    return None
                result /= term_value
            elif op.getText() == '%':
                if term_value == 0:
                    self.add_error(ctx, "Módulo por cero")
                    return None
                result %= term_value
        
        return result
    
    def evaluate_expression_aditiva(self, ctx):
        """Evalúa una expresión aditiva (suma, resta)."""
        # Evaluar primera expresión multiplicativa
        result = self.evaluate_expression_multiplicativa(ctx.expresionMultiplicativa(0))
        if result is None:
            return None
        
        # Aplicar operadores aditivos (+ o -)
        for i, op in enumerate(ctx.operadoresAditivos()):
            term_value = self.evaluate_expression_multiplicativa(ctx.expresionMultiplicativa(i + 1))
            if term_value is None:
                return None
            
            if op.getText() == '+':
                result += term_value
            elif op.getText() == '-':
                result -= term_value
        
        return result

    def evaluate_expression_multiplicativa(self, ctx):
        """Evalúa una expresión multiplicativa (multiplicación, división, módulo)."""
        # Evaluar primer término
        result = self.evaluate_term(ctx.termino(0))
        if result is None:
            return None
        
        # Aplicar operadores multiplicativos (*, /, %)
        for i, op in enumerate(ctx.operadoresMultiplicativos()):
            term_value = self.evaluate_term(ctx.termino(i + 1))
            if term_value is None:
                return None
            
            if op.getText() == '*':
                result *= term_value
            elif op.getText() == '/':
                if term_value == 0:
                    self.add_error(ctx, "División por cero")
                    return None
                result /= term_value
            elif op.getText() == '%':
                if term_value == 0:
                    self.add_error(ctx, "Módulo por cero")
                    return None
                result %= term_value
        
        return result

    def evaluate_term(self, ctx):
        """Evalúa un término y retorna su valor si es posible."""
        if ctx.ID():
            symbol = self.symbol_table.lookup(ctx.ID().getText())
            if symbol is None:
                self.add_error(ctx, f"Variable '{ctx.ID().getText()}' no declarada")
                return None
            return symbol.value
        elif ctx.NUMERO_VALORES():
            num_text = ctx.NUMERO_VALORES().getText()
            if 'l' in num_text:
                return int(num_text.replace('l', ''))
            elif '.' in num_text:
                return float(num_text)
            else:
                return int(num_text)
        elif ctx.STRING():
            # Eliminar las comillas
            return ctx.STRING().getText()[1:-1]
        elif ctx.llamadaFuncion():
            # Las llamadas a funciones no se evalúan en tiempo de compilación
            return None
        elif ctx.expresion():
            # Para expresiones entre paréntesis
            return self.evaluate_expression(ctx.expresion())
            
        return None
    
    def get_additive_expression_type(self, ctx):
        """Determina el tipo de una expresión aditiva."""
        # Obtener tipo de la primera expresión multiplicativa
        result_type = self.get_multiplicative_expression_type(ctx.expresionMultiplicativa(0))
        if result_type is None:
            return None
        
        # Verificar compatibilidad con otras expresiones multiplicativas
        for i in range(1, len(ctx.expresionMultiplicativa())):
            mult_type = self.get_multiplicative_expression_type(ctx.expresionMultiplicativa(i))
            if mult_type is None:
                return None
            
            result_type = self.get_type_compatibility(result_type, mult_type)
            if result_type is None:
                self.add_error(ctx, f"Operación aritmética entre tipos incompatibles")
                return None
        
        return result_type
    
    def get_multiplicative_expression_type(self, ctx):
        """Determina el tipo de una expresión multiplicativa."""
        # Obtener tipo del primer término
        result_type = self.get_term_type(ctx.termino(0))
        if result_type is None:
            return None
        
        # Verificar compatibilidad con otros términos
        for i in range(1, len(ctx.termino())):
            term_type = self.get_term_type(ctx.termino(i))
            if term_type is None:
                return None
            
            result_type = self.get_type_compatibility(result_type, term_type)
            if result_type is None:
                self.add_error(ctx, f"Operación aritmética entre tipos incompatibles")
                return None
        
        return result_type

    def get_expression_type(self, ctx):
        """Determina el tipo de una expresión."""
        # Si solo hay un término sin operadores
        if len(ctx.termino()) == 1 and not ctx.operadoresAritmeticos():
            return self.get_term_type(ctx.termino(0))
            
        # Si hay operadores aritméticos, evaluamos la compatibilidad
        if ctx.operadoresAritmeticos():
            term_types = []
            for term in ctx.termino():
                term_type = self.get_term_type(term)
                if term_type is None:
                    return None  # Propagar error
                term_types.append(term_type)
            
            # Verificar compatibilidad entre todos los términos
            result_type = term_types[0]
            for i in range(1, len(term_types)):
                result_type = self.get_type_compatibility(result_type, term_types[i])
                if result_type is None:
                    self.add_error(ctx, f"Operación aritmética entre tipos incompatibles")
                    return None
            
            return result_type
            
        return None        

    def get_term_type(self, ctx):
        """Determina el tipo de un término."""
        if ctx.ID():
            symbol = self.symbol_table.lookup(ctx.ID().getText())
            if symbol is None:
                self.add_error(ctx, f"Variable '{ctx.ID().getText()}' no declarada")
                return None
            return symbol.type
        elif ctx.NUMERO_VALORES():
            num_text = ctx.NUMERO_VALORES().getText()
            if 'l' in num_text:
                return "lg"
            elif '.' in num_text:
                return "flt"
            else:
                return "ent"
        elif ctx.STRING():
            return "str"
        elif ctx.llamadaFuncion():
            function_name = ctx.llamadaFuncion().ID().getText()
            # Buscar la función en la tabla de símbolos
            function = self.symbol_table.lookup(function_name)
            if function is None:
                self.add_error(ctx, f"Función '{function_name}' no declarada")
                return None
            return function.type
        elif ctx.expresion():
            # Para expresiones entre paréntesis
            return self.get_expression_type(ctx.expresion())
            
        return None

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
            
            # Evaluar la expresión si es posible
            value = self.evaluate_expression(ctx.expresion())
            
            # Convertir el valor al tipo adecuado si es necesario
            if value is not None:
                if type_name == "ent":
                    value = int(value)
                elif type_name == "flt":
                    value = float(value)
                elif type_name == "lg":
                    value = int(value)
        
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
        
        # Evaluar la expresión si es posible
        value = self.evaluate_expression(ctx.expresion())
        
        # Convertir el valor al tipo adecuado si es necesario
        if value is not None:
            if symbol.type == "ent":
                value = int(value)
            elif symbol.type == "flt":
                value = float(value)
            elif symbol.type == "lg":
                value = int(value)
        
        # Actualizar el valor
        self.symbol_table.update(name, value)

    # Verificar expresiones (incluyendo operaciones aritméticas)
    def enterExpresion(self, ctx):
        # Verificamos la división por cero
        for i, op in enumerate(ctx.operadoresAritmeticos()):
            if op.getText() == '/' and i+1 < len(ctx.termino()):
                term = ctx.termino(i+1)
                # Si el término es un número literal
                if term.NUMERO_VALORES() and term.NUMERO_VALORES().getText() == '0':
                    self.add_error(ctx, "División por cero")
                    return

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
        
        # Recopilar información de parámetros
        params_info = []
        if ctx.parametros():
            param_ctx = ctx.parametros()
            param_types = param_ctx.tipo()
            param_names = param_ctx.ID()
            
            for i in range(len(param_types)):
                param_type = self.get_param_type(param_types[i])
                param_name = param_names[i].getText()
                params_info.append((param_name, param_type))
        
        # Declarar la función con sus parámetros
        self.symbol_table.declare(name, return_type, False, None, params_info)
        
        # Crear un nuevo ámbito para los parámetros y variables locales
        self.symbol_table.enter_scope(f"función_{name}")
        self.current_function_type = return_type
        self.has_return = False
        
        # Declarar los parámetros en el ámbito local
        if ctx.parametros():
            param_ctx = ctx.parametros()
            param_types = param_ctx.tipo()
            param_names = param_ctx.ID()
            
            for i in range(len(param_types)):
                param_type = self.get_param_type(param_types[i])
                param_name = param_names[i].getText()
                
                # Verificar si ya existe en el ámbito actual
                if param_name in self.symbol_table.get_current_scope_symbols():
                    self.add_error(param_ctx, f"Parámetro '{param_name}' duplicado")
                    continue
                
                # Declarar el parámetro
                self.symbol_table.declare(param_name, param_type, False, None)

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
        self.symbol_table.declare(name, "void")
        
        # Crear un nuevo ámbito para los parámetros y variables locales
        self.symbol_table.enter_scope(f"función_{name}")
        
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
                
                # Declarar el parámetro
                self.symbol_table.declare(param_name, param_type, False, None)

    def exitFuncionSinRetorno(self, ctx):
        # Salir del ámbito
        self.symbol_table.exit_scope()

    # Entrar a un ciclo o un if
    def enterEstructuraIf(self, ctx):
        self.symbol_table.enter_scope("if")

    def exitEstructuraIf(self, ctx):
        self.symbol_table.exit_scope()

    def enterCicloFor(self, ctx):
        self.symbol_table.enter_scope("for")

    def exitCicloFor(self, ctx):
        self.symbol_table.exit_scope()

    def enterCicloWhile(self, ctx):
        self.symbol_table.enter_scope("while")

    def exitCicloWhile(self, ctx):
        self.symbol_table.exit_scope()

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
            self.add_error(ctx, "Sentencia de retorno fuera de función")
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
        
        # Verificar número de parámetros
        expected_params = function.params if function.params else []
        actual_params = ctx.expresion()
        
        if len(actual_params) != len(expected_params):
            self.add_error(ctx, f"Número incorrecto de parámetros en llamada a '{function_name}': esperados {len(expected_params)}, encontrados {len(actual_params)}")
            return
        
        # Verificar tipos de parámetros
        for i, (param_name, param_type) in enumerate(expected_params):
            expr_type = self.get_expression_type(actual_params[i])
            if expr_type is None:
                continue  # Ya se reportó un error
            
            compat_type = self.get_type_compatibility(param_type, expr_type)
            if compat_type is None:
                self.add_error(ctx, f"Tipo incompatible en parámetro {i+1} de '{function_name}': esperado '{param_type}', encontrado '{expr_type}'")