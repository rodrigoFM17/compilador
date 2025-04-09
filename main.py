import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from MiLenguajeLexer import MiLenguajeLexer
from MiLenguajeParser import MiLenguajeParser
from semantic_analyzer import SemanticAnalyzer
from symbol_table import SemanticError

class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Error sintáctico en línea {line}, columna {column}: {msg}"
        self.errors.append(error_message)
    
    def get_errors(self):
        return self.errors

def compile_code(input_file):
    # Leer archivo de entrada
    input_stream = FileStream(input_file, encoding='utf-8')
    
    # Crear lexer
    lexer = MiLenguajeLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_error_listener = MiErrorListener()
    lexer.addErrorListener(lexer_error_listener)
    
    # Verificar errores léxicos
    lexer_errors = lexer_error_listener.get_errors()
    if lexer_errors:
        print("Errores léxicos encontrados:")
        for error in lexer_errors:
            print(f"  {error}")
        return False
    
    # Crear stream de tokens
    token_stream = CommonTokenStream(lexer)
    
    # Crear parser
    parser = MiLenguajeParser(token_stream)
    parser.removeErrorListeners()
    parser_error_listener = MiErrorListener()
    parser.addErrorListener(parser_error_listener)
    
    # Ejecutar parser
    tree = parser.programa()
    
    # Verificar errores sintácticos
    parser_errors = parser_error_listener.get_errors()
    if parser_errors:
        print("Errores sintácticos encontrados:")
        for error in parser_errors:
            print(f"  {error}")
        return False
    
    # Ejecutar análisis semántico
    analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(analyzer, tree)
    
    # Verificar errores semánticos
    semantic_errors = analyzer.get_errors()
    if semantic_errors:
        print("Errores semánticos encontrados:")
        for error in semantic_errors:
            print(f"  {error}")
        return False
    
    print("Compilación exitosa. No se encontraron errores.")
    print("\nInformación de la tabla de símbolos:")
    print("{:<15} {:<10} {:<10} {:<15}".format("NOMBRE", "TIPO", "CONSTANTE", "VALOR"))
    print("-" * 50)
    for name, symbol in analyzer.symbol_table.get_all_symbols().items():
        is_const = "Sí" if symbol.is_constant else "No"
        value = str(symbol.value) if symbol.value is not None else "None"
        print("{:<15} {:<10} {:<10} {:<15}".format(name, symbol.type, is_const, value))
    
    return True

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.txt")
        return
    
    try:
        compile_code(sys.argv[1])
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()