#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
import sys

# Importamos el analizador léxico creado anteriormente
# Asumimos que está en un archivo llamado "analizador_lexico.py"
try:
    from lexClaude import TipoToken, Token, AnalizadorLexico
except ImportError:
    # Si estamos ejecutando este archivo directamente, definimos las clases aquí
    class TipoToken(Enum):
        # Palabras clave
        CONST = 1
        FINAL = 2
        ENT = 3
        FLT = 4
        LG = 5
        STR = 6
        SCN = 7
        CLG = 8
        FCT = 9
        IF = 10
        ELSE = 11
        FOR = 12
        WHILE = 13
        RETURN = 14
        
        # Identificadores y literales
        IDENTIFICADOR = 15
        NUMERO_ENTERO = 16
        NUMERO_FLOTANTE = 17
        CADENA = 18
        
        # Operadores y símbolos
        IGUAL = 19
        MAS = 20
        MENOS = 21
        MULTIPLICACION = 22
        DIVISION = 23
        MENOR = 24
        MAYOR = 25
        MENOR_IGUAL = 26
        MAYOR_IGUAL = 27
        IGUAL_IGUAL = 28
        DIFERENTE = 29
        
        # Puntuación
        PARENTESIS_IZQ = 30
        PARENTESIS_DER = 31
        LLAVE_IZQ = 32
        LLAVE_DER = 33
        PUNTO_COMA = 34
        COMA = 35
        DOS_PUNTOS = 36
        DOLAR = 37
        
        # Fin del archivo
        EOF = 38
        
        # Token desconocido
        ERROR = 39

    class Token:
        def __init__(self, tipo, lexema, linea, columna):
            self.tipo = tipo
            self.lexema = lexema
            self.linea = linea
            self.columna = columna
        
        def __str__(self):
            return f"Token({self.tipo.name}, '{self.lexema}', linea={self.linea}, columna={self.columna})"
        
class Nodo:
    """Clase base para los nodos del árbol de sintaxis abstracta (AST)."""
    def __init__(self, tipo):
        self.tipo = tipo
        self.hijos = []
    
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
    
    def imprimir(self, nivel=0):
        print("  " * nivel + self.tipo)
        for hijo in self.hijos:
            if isinstance(hijo, Nodo):
                hijo.imprimir(nivel + 1)
            else:
                print("  " * (nivel + 1) + str(hijo))

class AnalizadorSintactico:
    """Analizador sintáctico para la gramática definida."""
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
        self.token_actual = None
        self.avanzar()  # Inicializar token_actual con el primer token
    
    def avanzar(self):
        """Avanza al siguiente token."""
        if self.posicion < len(self.tokens):
            self.token_actual = self.tokens[self.posicion]
            self.posicion += 1
        return self.token_actual
    
    def retroceder(self):
        """Retrocede al token anterior."""
        self.posicion -= 1
        if self.posicion >= 0:
            self.token_actual = self.tokens[self.posicion - 1]
        else:
            self.posicion = 0
    
    def verificar_tipo(self, tipo_token):
        """Verifica si el token actual es del tipo especificado."""
        return self.token_actual.tipo == tipo_token
    
    def consumir(self, tipo_token, mensaje_error):
        """Consume un token si es del tipo esperado, de lo contrario lanza un error."""
        if self.verificar_tipo(tipo_token):
            token = self.token_actual
            self.avanzar()
            return token
        else:
            raise ErrorSintactico(f"{mensaje_error}. Se esperaba {tipo_token.name}, pero se encontró {self.token_actual.tipo.name}", self.token_actual)
    
    def analizar(self):
        """Comienza el análisis sintáctico y retorna el AST resultante."""
        # No usamos try-except aquí para permitir que el error se propague hacia arriba
        ast = self.programa()
        
        # Verificar que se hayan consumido todos los tokens excepto EOF
        if not self.verificar_tipo(TipoToken.EOF):
            raise ErrorSintactico(f"Tokens adicionales después del final del programa", self.token_actual)
        
        return ast
    
    # Implementación de las reglas gramaticales
    
    def programa(self):
        """
        <programa> ::= <sentencia>+
        """
        nodo = Nodo("Programa")
        
        # Debe haber al menos una sentencia
        if self.verificar_tipo(TipoToken.EOF):
            raise ErrorSintactico("El programa no puede estar vacío", self.token_actual)
        
        # Procesar todas las sentencias
        while not self.verificar_tipo(TipoToken.EOF):
            nodo.agregar_hijo(self.sentencia())
        
        # Retornar el nodo construido - IMPORTANTE: Esta línea estaba faltando
        return nodo

    def sentencia(self):
        """
        <sentencia> ::= <declaración> | <asignación> | <estructuras_de_control> | <expresión> | <kw_clg> | <sentencia_return>
        """
        # Verificar el tipo de sentencia
        if self.token_actual.tipo in [TipoToken.CONST, TipoToken.FINAL, TipoToken.ENT, TipoToken.FLT, TipoToken.LG, TipoToken.STR]:
            return self.declaracion()
        elif self.token_actual.tipo == TipoToken.IDENTIFICADOR:
            # Verificar si es una asignación o una expresión
            token_guardado = self.token_actual
            self.avanzar()
            if self.verificar_tipo(TipoToken.IGUAL):
                self.retroceder()  # Volver al identificador
                return self.asignacion()
            else:
                self.retroceder()  # Volver al identificador
                return self.expresion()
        elif self.token_actual.tipo in [TipoToken.IF, TipoToken.FOR, TipoToken.WHILE]:
            return self.estructuras_de_control()
        elif self.token_actual.tipo == TipoToken.CLG:
            return self.kw_clg()
        elif self.token_actual.tipo == TipoToken.FCT:
            # Añadir soporte para definición de funciones
            return self.definicion_funcion()
        # Añadir soporte para sentencias de retorno
        elif self.token_actual.tipo == TipoToken.RETURN:
            return self.sentencia_return()
        else:
            # Si no coincide con ninguna de las anteriores, asumimos que es una expresión
            return self.expresion()
    
    def declaracion(self):
        """
        <declaración> ::= <kw_unmutable>? <tipo> <id> ("=" (<kw_scn> | <expresión>))? ";"
        """
        nodo = Nodo("Declaración")
        
        # Verificar si hay un modificador de inmutabilidad
        if self.verificar_tipo(TipoToken.CONST) or self.verificar_tipo(TipoToken.FINAL):
            nodo.agregar_hijo(self.token_actual)
            self.avanzar()
        
        # Verificar el tipo de dato
        if not (self.verificar_tipo(TipoToken.ENT) or self.verificar_tipo(TipoToken.FLT) or 
                self.verificar_tipo(TipoToken.LG) or self.verificar_tipo(TipoToken.STR)):
            raise ErrorSintactico("Se esperaba un tipo de dato", self.token_actual)
        
        nodo.agregar_hijo(self.token_actual)  # Agregar el tipo
        self.avanzar()
        
        # Verificar el identificador
        if not self.verificar_tipo(TipoToken.IDENTIFICADOR):
            raise ErrorSintactico("Se esperaba un identificador", self.token_actual)
        
        nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
        self.avanzar()
        
        # Verificar si hay una asignación
        if self.verificar_tipo(TipoToken.IGUAL):
            nodo.agregar_hijo(self.token_actual)  # Agregar el operador =
            self.avanzar()
            
            # Verificar si es un scn() o una expresión
            if self.verificar_tipo(TipoToken.SCN):
                nodo.agregar_hijo(self.token_actual)  # Agregar scn()
                self.avanzar()
            else:
                nodo.agregar_hijo(self.expresion())  # Agregar la expresión
        
        # Verificar el punto y coma final
        self.consumir(TipoToken.PUNTO_COMA, "Falta punto y coma al final de la declaración")
        
        return nodo
    
    def asignacion(self):
        """
        <asignación> ::= <id> "=" <expresión> ";"
        """
        nodo = Nodo("Asignación")
        
        # Verificar el identificador
        if not self.verificar_tipo(TipoToken.IDENTIFICADOR):
            raise ErrorSintactico("Se esperaba un identificador", self.token_actual)
        
        nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
        self.avanzar()
        
        # Verificar el operador =
        self.consumir(TipoToken.IGUAL, "Se esperaba un operador de asignación")
        
        # Verificar la expresión - Aquí está el cambio importante, usamos operacion_aritmetica en lugar de expresion
        nodo.agregar_hijo(self.operacion_aritmetica())
        
        # Verificar el punto y coma final
        self.consumir(TipoToken.PUNTO_COMA, "Falta punto y coma al final de la asignación")
        
        return nodo
        
    def expresion(self):
        """
        <expresión> ::= (<operacion_aritmetica> | <llamada_funcion> | <id> | <numero_valores>) ";"
        """
        nodo = Nodo("Expresión")
        
        # Verificar el tipo de expresión
        if self.verificar_tipo(TipoToken.IDENTIFICADOR):
            # Verificar si es una llamada a función o un identificador
            token_guardado = self.token_actual
            self.avanzar()
            if self.verificar_tipo(TipoToken.PARENTESIS_IZQ):
                self.retroceder()  # Volver al identificador
                nodo.agregar_hijo(self.llamada_funcion())
            else:
                self.retroceder()  # Volver al identificador
                nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
                self.avanzar()
        elif self.verificar_tipo(TipoToken.NUMERO_ENTERO) or self.verificar_tipo(TipoToken.NUMERO_FLOTANTE):
            nodo.agregar_hijo(self.token_actual)  # Agregar el número
            self.avanzar()
        else:
            nodo.agregar_hijo(self.operacion_aritmetica())
        
        # Verificar si tenemos que consumir punto y coma (para expresiones seguidas de ;)
        if not (self.verificar_tipo(TipoToken.EOF) or self.verificar_tipo(TipoToken.LLAVE_DER) or 
                self.verificar_tipo(TipoToken.PARENTESIS_DER)):
            # Si esta expresión es parte de una sentencia return o asignación, etc.,
            # no consumimos el punto y coma aquí para evitar problemas
            pass
        
        return nodo
    
    def operacion_aritmetica(self):
        """
        <operacion_aritmetica> ::= <termino> (<operadores_aritmeticos_segundo_orden> <termino>)*
        """
        nodo = Nodo("OperaciónAritmética")
        
        # Procesar el primer término
        nodo.agregar_hijo(self.termino())
        
        # Procesar términos adicionales
        while (self.verificar_tipo(TipoToken.MAS) or self.verificar_tipo(TipoToken.MENOS)):
            nodo.agregar_hijo(self.token_actual)  # Agregar el operador
            self.avanzar()
            nodo.agregar_hijo(self.termino())
        
        return nodo
    
    def termino(self):
        """
        <termino> ::= <factor> (<operadores_aritmeticos_primer_orden> <factor>)*
        """
        nodo = Nodo("Término")
        
        # Procesar el primer factor
        nodo.agregar_hijo(self.factor())
        
        # Procesar factores adicionales
        while (self.verificar_tipo(TipoToken.MULTIPLICACION) or self.verificar_tipo(TipoToken.DIVISION)):
            nodo.agregar_hijo(self.token_actual)  # Agregar el operador
            self.avanzar()
            nodo.agregar_hijo(self.factor())
        
        return nodo
    
    def factor(self):
        """
        <factor> ::= <numero_valores> | <llamada_funcion> | <id> | "(" <operacion_aritmetica> ")"
        """
        nodo = Nodo("Factor")
        
        if self.verificar_tipo(TipoToken.NUMERO_ENTERO) or self.verificar_tipo(TipoToken.NUMERO_FLOTANTE):
            nodo.agregar_hijo(self.token_actual)  # Agregar el número
            self.avanzar()
        elif self.verificar_tipo(TipoToken.IDENTIFICADOR):
            # Verificar si es una llamada a función o un identificador
            token_guardado = self.token_actual
            self.avanzar()
            if self.verificar_tipo(TipoToken.PARENTESIS_IZQ):
                self.retroceder()  # Volver al identificador
                nodo.agregar_hijo(self.llamada_funcion())
            else:
                self.retroceder()  # Volver al identificador
                nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
                self.avanzar()
        elif self.verificar_tipo(TipoToken.PARENTESIS_IZQ):
            self.avanzar()  # Consumir el paréntesis izquierdo
            nodo.agregar_hijo(self.operacion_aritmetica())
            self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho")
        else:
            raise ErrorSintactico("Se esperaba un número, identificador, llamada a función o expresión entre paréntesis", self.token_actual)
        
        return nodo
    
    def llamada_funcion(self):
        """
        <llamada_función> ::= <id> "(" (<expresión> ("," <expresión>)*)? ")"
        """
        nodo = Nodo("LlamadaFunción")
        
        # Verificar el identificador
        if not self.verificar_tipo(TipoToken.IDENTIFICADOR):
            raise ErrorSintactico("Se esperaba un identificador de función", self.token_actual)
        
        nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
        self.avanzar()
        
        # Verificar el paréntesis izquierdo
        self.consumir(TipoToken.PARENTESIS_IZQ, "Se esperaba un paréntesis izquierdo después del identificador de función")
        
        # Verificar si hay argumentos
        if not self.verificar_tipo(TipoToken.PARENTESIS_DER):
            # Procesar el primer argumento
            nodo.agregar_hijo(self.expresion())
            
            # Procesar argumentos adicionales
            while self.verificar_tipo(TipoToken.COMA):
                self.avanzar()  # Consumir la coma
                nodo.agregar_hijo(self.expresion())
        
        # Verificar el paréntesis derecho
        self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho en la llamada a función")
        
        return nodo
    
    def estructuras_de_control(self):
        """
        <estructuras_de_control> ::= <estructura_if> | <ciclo_for> | <ciclo_while>
        """
        if self.verificar_tipo(TipoToken.IF):
            return self.estructura_if()
        elif self.verificar_tipo(TipoToken.FOR):
            return self.ciclo_for()
        elif self.verificar_tipo(TipoToken.WHILE):
            return self.ciclo_while()
        else:
            raise ErrorSintactico("Se esperaba una estructura de control (if, for o while)", self.token_actual)
    
    def estructura_if(self):
        """
        <estructura_if> ::= "if" "(" <expresión_lógica> ")" "{" <sentencia>+ "}" ("else" "{" <sentencia>+ "}")?
        """
        nodo = Nodo("EstructuraIf")
        
        # Verificar la palabra clave if
        self.consumir(TipoToken.IF, "Se esperaba la palabra clave 'if'")
        
        # Verificar el paréntesis izquierdo
        self.consumir(TipoToken.PARENTESIS_IZQ, "Se esperaba un paréntesis izquierdo después de 'if'")
        
        # Verificar la expresión lógica
        nodo.agregar_hijo(self.expresion_logica())
        
        # Verificar el paréntesis derecho
        self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho en la condición del if")
        
        # Verificar la llave izquierda
        self.consumir(TipoToken.LLAVE_IZQ, "Se esperaba una llave izquierda para el bloque del if")
        
        # Procesar las sentencias del bloque if
        bloque_if = Nodo("BloqueIf")
        while not self.verificar_tipo(TipoToken.LLAVE_DER):
            if self.verificar_tipo(TipoToken.EOF):
                raise ErrorSintactico("Fin inesperado del archivo. Falta llave derecha para cerrar el bloque del if", self.token_actual)
            bloque_if.agregar_hijo(self.sentencia())
        
        nodo.agregar_hijo(bloque_if)
        
        # Verificar la llave derecha
        self.consumir(TipoToken.LLAVE_DER, "Falta llave derecha para cerrar el bloque del if")
        
        # Verificar si hay un bloque else
        if self.verificar_tipo(TipoToken.ELSE):
            self.avanzar()  # Consumir else
            
            # Verificar la llave izquierda
            self.consumir(TipoToken.LLAVE_IZQ, "Se esperaba una llave izquierda para el bloque del else")
            
            # Procesar las sentencias del bloque else
            bloque_else = Nodo("BloqueElse")
            while not self.verificar_tipo(TipoToken.LLAVE_DER):
                if self.verificar_tipo(TipoToken.EOF):
                    raise ErrorSintactico("Fin inesperado del archivo. Falta llave derecha para cerrar el bloque del else", self.token_actual)
                bloque_else.agregar_hijo(self.sentencia())
            
            nodo.agregar_hijo(bloque_else)
            
            # Verificar la llave derecha
            self.consumir(TipoToken.LLAVE_DER, "Falta llave derecha para cerrar el bloque del else")
        
        return nodo
    
    def expresion_logica(self):
        """
        <expresión_lógica> ::= <expresión> <operadores_comparación> <expresión>
        """
        nodo = Nodo("ExpresiónLógica")
        
        # Procesar la primera expresión
        nodo.agregar_hijo(self.expresion())
        
        # Verificar el operador de comparación
        if not (self.verificar_tipo(TipoToken.MENOR) or self.verificar_tipo(TipoToken.MAYOR) or
                self.verificar_tipo(TipoToken.IGUAL_IGUAL) or self.verificar_tipo(TipoToken.MENOR_IGUAL) or
                self.verificar_tipo(TipoToken.MAYOR_IGUAL) or self.verificar_tipo(TipoToken.DIFERENTE)):
            raise ErrorSintactico("Se esperaba un operador de comparación", self.token_actual)
        
        nodo.agregar_hijo(self.token_actual)  # Agregar el operador
        self.avanzar()
        
        # Procesar la segunda expresión
        nodo.agregar_hijo(self.expresion())
        
        return nodo
    
    def ciclo_for(self):
        """
        <ciclo_for> ::= "for" "(" (<declaración> | <asignación>) ";" <expresión_lógica> ";" <asignación> ")" "{" <sentencia>+ "}"
        """
        nodo = Nodo("CicloFor")
        
        # Verificar la palabra clave for
        self.consumir(TipoToken.FOR, "Se esperaba la palabra clave 'for'")
        
        # Verificar el paréntesis izquierdo
        self.consumir(TipoToken.PARENTESIS_IZQ, "Se esperaba un paréntesis izquierdo después de 'for'")
        
        # Verificar la inicialización (declaración o asignación)
        if self.token_actual.tipo in [TipoToken.CONST, TipoToken.FINAL, TipoToken.ENT, TipoToken.FLT, TipoToken.LG, TipoToken.STR]:
            nodo.agregar_hijo(self.declaracion())
        else:
            nodo.agregar_hijo(self.asignacion())
        
        # No verificamos el punto y coma aquí porque ya lo hacen las funciones declaracion y asignacion
        
        # Verificar la condición (expresión lógica)
        nodo.agregar_hijo(self.expresion_logica())
        
        # Verificar el punto y coma
        self.consumir(TipoToken.PUNTO_COMA, "Falta punto y coma después de la condición del for")
        
        # Verificar la actualización (asignación)
        nodo.agregar_hijo(self.asignacion())
        
        # Verificar el paréntesis derecho
        self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho en la definición del for")
        
        # Verificar la llave izquierda
        self.consumir(TipoToken.LLAVE_IZQ, "Se esperaba una llave izquierda para el bloque del for")
        
        # Procesar las sentencias del bloque for
        bloque_for = Nodo("BloqueFor")
        while not self.verificar_tipo(TipoToken.LLAVE_DER):
            if self.verificar_tipo(TipoToken.EOF):
                raise ErrorSintactico("Fin inesperado del archivo. Falta llave derecha para cerrar el bloque del for", self.token_actual)
            bloque_for.agregar_hijo(self.sentencia())
        
        nodo.agregar_hijo(bloque_for)
        
        # Verificar la llave derecha
        self.consumir(TipoToken.LLAVE_DER, "Falta llave derecha para cerrar el bloque del for")
        
        return nodo
    
    def ciclo_while(self):
        """
        <ciclo_while> ::= "while" "(" <expresión_lógica> ")" "{" <sentencia>+ "}"
        """
        nodo = Nodo("CicloWhile")
        
        # Verificar la palabra clave while
        self.consumir(TipoToken.WHILE, "Se esperaba la palabra clave 'while'")
        
        # Verificar el paréntesis izquierdo
        self.consumir(TipoToken.PARENTESIS_IZQ, "Se esperaba un paréntesis izquierdo después de 'while'")
        
        # Verificar la expresión lógica
        nodo.agregar_hijo(self.expresion_logica())
        
        # Verificar el paréntesis derecho
        self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho en la condición del while")
        
        # Verificar la llave izquierda
        self.consumir(TipoToken.LLAVE_IZQ, "Se esperaba una llave izquierda para el bloque del while")
        
        # Procesar las sentencias del bloque while
        bloque_while = Nodo("BloqueWhile")
        while not self.verificar_tipo(TipoToken.LLAVE_DER):
            if self.verificar_tipo(TipoToken.EOF):
                raise ErrorSintactico("Fin inesperado del archivo. Falta llave derecha para cerrar el bloque del while", self.token_actual)
            bloque_while.agregar_hijo(self.sentencia())
        
        nodo.agregar_hijo(bloque_while)
        
        # Verificar la llave derecha
        self.consumir(TipoToken.LLAVE_DER, "Falta llave derecha para cerrar el bloque del while")
        
        return nodo
    
    def kw_clg(self):
        """
        <kw_clg> ::= "clg(" (<id> | <string_literal>) ")"
        """
        nodo = Nodo("Impresión")
        
        # Verificar la palabra clave clg
        self.consumir(TipoToken.CLG, "Se esperaba la palabra clave 'clg'")
        
        # Verificar el paréntesis izquierdo
        self.consumir(TipoToken.PARENTESIS_IZQ, "Se esperaba un paréntesis izquierdo después de 'clg'")
        
        # Verificar el argumento (identificador o cadena)
        if self.verificar_tipo(TipoToken.IDENTIFICADOR):
            nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
            self.avanzar()
        elif self.verificar_tipo(TipoToken.CADENA):
            nodo.agregar_hijo(self.token_actual)  # Agregar la cadena
            self.avanzar()
        else:
            raise ErrorSintactico("Se esperaba un identificador o una cadena como argumento de clg", self.token_actual)
        
        # Verificar el paréntesis derecho
        self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho en la llamada a clg")
        
        # Verificar el punto y coma
        self.consumir(TipoToken.PUNTO_COMA, "Falta punto y coma al final de la llamada a clg")
        
        return nodo
    
    def parametros(self):
        """
        <parámetros> ::= <tipo> <id> ("," <tipo> <id>)*
        """
        nodo = Nodo("Parámetros")
        
        # Procesar el primer parámetro
        if not (self.verificar_tipo(TipoToken.ENT) or self.verificar_tipo(TipoToken.FLT) or 
                self.verificar_tipo(TipoToken.LG) or self.verificar_tipo(TipoToken.STR)):
            raise ErrorSintactico("Se esperaba un tipo de dato para el parámetro", self.token_actual)
        
        tipo = self.token_actual  # Guardar el tipo
        self.avanzar()
        
        # Verificar el identificador
        if not self.verificar_tipo(TipoToken.IDENTIFICADOR):
            raise ErrorSintactico("Se esperaba un identificador después del tipo de parámetro", self.token_actual)
        
        # Crear un nodo para el parámetro
        parametro = Nodo("Parámetro")
        parametro.agregar_hijo(tipo)  # Agregar el tipo
        parametro.agregar_hijo(self.token_actual)  # Agregar el identificador
        nodo.agregar_hijo(parametro)
        
        self.avanzar()
        
        # Procesar parámetros adicionales
        while self.verificar_tipo(TipoToken.COMA):
            self.avanzar()  # Consumir la coma
            
            # Verificar el tipo
            if not (self.verificar_tipo(TipoToken.ENT) or self.verificar_tipo(TipoToken.FLT) or 
                    self.verificar_tipo(TipoToken.LG) or self.verificar_tipo(TipoToken.STR)):
                raise ErrorSintactico("Se esperaba un tipo de dato para el parámetro", self.token_actual)
            
            tipo = self.token_actual  # Guardar el tipo
            self.avanzar()
            
            # Verificar el identificador
            if not self.verificar_tipo(TipoToken.IDENTIFICADOR):
                raise ErrorSintactico("Se esperaba un identificador después del tipo de parámetro", self.token_actual)
            
            # Crear un nodo para el parámetro
            parametro = Nodo("Parámetro")
            parametro.agregar_hijo(tipo)  # Agregar el tipo
            parametro.agregar_hijo(self.token_actual)  # Agregar el identificador
            nodo.agregar_hijo(parametro)
            
            self.avanzar()
        
        return nodo
    
    def definicion_funcion(self):
        """
        <función_con_retorno> ::= "fct" <id> "(" <parametros>? ")" ":" <tipo> "{" <sentencia>+ "}"
        <función_sin_retorno> ::= "fct" <id> "(" <parametros>? ")" "{" <sentencia>+ "}"
        """
        nodo = Nodo("DefiniciónFunción")
        
        # Verificar la palabra clave fct
        self.consumir(TipoToken.FCT, "Se esperaba la palabra clave 'fct'")
        
        # Verificar el identificador
        if not self.verificar_tipo(TipoToken.IDENTIFICADOR):
            raise ErrorSintactico("Se esperaba un identificador después de 'fct'", self.token_actual)
        
        nodo.agregar_hijo(self.token_actual)  # Agregar el identificador
        self.avanzar()
        
        # Verificar el paréntesis izquierdo
        self.consumir(TipoToken.PARENTESIS_IZQ, "Se esperaba un paréntesis izquierdo después del nombre de la función")
        
        # Verificar si hay parámetros
        if not self.verificar_tipo(TipoToken.PARENTESIS_DER):
            nodo.agregar_hijo(self.parametros())
        
        # Verificar el paréntesis derecho
        self.consumir(TipoToken.PARENTESIS_DER, "Falta paréntesis derecho en la definición de la función")
        
        # Verificar si tiene tipo de retorno
        con_retorno = False
        if self.verificar_tipo(TipoToken.DOS_PUNTOS):
            con_retorno = True
            self.avanzar()  # Consumir :
            
            # Verificar el tipo de retorno
            if not (self.verificar_tipo(TipoToken.ENT) or self.verificar_tipo(TipoToken.FLT) or 
                    self.verificar_tipo(TipoToken.LG) or self.verificar_tipo(TipoToken.STR)):
                raise ErrorSintactico("Se esperaba un tipo de retorno válido", self.token_actual)
            
            nodo.agregar_hijo(self.token_actual)  # Agregar el tipo de retorno
            self.avanzar()
        
        # Marcar el tipo de función
        if con_retorno:
            nodo.tipo = "FunciónConRetorno"
        else:
            nodo.tipo = "FunciónSinRetorno"
            
        # Verificar la llave izquierda
        self.consumir(TipoToken.LLAVE_IZQ, "Se esperaba una llave izquierda para el bloque de la función")
        
        # Procesar las sentencias del cuerpo de la función
        cuerpo_funcion = Nodo("CuerpoFunción")
        while not self.verificar_tipo(TipoToken.LLAVE_DER):
            if self.verificar_tipo(TipoToken.EOF):
                raise ErrorSintactico("Fin inesperado del archivo. Falta llave derecha para cerrar el bloque de la función", self.token_actual)
            cuerpo_funcion.agregar_hijo(self.sentencia())
        
        nodo.agregar_hijo(cuerpo_funcion)
        
        # Verificar la llave derecha
        self.consumir(TipoToken.LLAVE_DER, "Falta llave derecha para cerrar el bloque de la función")
        
        return nodo
    
    def sentencia_return(self):
        """
        <sentencia_return> ::= "return" <expresión>? ";"
        """
        nodo = Nodo("SentenciaReturn")
        
        # Verificar la palabra clave return
        self.consumir(TipoToken.RETURN, "Se esperaba la palabra clave 'return'")
        
        # Verificar si hay una expresión de retorno
        if not self.verificar_tipo(TipoToken.PUNTO_COMA):
            # Procesamos la operación aritmética completa
            nodo.agregar_hijo(self.operacion_aritmetica())
        
        # Verificar el punto y coma final
        self.consumir(TipoToken.PUNTO_COMA, "Falta punto y coma al final de la sentencia return")
        
        return nodo
    
class ErrorSintactico(Exception):
    """Excepción para errores sintácticos durante el análisis."""
    def __init__(self, mensaje, token=None):
        self.mensaje = mensaje
        self.token = token
        if token:
            super().__init__(f"{mensaje} en línea {token.linea}, columna {token.columna}, token: {token.lexema}")
        else:
            super().__init__(mensaje)
            
    def __str__(self):
        if self.token:
            return f"{self.mensaje} en línea {self.token.linea}, columna {self.token.columna}, token: {self.token.lexema}"
        else:
            return self.mensaje
        
def probar_analizador_sintactico(codigo_fuente):
    """Función para probar el analizador sintáctico con mejor manejo de errores."""
    print("=== ANÁLISIS LÉXICO ===")
    try:
        analizador_lexico = AnalizadorLexico(codigo_fuente)
        tokens = analizador_lexico.analizar()
        
        # Imprimir tokens para depuración
        for token in tokens:
            print(token)
        
        print("\n=== ANÁLISIS SINTÁCTICO ===")
        analizador_sintactico = AnalizadorSintactico(tokens)
        
        # Ahora dejamos que los errores se propaguen para capturarlos aquí
        try:
            ast = analizador_sintactico.analizar()
            print("Análisis sintáctico completado con éxito.")
            print("\n=== ÁRBOL SINTÁCTICO ===")
            ast.imprimir()
        except ErrorSintactico as e:
            print(f"Error sintáctico: {e}")
            # Mostrar información más detallada sobre el error
            if hasattr(e, 'token') and e.token:
                print(f"Error en línea {e.token.linea}, columna {e.token.columna}")
                print(f"Token problemático: '{e.token.lexema}' (tipo: {e.token.tipo.name})")
                
                # Mostrar el contexto del error
                lineas = codigo_fuente.split('\n')
                if 0 <= e.token.linea - 1 < len(lineas):
                    print("\nContexto del error:")
                    linea_error = lineas[e.token.linea - 1]
                    print(f"Línea {e.token.linea}: {linea_error}")
                    # Marcar la posición del error
                    print(" " * (e.token.columna + 7) + "^")
        except Exception as e:
            print(f"Error inesperado: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
    except Exception as e:
        print(f"Error durante el análisis léxico: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Ejemplo de código fuente para probar
    codigo = '''
    ent x = 10;
    fct suma(ent a, ent b) : ent {
        return a + b;
    }

    x = x + 1;

    while (x < 10) {
        x = x + 1;

        if (x == 10) {
            clg("ultimo");
        }
    }

    suma(x, y)
    '''
    
    probar_analizador_sintactico(codigo)
    
    