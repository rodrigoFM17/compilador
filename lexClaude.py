#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, auto
import re

class TipoToken(Enum):
    # Palabras clave
    CONST = auto()
    FINAL = auto()
    ENT = auto()
    FLT = auto()
    LG = auto()
    STR = auto()
    SCN = auto()
    CLG = auto()
    FCT = auto()
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    RETURN = auto()
    
    # Identificadores y literales
    IDENTIFICADOR = auto()
    NUMERO_ENTERO = auto()
    NUMERO_FLOTANTE = auto()
    CADENA = auto()
    
    # Operadores y símbolos
    IGUAL = auto()
    MAS = auto()
    MENOS = auto()
    MULTIPLICACION = auto()
    DIVISION = auto()
    MENOR = auto()
    MAYOR = auto()
    MENOR_IGUAL = auto()
    MAYOR_IGUAL = auto()
    IGUAL_IGUAL = auto()
    DIFERENTE = auto()
    
    # Puntuación
    PARENTESIS_IZQ = auto()
    PARENTESIS_DER = auto()
    LLAVE_IZQ = auto()
    LLAVE_DER = auto()
    PUNTO_COMA = auto()
    COMA = auto()
    DOS_PUNTOS = auto()
    DOLAR = auto()
    
    # Fin del archivo
    EOF = auto()
    
    # Token desconocido
    ERROR = auto()

class Token:
    """Clase que representa un token con su tipo, lexema, línea y columna."""
    
    def __init__(self, tipo, lexema, linea, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
    
    def __str__(self):
        return f"Token({self.tipo.name}, '{self.lexema}', linea={self.linea}, columna={self.columna})"

class AnalizadorLexico:
    """Analizador léxico para el lenguaje definido por la gramática."""
    
    def __init__(self, codigo_fuente):
        self.codigo_fuente = codigo_fuente
        self.posicion = 0
        self.linea = 1
        self.columna = 1
        self.tokens = []
        
        # Diccionario de palabras reservadas
        self.palabras_reservadas = {
            'const': TipoToken.CONST,
            'final': TipoToken.FINAL,
            'ent': TipoToken.ENT,
            'flt': TipoToken.FLT,
            'lg': TipoToken.LG,
            'str': TipoToken.STR,
            'scn': TipoToken.SCN,
            'clg': TipoToken.CLG,
            'fct': TipoToken.FCT,
            'if': TipoToken.IF,
            'else': TipoToken.ELSE,
            'for': TipoToken.FOR,
            'while': TipoToken.WHILE,
            'return': TipoToken.RETURN
        }
    
    def caracter_actual(self):
        """Retorna el carácter actual o None si está al final del código fuente."""
        if self.posicion >= len(self.codigo_fuente):
            return None
        return self.codigo_fuente[self.posicion]
    
    def caracter_siguiente(self):
        """Retorna el carácter siguiente o None si está al final del código fuente."""
        if self.posicion + 1 >= len(self.codigo_fuente):
            return None
        return self.codigo_fuente[self.posicion + 1]
    
    def avanzar(self):
        """Avanza al siguiente carácter y actualiza la columna."""
        self.posicion += 1
        self.columna += 1
        return self.caracter_actual()
    
    def retroceder(self):
        """Retrocede un carácter y actualiza la columna."""
        self.posicion -= 1
        self.columna -= 1
    
    def es_letra(self, c):
        """Verifica si un carácter es una letra."""
        return c is not None and c.isalpha()
    
    def es_digito(self, c):
        """Verifica si un carácter es un dígito."""
        return c is not None and c.isdigit()
    
    def es_alfanumerico(self, c):
        """Verifica si un carácter es alfanumérico."""
        return c is not None and (c.isalnum() or c == '_')
    
    def saltar_espacios_y_comentarios(self):
        """Salta espacios en blanco y comentarios."""
        while self.caracter_actual() is not None:
            # Saltar espacios en blanco
            if self.caracter_actual() in [' ', '\t']:
                self.avanzar()
            # Saltar saltos de línea
            elif self.caracter_actual() == '\n':
                self.linea += 1
                self.columna = 1
                self.avanzar()
            # Saltar retorno de carro
            elif self.caracter_actual() == '\r':
                self.avanzar()
            # Saltar comentarios de una línea (// ...)
            elif self.caracter_actual() == '/' and self.caracter_siguiente() == '/':
                while self.caracter_actual() is not None and self.caracter_actual() != '\n':
                    self.avanzar()
            # Saltar comentarios multilínea (/* ... */)
            elif self.caracter_actual() == '/' and self.caracter_siguiente() == '*':
                self.avanzar()  # Saltar /
                self.avanzar()  # Saltar *
                
                comentario_cerrado = False
                
                while self.caracter_actual() is not None and not comentario_cerrado:
                    if self.caracter_actual() == '*' and self.caracter_siguiente() == '/':
                        self.avanzar()  # Saltar *
                        self.avanzar()  # Saltar /
                        comentario_cerrado = True
                    else:
                        if self.caracter_actual() == '\n':
                            self.linea += 1
                            self.columna = 1
                        self.avanzar()
                
                if not comentario_cerrado:
                    print("Advertencia: Comentario multilínea no cerrado")
            else:
                break
    
    def analizar_identificador(self):
        """Analiza un identificador o palabra reservada."""
        inicio = self.posicion
        columna_inicio = self.columna
        
        # Primer carácter debe ser una letra
        if not self.es_letra(self.caracter_actual()):
            return None
        
        self.avanzar()
        
        # Caracteres posteriores pueden ser letras o dígitos
        while self.caracter_actual() is not None and self.es_alfanumerico(self.caracter_actual()):
            self.avanzar()
        
        lexema = self.codigo_fuente[inicio:self.posicion]
        
        # Verificar si es una palabra reservada
        if lexema in self.palabras_reservadas:
            return Token(self.palabras_reservadas[lexema], lexema, self.linea, columna_inicio)
        
        # Si no es una palabra reservada, es un identificador
        return Token(TipoToken.IDENTIFICADOR, lexema, self.linea, columna_inicio)
    
    def analizar_numero(self):
        """Analiza un número (entero o flotante)."""
        inicio = self.posicion
        columna_inicio = self.columna
        es_flotante = False
        
        # Debe empezar con un dígito
        if not self.es_digito(self.caracter_actual()):
            return None
        
        # Leer la parte entera
        while self.caracter_actual() is not None and self.es_digito(self.caracter_actual()):
            self.avanzar()
        
        # Verificar si tiene punto decimal
        if self.caracter_actual() == '.' and self.caracter_siguiente() is not None and self.es_digito(self.caracter_siguiente()):
            es_flotante = True
            self.avanzar()  # Saltar el punto
            
            # Leer la parte decimal
            while self.caracter_actual() is not None and self.es_digito(self.caracter_actual()):
                self.avanzar()
        
        lexema = self.codigo_fuente[inicio:self.posicion]
        
        if es_flotante:
            return Token(TipoToken.NUMERO_FLOTANTE, lexema, self.linea, columna_inicio)
        else:
            return Token(TipoToken.NUMERO_ENTERO, lexema, self.linea, columna_inicio)
    
    def analizar_cadena(self):
        """Analiza una cadena de texto entre comillas dobles."""
        if self.caracter_actual() != '"':
            return None
        
        inicio = self.posicion
        columna_inicio = self.columna
        
        self.avanzar()  # Saltar la comilla de apertura
        
        while self.caracter_actual() is not None and self.caracter_actual() != '"':
            # Manejo de escape de caracteres
            if self.caracter_actual() == '\\' and self.caracter_siguiente() is not None:
                self.avanzar()  # Saltar la barra invertida
            
            # Actualizar contador de líneas si hay salto de línea en la cadena
            if self.caracter_actual() == '\n':
                self.linea += 1
                self.columna = 1
            
            self.avanzar()
        
        if self.caracter_actual() is None:
            return Token(TipoToken.ERROR, "Cadena no cerrada", self.linea, columna_inicio)
        
        self.avanzar()  # Saltar la comilla de cierre
        
        lexema = self.codigo_fuente[inicio:self.posicion]
        return Token(TipoToken.CADENA, lexema, self.linea, columna_inicio)
    
    def analizar(self):
        """Analiza el código fuente y retorna una lista de tokens."""
        while self.posicion < len(self.codigo_fuente):
            # Saltar espacios en blanco y comentarios
            self.saltar_espacios_y_comentarios()
            
            # Verificar si hemos llegado al final del código
            if self.caracter_actual() is None:
                break
            
            token = None
            caracter_actual = self.caracter_actual()
            columna_actual = self.columna
            
            # Intentar reconocer el token
            if self.es_letra(caracter_actual):
                token = self.analizar_identificador()
            elif self.es_digito(caracter_actual):
                token = self.analizar_numero()
            elif caracter_actual == '"':
                token = self.analizar_cadena()
            else:
                # Analizar operadores y símbolos
                if caracter_actual == '=':
                    if self.caracter_siguiente() == '=':
                        self.avanzar()  # Saltar el primer '='
                        self.avanzar()  # Saltar el segundo '='
                        token = Token(TipoToken.IGUAL_IGUAL, "==", self.linea, columna_actual)
                    else:
                        self.avanzar()
                        token = Token(TipoToken.IGUAL, "=", self.linea, columna_actual)
                elif caracter_actual == '+':
                    self.avanzar()
                    token = Token(TipoToken.MAS, "+", self.linea, columna_actual)
                elif caracter_actual == '-':
                    self.avanzar()
                    token = Token(TipoToken.MENOS, "-", self.linea, columna_actual)
                elif caracter_actual == '*':
                    self.avanzar()
                    token = Token(TipoToken.MULTIPLICACION, "*", self.linea, columna_actual)
                elif caracter_actual == '/':
                    self.avanzar()
                    token = Token(TipoToken.DIVISION, "/", self.linea, columna_actual)
                elif caracter_actual == '<':
                    if self.caracter_siguiente() == '=':
                        self.avanzar()  # Saltar '<'
                        self.avanzar()  # Saltar '='
                        token = Token(TipoToken.MENOR_IGUAL, "<=", self.linea, columna_actual)
                    else:
                        self.avanzar()
                        token = Token(TipoToken.MENOR, "<", self.linea, columna_actual)
                elif caracter_actual == '>':
                    if self.caracter_siguiente() == '=':
                        self.avanzar()  # Saltar '>'
                        self.avanzar()  # Saltar '='
                        token = Token(TipoToken.MAYOR_IGUAL, ">=", self.linea, columna_actual)
                    else:
                        self.avanzar()
                        token = Token(TipoToken.MAYOR, ">", self.linea, columna_actual)
                elif caracter_actual == '!':
                    if self.caracter_siguiente() == '=':
                        self.avanzar()  # Saltar '!'
                        self.avanzar()  # Saltar '='
                        token = Token(TipoToken.DIFERENTE, "!=", self.linea, columna_actual)
                    else:
                        self.avanzar()
                        token = Token(TipoToken.ERROR, "! sin =", self.linea, columna_actual)
                elif caracter_actual == '(':
                    self.avanzar()
                    token = Token(TipoToken.PARENTESIS_IZQ, "(", self.linea, columna_actual)
                elif caracter_actual == ')':
                    self.avanzar()
                    token = Token(TipoToken.PARENTESIS_DER, ")", self.linea, columna_actual)
                elif caracter_actual == '{':
                    self.avanzar()
                    token = Token(TipoToken.LLAVE_IZQ, "{", self.linea, columna_actual)
                elif caracter_actual == '}':
                    self.avanzar()
                    token = Token(TipoToken.LLAVE_DER, "}", self.linea, columna_actual)
                elif caracter_actual == ';':
                    self.avanzar()
                    token = Token(TipoToken.PUNTO_COMA, ";", self.linea, columna_actual)
                elif caracter_actual == ',':
                    self.avanzar()
                    token = Token(TipoToken.COMA, ",", self.linea, columna_actual)
                elif caracter_actual == ':':
                    self.avanzar()
                    token = Token(TipoToken.DOS_PUNTOS, ":", self.linea, columna_actual)
                elif caracter_actual == '$':
                    self.avanzar()
                    token = Token(TipoToken.DOLAR, "$", self.linea, columna_actual)
                else:
                    self.avanzar()
                    token = Token(TipoToken.ERROR, caracter_actual, self.linea, columna_actual)
            
            if token is not None:
                self.tokens.append(token)
        
        # Agregar token de fin de archivo
        self.tokens.append(Token(TipoToken.EOF, "", self.linea, self.columna))
        
        return self.tokens


def probar_analizador_lexico(codigo_fuente):
    """Función para probar el analizador léxico."""
    analizador = AnalizadorLexico(codigo_fuente)
    tokens = analizador.analizar()
    
    for token in tokens:
        print(token)
    
    return tokens


if __name__ == '__main__':
    # Ejemplo de código fuente para probar
    codigo = '''
    ent x = 10;
    flt y = 20.5;
    if (x < y) {
        clg("x es menor que $y");
    } else {
        clg("x es mayor o igual que $y");
    }
    
    fct suma(ent a, ent b) : ent {
        ent resultado = a + b;
        return resultado;
    }
    '''
    
    probar_analizador_lexico(codigo)