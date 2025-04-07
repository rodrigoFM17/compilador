#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, auto

# Importamos las clases necesarias de los analizadores anteriores
try:
    from lexClaude import TipoToken, Token, AnalizadorLexico
    from sintaticClaude import Nodo, AnalizadorSintactico, ErrorSintactico
except ImportError:
    # Si el archivo se ejecuta directamente, definimos estructuras básicas
    class TipoToken(Enum):
        pass
    
    class Token:
        pass
    
    class Nodo:
        pass


class TipoDato(Enum):
    """Tipos de datos permitidos en el lenguaje."""
    ENTERO = auto()
    FLOTANTE = auto()
    LOGICO = auto()
    CADENA = auto()
    VOID = auto()  # Para funciones sin retorno
    ERROR = auto()  # Para indicar un error de tipo


class Ambito:
    """Representa un ámbito de variables y funciones."""
    
    def __init__(self, padre=None, nombre="global"):
        self.padre = padre
        self.nombre = nombre
        self.variables = {}  # Diccionario de variables en este ámbito
        self.funciones = {}  # Diccionario de funciones en este ámbito
    
    def definir_variable(self, nombre, tipo, es_constante=False, inicializada=False):
        """Define una variable en este ámbito."""
        if nombre in self.variables:
            return False  # Variable ya definida en este ámbito
        
        self.variables[nombre] = {
            'tipo': tipo,
            'es_constante': es_constante,
            'inicializada': inicializada
        }
        return True
    
    def definir_funcion(self, nombre, tipo_retorno, parametros):
        """Define una función en este ámbito."""
        if nombre in self.funciones:
            return False  # Función ya definida en este ámbito
        
        self.funciones[nombre] = {
            'tipo_retorno': tipo_retorno,
            'parametros': parametros
        }
        return True
    
    def obtener_variable(self, nombre):
        """Busca una variable en este ámbito y sus padres."""
        if nombre in self.variables:
            return self.variables[nombre]
        
        if self.padre:
            return self.padre.obtener_variable(nombre)
        
        return None  # Variable no encontrada
    
    def obtener_funcion(self, nombre):
        """Busca una función en este ámbito y sus padres."""
        if nombre in self.funciones:
            return self.funciones[nombre]
        
        if self.padre:
            return self.padre.obtener_funcion(nombre)
        
        return None  # Función no encontrada


class ErrorSemantico(Exception):
    """Excepción para errores semánticos durante el análisis."""
    def __init__(self, mensaje, nodo=None):
        self.mensaje = mensaje
        self.nodo = nodo
        if nodo and hasattr(nodo, 'linea') and hasattr(nodo, 'columna'):
            super().__init__(f"{mensaje} en línea {nodo.linea}, columna {nodo.columna}")
        else:
            super().__init__(mensaje)


class AnalizadorSemantico:
    """Analizador semántico para la gramática definida."""
    
    def __init__(self, ast):
        self.ast = ast
        self.ambito_actual = Ambito()  # Ámbito global
        self.errores = []
        self.dentro_de_funcion = False
        self.tipo_retorno_actual = None
    
    def analizar(self):
        """Comienza el análisis semántico del AST."""
        if not self.ast:
            return False
        
        try:
            self.visitar(self.ast)
            return len(self.errores) == 0
        except ErrorSemantico as e:
            self.errores.append(str(e))
            return False
    
    def visitar(self, nodo):
        """Visita un nodo del AST y ejecuta el método correspondiente."""
        if not isinstance(nodo, Nodo):
            return None
        
        nombre_metodo = f"visitar_{nodo.tipo.lower().replace('ó', 'o').replace('í', 'i')}"
        metodo = getattr(self, nombre_metodo, self.visitar_desconocido)
        return metodo(nodo)
    
    def visitar_desconocido(self, nodo):
        """Método por defecto para nodos desconocidos."""
        for hijo in nodo.hijos:
            self.visitar(hijo)
        return None
    
    def visitar_programa(self, nodo):
        """Visita el nodo raíz del programa."""
        for hijo in nodo.hijos:
            self.visitar(hijo)
        return None
    
    def visitar_declaracion(self, nodo):
        """Visita un nodo de declaración de variable."""
        # Verificar si hay un modificador de constante
        es_constante = False
        indice_tipo = 0
        
        if len(nodo.hijos) > 0 and hasattr(nodo.hijos[0], 'tipo') and (nodo.hijos[0].tipo == TipoToken.CONST or nodo.hijos[0].tipo == TipoToken.FINAL):
            es_constante = True
            indice_tipo = 1
        
        # Obtener el tipo de dato
        if indice_tipo < len(nodo.hijos) and hasattr(nodo.hijos[indice_tipo], 'tipo'):
            token_tipo = nodo.hijos[indice_tipo]
            tipo = self._convertir_token_a_tipo(token_tipo)
        else:
            self.errores.append("Error semántico: Falta el tipo de dato en la declaración")
            return None
        
        # Obtener el identificador
        if indice_tipo + 1 < len(nodo.hijos) and hasattr(nodo.hijos[indice_tipo + 1], 'lexema'):
            token_id = nodo.hijos[indice_tipo + 1]
            nombre = token_id.lexema
        else:
            self.errores.append("Error semántico: Falta el identificador en la declaración")
            return None
        
        # Verificar si ya existe en el ámbito actual
        if self.ambito_actual.variables.get(nombre) is not None:
            self.errores.append(f"Error semántico: Variable '{nombre}' ya definida en este ámbito")
            return None
        
        # Verificar si hay inicialización
        inicializada = False
        valor_tipo = None
        
        if len(nodo.hijos) > indice_tipo + 2 and hasattr(nodo.hijos[indice_tipo + 2], 'tipo') and nodo.hijos[indice_tipo + 2].tipo == TipoToken.IGUAL:
            inicializada = True
            # Si es scn(), no validamos el tipo
            if (indice_tipo + 3 < len(nodo.hijos) and 
                hasattr(nodo.hijos[indice_tipo + 3], 'tipo') and 
                nodo.hijos[indice_tipo + 3].tipo == TipoToken.SCN):
                pass
            elif indice_tipo + 3 < len(nodo.hijos):
                # Validar el tipo de la expresión
                valor_tipo = self.visitar(nodo.hijos[indice_tipo + 3])
                # Verificar que valor_tipo no sea None antes de acceder a name
                if valor_tipo is not None and valor_tipo != TipoDato.ERROR and valor_tipo != tipo:
                    self.errores.append(f"Error semántico: Tipo incompatible en la asignación. Se esperaba {tipo.name}, pero se encontró {valor_tipo.name}")
                elif valor_tipo is None:
                    self.errores.append(f"Error semántico: No se pudo determinar el tipo de la expresión en la asignación")
        
        # Registrar la variable en el ámbito actual
        self.ambito_actual.definir_variable(nombre, tipo, es_constante, inicializada)
        
        return None
    
    def visitar_asignacion(self, nodo):
        """Visita un nodo de asignación."""
        # Comprobar que hay suficientes hijos
        if len(nodo.hijos) < 2:
            self.errores.append("Error semántico: Faltan componentes en la asignación")
            return None
            
        # Obtener el identificador
        if hasattr(nodo.hijos[0], 'lexema'):
            token_id = nodo.hijos[0]
            nombre = token_id.lexema
        else:
            self.errores.append("Error semántico: Identificador inválido en asignación")
            return None
        
        # Verificar si la variable existe
        variable = self.ambito_actual.obtener_variable(nombre)
        if not variable:
            self.errores.append(f"Error semántico: Variable '{nombre}' no definida")
            return None
        
        # Verificar si es una constante
        if variable['es_constante'] and variable['inicializada']:
            self.errores.append(f"Error semántico: No se puede modificar la constante '{nombre}'")
            return None
        
        # Validar el tipo de la expresión
        valor_tipo = self.visitar(nodo.hijos[1])
        
        # Verificar que valor_tipo no sea None antes de acceder a name
        if valor_tipo is not None and valor_tipo != TipoDato.ERROR and valor_tipo != variable['tipo']:
            self.errores.append(f"Error semántico: Tipo incompatible en la asignación. Se esperaba {variable['tipo'].name}, pero se encontró {valor_tipo.name}")
        elif valor_tipo is None:
            self.errores.append(f"Error semántico: No se pudo determinar el tipo de la expresión en la asignación")
        
        # Marcar la variable como inicializada
        variable['inicializada'] = True
        
        return None
    
    def visitar_operacionaritmetica(self, nodo):
        """Visita un nodo de operación aritmética."""
        # Si no hay hijos, retornar ERROR
        if not nodo.hijos:
            return TipoDato.ERROR
        
        # Si solo hay un hijo, procesarlo directamente
        if len(nodo.hijos) == 1:
            if isinstance(nodo.hijos[0], Nodo):
                return self.visitar(nodo.hijos[0])
            elif hasattr(nodo.hijos[0], 'tipo'):
                # Si es un token identificador
                if nodo.hijos[0].tipo == TipoToken.IDENTIFICADOR:
                    nombre = nodo.hijos[0].lexema
                    variable = self.ambito_actual.obtener_variable(nombre)
                    if not variable:
                        self.errores.append(f"Error semántico: Variable '{nombre}' no definida")
                        return TipoDato.ERROR
                    
                    if not variable['inicializada']:
                        self.errores.append(f"Error semántico: Variable '{nombre}' no inicializada")
                    
                    return variable['tipo']
                # Si es un número entero
                elif nodo.hijos[0].tipo == TipoToken.NUMERO_ENTERO:
                    return TipoDato.ENTERO
                # Si es un número flotante
                elif nodo.hijos[0].tipo == TipoToken.NUMERO_FLOTANTE:
                    return TipoDato.FLOTANTE
            
            # Si no podemos determinar el tipo
            return TipoDato.ERROR
        
        # Obtener los tipos de los operandos
        tipos = []
        for i in range(0, len(nodo.hijos), 2):
            if isinstance(nodo.hijos[i], Nodo):
                tipo = self.visitar(nodo.hijos[i])
            elif hasattr(nodo.hijos[i], 'tipo'):
                # Si es un token identificador
                if nodo.hijos[i].tipo == TipoToken.IDENTIFICADOR:
                    nombre = nodo.hijos[i].lexema
                    variable = self.ambito_actual.obtener_variable(nombre)
                    if not variable:
                        self.errores.append(f"Error semántico: Variable '{nombre}' no definida")
                        tipo = TipoDato.ERROR
                    else:
                        if not variable['inicializada']:
                            self.errores.append(f"Error semántico: Variable '{nombre}' no inicializada")
                        tipo = variable['tipo']
                # Si es un número entero
                elif nodo.hijos[i].tipo == TipoToken.NUMERO_ENTERO:
                    tipo = TipoDato.ENTERO
                # Si es un número flotante
                elif nodo.hijos[i].tipo == TipoToken.NUMERO_FLOTANTE:
                    tipo = TipoDato.FLOTANTE
                else:
                    tipo = TipoDato.ERROR
            else:
                tipo = TipoDato.ERROR
            
            tipos.append(tipo)
        
        # Verificar compatibilidad de los operandos
        operadores = []
        for i in range(1, len(nodo.hijos), 2):
            if hasattr(nodo.hijos[i], 'tipo'):
                operadores.append(nodo.hijos[i].tipo)
        
        tipo_resultante = self._tipo_operacion(tipos, operadores[0] if operadores else None)
        
        if tipo_resultante == TipoDato.ERROR:
            self.errores.append("Error semántico: Operandos incompatibles en operación aritmética")
        
        return tipo_resultante
    
    def visitar_termino(self, nodo):
        """Visita un nodo de término."""
        print(f"DEBUG - Visitando término con {len(nodo.hijos)} hijos")
        
        # Si no hay hijos, retornar ERROR
        if not nodo.hijos:
            return TipoDato.ERROR
        
        # Si solo hay un factor, devolver su tipo
        if len(nodo.hijos) == 1:
            return self.visitar(nodo.hijos[0])
        
        # Obtener los tipos de los operandos
        tipos = []
        for i in range(0, len(nodo.hijos), 2):
            tipo = self.visitar(nodo.hijos[i])
            tipos.append(tipo)
        
        # Verificar compatibilidad de los operandos
        operadores = []
        for i in range(1, len(nodo.hijos), 2):
            if hasattr(nodo.hijos[i], 'tipo'):
                operadores.append(nodo.hijos[i].tipo)
        
        tipo_resultante = self._tipo_operacion(tipos, operadores[0] if operadores else None)
        
        if tipo_resultante == TipoDato.ERROR:
            self.errores.append("Error semántico: Operandos incompatibles en término")
        
        return tipo_resultante
    
    def visitar_factor(self, nodo):
        """Visita un nodo de factor."""
        print(f"DEBUG - Visitando factor con {len(nodo.hijos)} hijos")
        
        # Si no hay hijos, retornar ERROR
        if not nodo.hijos:
            return TipoDato.ERROR
        
        # Si es un nodo
        if isinstance(nodo.hijos[0], Nodo):
            return self.visitar(nodo.hijos[0])
        
        # Si es un token
        if hasattr(nodo.hijos[0], 'tipo'):
            print(f"DEBUG - Factor tiene token: {nodo.hijos[0].tipo}")
            
            # Si es un número entero
            if nodo.hijos[0].tipo == TipoToken.NUMERO_ENTERO:
                print("DEBUG - Factor es número entero")
                return TipoDato.ENTERO
            
            # Si es un número flotante
            if nodo.hijos[0].tipo == TipoToken.NUMERO_FLOTANTE:
                return TipoDato.FLOTANTE
            
            # Si es un identificador
            if nodo.hijos[0].tipo == TipoToken.IDENTIFICADOR:
                nombre = nodo.hijos[0].lexema
                variable = self.ambito_actual.obtener_variable(nombre)
                if not variable:
                    self.errores.append(f"Error semántico: Variable '{nombre}' no definida")
                    return TipoDato.ERROR
                
                if not variable['inicializada']:
                    self.errores.append(f"Error semántico: Variable '{nombre}' no inicializada")
                
                return variable['tipo']
        
        # Si no podemos determinar el tipo
        print("DEBUG - No se pudo determinar el tipo del factor")
        return TipoDato.ERROR
    
    def visitar_llamadafuncion(self, nodo):
        """Visita un nodo de llamada a función."""
        # Obtener el nombre de la función
        nombre = nodo.hijos[0].lexema
        
        # Verificar si la función existe
        funcion = self.ambito_actual.obtener_funcion(nombre)
        if not funcion:
            self.errores.append(f"Error semántico: Función '{nombre}' no definida")
            return TipoDato.ERROR
        
        # Verificar el número de argumentos
        parametros = funcion['parametros']
        argumentos = [nodo.hijos[i] for i in range(1, len(nodo.hijos))]
        
        if len(parametros) != len(argumentos):
            self.errores.append(f"Error semántico: Número incorrecto de argumentos en llamada a '{nombre}'. Se esperaban {len(parametros)}, pero se encontraron {len(argumentos)}")
            return funcion['tipo_retorno']
        
        # Verificar los tipos de los argumentos
        for i, arg in enumerate(argumentos):
            tipo_arg = self.visitar(arg)
            if tipo_arg != TipoDato.ERROR and tipo_arg != parametros[i]['tipo']:
                self.errores.append(f"Error semántico: Tipo incompatible en argumento {i+1} de '{nombre}'. Se esperaba {parametros[i]['tipo'].name}, pero se encontró {tipo_arg.name}")
        
        return funcion['tipo_retorno']
    
    def visitar_expresion(self, nodo):
        """Visita un nodo de expresión."""
        # Si no hay hijos, retornar ERROR
        if not nodo.hijos:
            return TipoDato.ERROR
        
        # Si el primer hijo es un identificador
        if hasattr(nodo.hijos[0], 'tipo') and nodo.hijos[0].tipo == TipoToken.IDENTIFICADOR:
            nombre = nodo.hijos[0].lexema
            variable = self.ambito_actual.obtener_variable(nombre)
            if not variable:
                self.errores.append(f"Error semántico: Variable '{nombre}' no definida")
                return TipoDato.ERROR
            
            if not variable['inicializada']:
                self.errores.append(f"Error semántico: Variable '{nombre}' no inicializada")
            
            return variable['tipo']
        
        # Si el hijo es un nodo, visitar recursivamente
        if isinstance(nodo.hijos[0], Nodo):
            return self.visitar(nodo.hijos[0])
        
        # Si es un número o una cadena
        if hasattr(nodo.hijos[0], 'tipo'):
            if nodo.hijos[0].tipo == TipoToken.NUMERO_ENTERO:
                return TipoDato.ENTERO
            elif nodo.hijos[0].tipo == TipoToken.NUMERO_FLOTANTE:
                return TipoDato.FLOTANTE
            elif nodo.hijos[0].tipo == TipoToken.CADENA:
                return TipoDato.CADENA
        
        # Si no podemos determinar el tipo
        return TipoDato.ERROR
    
    def visitar_expresionlogica(self, nodo):
        """Visita un nodo de expresión lógica."""
        # Verificar los operandos
        izq_tipo = self.visitar(nodo.hijos[0])
        der_tipo = self.visitar(nodo.hijos[2])
        
        # Verificar compatibilidad para comparación
        if izq_tipo == TipoDato.ERROR or der_tipo == TipoDato.ERROR:
            return TipoDato.LOGICO
        
        if not self._son_tipos_compatibles_para_comparacion(izq_tipo, der_tipo):
            self.errores.append(f"Error semántico: Tipos incompatibles en expresión lógica. No se pueden comparar {izq_tipo.name} y {der_tipo.name}")
        
        return TipoDato.LOGICO
    
    def visitar_estructuraif(self, nodo):
        """Visita un nodo de estructura if."""
        # Verificar la condición
        cond_tipo = self.visitar(nodo.hijos[0])
        if cond_tipo != TipoDato.LOGICO and cond_tipo != TipoDato.ERROR:
            self.errores.append(f"Error semántico: La condición del if debe ser de tipo lógico, pero es de tipo {cond_tipo.name}")
        
        # Crear un nuevo ámbito para el bloque if
        ambito_padre = self.ambito_actual
        self.ambito_actual = Ambito(ambito_padre, "if")
        
        # Visitar el bloque if
        self.visitar(nodo.hijos[1])
        
        # Restaurar el ámbito
        self.ambito_actual = ambito_padre
        
        # Si hay un bloque else
        if len(nodo.hijos) > 2:
            # Crear un nuevo ámbito para el bloque else
            self.ambito_actual = Ambito(ambito_padre, "else")
            
            # Visitar el bloque else
            self.visitar(nodo.hijos[2])
            
            # Restaurar el ámbito
            self.ambito_actual = ambito_padre
        
        return None
    
    def visitar_ciclofor(self, nodo):
        """Visita un nodo de ciclo for."""
        # Crear un nuevo ámbito para el for
        ambito_padre = self.ambito_actual
        self.ambito_actual = Ambito(ambito_padre, "for")
        
        # Visitar la inicialización
        self.visitar(nodo.hijos[0])
        
        # Verificar la condición
        cond_tipo = self.visitar(nodo.hijos[1])
        if cond_tipo != TipoDato.LOGICO and cond_tipo != TipoDato.ERROR:
            self.errores.append(f"Error semántico: La condición del for debe ser de tipo lógico, pero es de tipo {cond_tipo.name}")
        
        # Visitar la actualización
        self.visitar(nodo.hijos[2])
        
        # Visitar el bloque for
        self.visitar(nodo.hijos[3])
        
        # Restaurar el ámbito
        self.ambito_actual = ambito_padre
        
        return None
    
    def visitar_ciclowhile(self, nodo):
        """Visita un nodo de ciclo while."""
        # Verificar la condición
        cond_tipo = self.visitar(nodo.hijos[0])
        if cond_tipo != TipoDato.LOGICO and cond_tipo != TipoDato.ERROR:
            self.errores.append(f"Error semántico: La condición del while debe ser de tipo lógico, pero es de tipo {cond_tipo.name}")
        
        # Crear un nuevo ámbito para el while
        ambito_padre = self.ambito_actual
        self.ambito_actual = Ambito(ambito_padre, "while")
        
        # Visitar el bloque while
        self.visitar(nodo.hijos[1])
        
        # Restaurar el ámbito
        self.ambito_actual = ambito_padre
        
        return None
    
    def visitar_impresion(self, nodo):
        """Visita un nodo de impresión (clg)."""
        # Si el argumento es un identificador
        if nodo.hijos[0].tipo == TipoToken.IDENTIFICADOR:
            nombre = nodo.hijos[0].lexema
            variable = self.ambito_actual.obtener_variable(nombre)
            if not variable:
                self.errores.append(f"Error semántico: Variable '{nombre}' no definida")
            elif not variable['inicializada']:
                self.errores.append(f"Error semántico: Variable '{nombre}' no inicializada")
        
        # Si el argumento es una cadena, verificar las variables interpoladas
        elif nodo.hijos[0].tipo == TipoToken.CADENA:
            cadena = nodo.hijos[0].lexema
            # Encontrar todas las variables interpoladas (después de $)
            partes = cadena.split('$')
            for i in range(1, len(partes)):
                # Extraer el nombre de la variable (hasta el primer carácter no alfanumérico)
                nombre = ""
                for c in partes[i]:
                    if c.isalnum() or c == '_':
                        nombre += c
                    else:
                        break
                
                if nombre:
                    variable = self.ambito_actual.obtener_variable(nombre)
                    if not variable:
                        self.errores.append(f"Error semántico: Variable interpolada '{nombre}' no definida")
                    elif not variable['inicializada']:
                        self.errores.append(f"Error semántico: Variable interpolada '{nombre}' no inicializada")
        
        return None
    
    def visitar_funcionconretorno(self, nodo):
        """Visita un nodo de función con retorno."""
        # Obtener el nombre de la función
        nombre = nodo.hijos[0].lexema
        
        # Verificar si ya existe en el ámbito actual
        if nombre in self.ambito_actual.funciones:
            self.errores.append(f"Error semántico: Función '{nombre}' ya definida en este ámbito")
            return None
        
        # Obtener el tipo de retorno
        token_tipo = nodo.hijos[-2]  # El tipo de retorno está antes del cuerpo de la función
        tipo_retorno = self._convertir_token_a_tipo(token_tipo)
        
        # Procesar los parámetros si existen
        parametros = []
        if len(nodo.hijos) > 2 and isinstance(nodo.hijos[1], Nodo) and nodo.hijos[1].tipo == "Parámetros":
            parametros_nodo = nodo.hijos[1]
            for param_nodo in parametros_nodo.hijos:
                tipo_param = self._convertir_token_a_tipo(param_nodo.hijos[0])
                nombre_param = param_nodo.hijos[1].lexema
                parametros.append({'nombre': nombre_param, 'tipo': tipo_param})
        
        # Registrar la función en el ámbito actual
        self.ambito_actual.definir_funcion(nombre, tipo_retorno, parametros)
        
        # Crear un nuevo ámbito para la función
        ambito_padre = self.ambito_actual
        self.ambito_actual = Ambito(ambito_padre, nombre)
        
        # Registrar los parámetros en el ámbito de la función
        for param in parametros:
            self.ambito_actual.definir_variable(param['nombre'], param['tipo'], False, True)
        
        # Establecer el contexto de la función
        self.dentro_de_funcion = True
        self.tipo_retorno_actual = tipo_retorno
        
        # Visitar el cuerpo de la función
        cuerpo_nodo = nodo.hijos[-1]
        self.visitar(cuerpo_nodo)
        
        # Restaurar el contexto
        self.dentro_de_funcion = False
        self.tipo_retorno_actual = None
        
        # Restaurar el ámbito
        self.ambito_actual = ambito_padre
        
        return None
    
    def visitar_funcionsinretorno(self, nodo):
        """Visita un nodo de función sin retorno."""
        # Obtener el nombre de la función
        nombre = nodo.hijos[0].lexema
        
        # Verificar si ya existe en el ámbito actual
        if nombre in self.ambito_actual.funciones:
            self.errores.append(f"Error semántico: Función '{nombre}' ya definida en este ámbito")
            return None
        
        # Procesar los parámetros si existen
        parametros = []
        if len(nodo.hijos) > 1 and isinstance(nodo.hijos[1], Nodo) and nodo.hijos[1].tipo == "Parámetros":
            parametros_nodo = nodo.hijos[1]
            for param_nodo in parametros_nodo.hijos:
                tipo_param = self._convertir_token_a_tipo(param_nodo.hijos[0])
                nombre_param = param_nodo.hijos[1].lexema
                parametros.append({'nombre': nombre_param, 'tipo': tipo_param})
        
        # Registrar la función en el ámbito actual
        self.ambito_actual.definir_funcion(nombre, TipoDato.VOID, parametros)
        
        # Crear un nuevo ámbito para la función
        ambito_padre = self.ambito_actual
        self.ambito_actual = Ambito(ambito_padre, nombre)
        
        # Registrar los parámetros en el ámbito de la función
        for param in parametros:
            self.ambito_actual.definir_variable(param['nombre'], param['tipo'], False, True)
        
        # Establecer el contexto de la función
        self.dentro_de_funcion = True
        self.tipo_retorno_actual = TipoDato.VOID
        
        # Visitar el cuerpo de la función
        cuerpo_nodo = nodo.hijos[-1]
        self.visitar(cuerpo_nodo)
        
        # Restaurar el contexto
        self.dentro_de_funcion = False
        self.tipo_retorno_actual = None
        
        # Restaurar el ámbito
        self.ambito_actual = ambito_padre
        
        return None
    
    def _procesar_operacion_aritmetica_simple(self, nodo):
        """Procesa una operación aritmética simple para determinar su tipo."""
        print(f"DEBUG - Procesando operación aritmética con {len(nodo.hijos)} hijos")
        
        # Si no hay hijos, error
        if not nodo.hijos:
            return TipoDato.ERROR
        
        # Si solo hay un hijo (caso común en el AST que vimos)
        if len(nodo.hijos) == 1:
            hijo = nodo.hijos[0]
            
            # El hijo es un nodo Término
            if isinstance(hijo, Nodo):
                print(f"DEBUG - Hijo único es un nodo de tipo: {hijo.tipo}")
                
                # Si es un nodo Término con un hijo Factor
                if hijo.tipo == "Término" and len(hijo.hijos) > 0:
                    termino_hijo = hijo.hijos[0]
                    print(f"DEBUG - Hijo de Término es un nodo de tipo: {termino_hijo.tipo}")
                    
                    # Si el hijo de Término es un Factor con un hijo Token
                    if termino_hijo.tipo == "Factor" and len(termino_hijo.hijos) > 0:
                        factor_hijo = termino_hijo.hijos[0]
                        
                        # Si es un token literal
                        if hasattr(factor_hijo, 'tipo'):
                            print(f"DEBUG - Hijo de Factor es un token: {factor_hijo.tipo}")
                            
                            if factor_hijo.tipo == TipoToken.NUMERO_ENTERO:
                                return TipoDato.ENTERO
                            elif factor_hijo.tipo == TipoToken.NUMERO_FLOTANTE:
                                return TipoDato.FLOTANTE
                    
                    # Intentar visitar directamente el nodo Factor
                    return self.visitar(termino_hijo)
                
                # Visitar el hijo directamente
                return self.visitar(hijo)
            
            # Si es un token directo (improbable pero posible)
            if hasattr(hijo, 'tipo'):
                print(f"DEBUG - Token directo en operación: {hijo.tipo}")
                
                if hijo.tipo == TipoToken.NUMERO_ENTERO:
                    return TipoDato.ENTERO
                elif hijo.tipo == TipoToken.NUMERO_FLOTANTE:
                    return TipoDato.FLOTANTE
                elif hijo.tipo == TipoToken.IDENTIFICADOR:
                    variable = self.ambito_actual.obtener_variable(hijo.lexema)
                    if variable:
                        return variable['tipo']
                    else:
                        self.errores.append(f"Error semántico: Variable '{hijo.lexema}' no definida")
                        return TipoDato.ERROR
        
        # Si hay más hijos (operación binaria)
        if len(nodo.hijos) >= 3:
            # Verificar el primer operando
            tipo1 = self._procesar_operando(nodo.hijos[0])
            
            # Verificar el segundo operando
            tipo2 = self._procesar_operando(nodo.hijos[2])
            
            # Determinar el tipo resultante
            if tipo1 == TipoDato.ERROR or tipo2 == TipoDato.ERROR:
                return TipoDato.ERROR
            
            if tipo1 == TipoDato.FLOTANTE or tipo2 == TipoDato.FLOTANTE:
                return TipoDato.FLOTANTE
            
            return TipoDato.ENTERO
        
        return TipoDato.ERROR
    
    def _procesar_expresion_simple(self, nodo):
        """Procesa una expresión simple para determinar su tipo."""
        print(f"DEBUG - Procesando expresión con {len(nodo.hijos)} hijos")
        
        # Si no hay hijos, error
        if not nodo.hijos:
            return TipoDato.ERROR
        
        # Procesar el primer hijo
        hijo = nodo.hijos[0]
        
        # Si es un nodo
        if isinstance(hijo, Nodo):
            return self.visitar(hijo)
        
        # Si es un token
        if hasattr(hijo, 'tipo'):
            print(f"DEBUG - Token en expresión: {hijo.tipo.name}, lexema: {hijo.lexema}")
            
            if hijo.tipo == TipoToken.NUMERO_ENTERO:
                return TipoDato.ENTERO
            elif hijo.tipo == TipoToken.NUMERO_FLOTANTE:
                return TipoDato.FLOTANTE
            elif hijo.tipo == TipoToken.IDENTIFICADOR:
                variable = self.ambito_actual.obtener_variable(hijo.lexema)
                if variable:
                    return variable['tipo']
                else:
                    self.errores.append(f"Error semántico: Variable '{hijo.lexema}' no definida")
                    return TipoDato.ERROR
        
        return TipoDato.ERROR

    def _procesar_operando(self, nodo_o_token):
        """Procesa un operando (nodo o token) para determinar su tipo."""
        # Si es un nodo
        if isinstance(nodo_o_token, Nodo):
            return self.visitar(nodo_o_token)
        
        # Si es un token
        if hasattr(nodo_o_token, 'tipo'):
            if nodo_o_token.tipo == TipoToken.NUMERO_ENTERO:
                return TipoDato.ENTERO
            elif nodo_o_token.tipo == TipoToken.NUMERO_FLOTANTE:
                return TipoDato.FLOTANTE
            elif nodo_o_token.tipo == TipoToken.IDENTIFICADOR:
                variable = self.ambito_actual.obtener_variable(nodo_o_token.lexema)
                if variable:
                    return variable['tipo']
                else:
                    self.errores.append(f"Error semántico: Variable '{nodo_o_token.lexema}' no definida")
                    return TipoDato.ERROR
        
        return TipoDato.ERROR
    
    def visitar_sentenciareturn(self, nodo):
        """Visita un nodo de sentencia return."""
        # Verificar si estamos dentro de una función
        if not self.dentro_de_funcion:
            self.errores.append("Error semántico: Sentencia 'return' fuera de una función")
            return None
        
        # Si es un return sin expresión
        if len(nodo.hijos) == 0:
            if self.tipo_retorno_actual != TipoDato.VOID:
                self.errores.append(f"Error semántico: Se esperaba un valor de retorno de tipo {self.tipo_retorno_actual.name}")
            return None
        
        print(f"DEBUG - SentenciaReturn con {len(nodo.hijos)} hijos")
        
        # Procesar la expresión de retorno según su tipo
        tipo_expr = None
        
        # Este es el camino directo para obtener el tipo de una estructura como la que vemos en el AST
        if len(nodo.hijos) > 0:
            hijo_operacion = nodo.hijos[0]
            
            if isinstance(hijo_operacion, Nodo) and hijo_operacion.tipo == "OperaciónAritmética" and len(hijo_operacion.hijos) > 0:
                hijo_termino = hijo_operacion.hijos[0]
                
                if isinstance(hijo_termino, Nodo) and hijo_termino.tipo == "Término" and len(hijo_termino.hijos) > 0:
                    hijo_factor = hijo_termino.hijos[0]
                    
                    if isinstance(hijo_factor, Nodo) and hijo_factor.tipo == "Factor" and len(hijo_factor.hijos) > 0:
                        token_numero = hijo_factor.hijos[0]
                        
                        if hasattr(token_numero, 'tipo'):
                            if token_numero.tipo == TipoToken.NUMERO_ENTERO:
                                print("DEBUG - Se detectó un número entero en la sentencia return")
                                tipo_expr = TipoDato.ENTERO
                            elif token_numero.tipo == TipoToken.NUMERO_FLOTANTE:
                                print("DEBUG - Se detectó un número flotante en la sentencia return")
                                tipo_expr = TipoDato.FLOTANTE
        
        # Si no pudimos determinar el tipo directamente, intentamos el método normal
        if tipo_expr is None:
            operacion = nodo.hijos[0]
            
            # Si es una operación aritmética, intentamos visitar directamente el término
            if isinstance(operacion, Nodo) and operacion.tipo == "OperaciónAritmética" and len(operacion.hijos) > 0:
                termino = operacion.hijos[0]
                if isinstance(termino, Nodo) and termino.tipo == "Término":
                    tipo_expr = TipoDato.ENTERO  # Asumimos entero como caso base para literales
        
        # Si aún no tenemos tipo, intentamos visitar normalmente
        if tipo_expr is None:
            tipo_expr = self.visitar(nodo.hijos[0])
        
        # Verificar que tipo_expr no sea None
        if tipo_expr is None:
            self.errores.append("Error semántico: No se pudo determinar el tipo de la expresión de retorno")
        elif tipo_expr != TipoDato.ERROR and tipo_expr != self.tipo_retorno_actual:
            self.errores.append(f"Error semántico: Tipo de retorno incompatible. Se esperaba {self.tipo_retorno_actual.name}, pero se encontró {tipo_expr.name}")
        
        return None
    
    def visitar_bloque(self, nodo):
        """Visita un nodo de bloque (if, else, for, while, función)."""
        for hijo in nodo.hijos:
            self.visitar(hijo)
        return None
    
    def visitar_cuerpofuncion(self, nodo):
        """Visita el cuerpo de una función."""
        for hijo in nodo.hijos:
            self.visitar(hijo)
        return None
    
    def visitar_bloqueif(self, nodo):
        """Visita el bloque de un if."""
        return self.visitar_bloque(nodo)
    
    def visitar_bloqueelse(self, nodo):
        """Visita el bloque de un else."""
        return self.visitar_bloque(nodo)
    
    def visitar_bloquefor(self, nodo):
        """Visita el bloque de un for."""
        return self.visitar_bloque(nodo)
    
    def visitar_bloquewhile(self, nodo):
        """Visita el bloque de un while."""
        return self.visitar_bloque(nodo)
    
    def _convertir_token_a_tipo(self, token):
        """Convierte un token de tipo a un TipoDato."""
        if token.tipo == TipoToken.ENT:
            return TipoDato.ENTERO
        if token.tipo == TipoToken.FLT:
            return TipoDato.FLOTANTE
        if token.tipo == TipoToken.LG:
            return TipoDato.LOGICO
        if token.tipo == TipoToken.STR:
            return TipoDato.CADENA
        return TipoDato.ERROR
    
    def _tipo_operacion(self, tipos, operador=None):
        """Determina el tipo resultante de una operación aritmética."""
        # Filtrar tipos None
        tipos_validos = [t for t in tipos if t is not None]
        
        # Si no hay tipos válidos, retornar ERROR
        if not tipos_validos:
            return TipoDato.ERROR
        
        # Si algún operando es de tipo ERROR, el resultado es ERROR
        if TipoDato.ERROR in tipos_validos:
            return TipoDato.ERROR
        
        # Si hay más de un tipo diferente, verificar compatibilidad
        if len(set(tipos_validos)) > 1:
            # Solo permitimos mezclar ENTERO y FLOTANTE, el resultado es FLOTANTE
            if set(tipos_validos) == {TipoDato.ENTERO, TipoDato.FLOTANTE}:
                return TipoDato.FLOTANTE
            # Cualquier otra combinación es un error
            return TipoDato.ERROR
        
        # Si todos son del mismo tipo
        tipo = tipos_validos[0]
        
        # Verificar que el tipo sea compatible con operaciones aritméticas
        if tipo not in [TipoDato.ENTERO, TipoDato.FLOTANTE]:
            return TipoDato.ERROR
        
        # Si todos son del mismo tipo, devolvemos ese tipo
        return tipo 
    
    def _son_tipos_compatibles_para_comparacion(self, tipo1, tipo2):
        """Determina si dos tipos son compatibles para comparación."""
        # Cualquier tipo puede compararse consigo mismo
        if tipo1 == tipo2:
            return True
        
        # ENTERO y FLOTANTE son compatibles entre sí
        if {tipo1, tipo2} == {TipoDato.ENTERO, TipoDato.FLOTANTE}:
            return True
        
        # Cualquier otra combinación no es compatible
        return False
    
def imprimir_ast_detallado(nodo, nivel=0):
    """Imprime la estructura detallada del AST para depuración."""
    if not nodo:
        print("  " * nivel + "None")
        return
    
    if isinstance(nodo, Nodo):
        print("  " * nivel + f"Nodo: {nodo.tipo}")
        for i, hijo in enumerate(nodo.hijos):
            print("  " * nivel + f"Hijo {i}:")
            imprimir_ast_detallado(hijo, nivel + 1)
    else:
        if hasattr(nodo, 'tipo') and hasattr(nodo, 'lexema'):
            print("  " * nivel + f"Token: {nodo.tipo} = '{nodo.lexema}'")
        else:
            print("  " * nivel + f"Dato: {nodo}")


def probar_analizador_semantico_con_debug(codigo_fuente):
    """Función para probar el analizador semántico con depuración detallada."""
    print("=== ANÁLISIS LÉXICO ===")
    try:
        analizador_lexico = AnalizadorLexico(codigo_fuente)
        tokens = analizador_lexico.analizar()
        
        print("\n=== ANÁLISIS SINTÁCTICO ===")
        analizador_sintactico = AnalizadorSintactico(tokens)
        
        try:
            ast = analizador_sintactico.analizar()
            print("Análisis sintáctico completado con éxito.")
            
            print("\n=== ESTRUCTURA DETALLADA DEL AST ===")
            imprimir_ast_detallado(ast)
            
            print("\n=== ANÁLISIS SEMÁNTICO ===")
            analizador_semantico = AnalizadorSemantico(ast)
            resultado = analizador_semantico.analizar()
            
            if resultado:
                print("Análisis semántico completado con éxito.")
            else:
                print("Errores semánticos encontrados:")
                for error in analizador_semantico.errores:
                    print(f"  - {error}")
            
            return ast, analizador_semantico.errores
        except ErrorSintactico as e:
            print(f"Error sintáctico: {e}")
        except Exception as e:
            print(f"Error inesperado: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
    except Exception as e:
        print(f"Error durante el análisis léxico: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
    
    return None, []

if __name__ == '__main__':
    # Ejemplo de código fuente para probar
    codigo = '''
    ent x = 10;
    fct suma(ent a, ent b) : str {

        str ms = "fadsjfkla";
        return ms;
    }
    '''
    
    probar_analizador_semantico_con_debug(codigo)