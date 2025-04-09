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
        error_context = f"Contexto: '{offendingSymbol.text if offendingSymbol else 'EOF'}'"
        self.errors.append(error_message)
        self.errors.append(error_context)
    
    def get_errors(self):
        return self.errors

def show_token_stream(lexer):
    """Muestra todos los tokens generados por el lexer (función de depuración)"""
    print("\n=== TABLA DE TOKENS ===")
    print("TOKEN_TYPE".ljust(20) + "TEXT".ljust(30) + "LINE:COL")
    print("-" * 70)
    
    # Crear un diccionario inverso de nombres de tokens
    token_names = {}
    for i, name in enumerate(lexer.ruleNames):
        token_names[i + 1] = name  # Los tokens comienzan en 1
    
    # Añadir nombres de tokens especiales
    token_names[Token.EOF] = 'EOF'
    
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        # Obtener el nombre del token o usar el tipo como cadena si no está disponible
        token_name = token_names.get(token.type, str(token.type))
        print(f"{token_name}".ljust(20) + f"'{token.text}'".ljust(30) + f"{token.line}:{token.column}")
        token = lexer.nextToken()
    
    # Mostrar el token EOF al final
    print(f"EOF".ljust(20) + "'<EOF>'".ljust(30) + "N/A")
    print("-" * 70)
    lexer.reset()

def print_tree(tree, parser, indent=0):
    """Imprime el árbol sintáctico de forma recursiva"""
    if not tree:
        return
    
    # Si es nodo terminal (token)
    if isinstance(tree, TerminalNode):
        token_text = tree.getText()
        if token_text:
            print("  " * indent + f"└─ {token_text}")
    else:
        # Es un nodo no terminal (regla)
        try:
            rule_name = parser.ruleNames[tree.getRuleIndex()] if tree.getRuleIndex() >= 0 else "?"
            print("  " * indent + f"└─ {rule_name}")
        except IndexError:
            print("  " * indent + f"└─ [Regla desconocida]")
        
        # Recorrer los hijos
        for i in range(tree.getChildCount()):
            print_tree(tree.getChild(i), parser, indent + 1)

def compile_code(input_file, debug=False):
    # Leer archivo de entrada
    try:
        print(f"Leyendo archivo: {input_file}")
        input_stream = FileStream(input_file, encoding='utf-8')
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return False
    
    # Crear lexer
    lexer = MiLenguajeLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_error_listener = MiErrorListener()
    lexer.addErrorListener(lexer_error_listener)
    
    # Mostrar tokens si estamos en modo debug
    if debug:
        try:
            show_token_stream(lexer)
        except Exception as e:
            print(f"Error al mostrar tokens: {e}")
            import traceback
            traceback.print_exc()
    
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
    try:
        print("Analizando sintaxis...")
        tree = parser.programa()
        
        # Mostrar árbol sintáctico si estamos en modo debug
        if debug:
            try:
                print("\n=== ÁRBOL SINTÁCTICO ===")
                print_tree(tree, parser)
                print("=" * 60)
            except Exception as e:
                print(f"Error al mostrar árbol sintáctico: {e}")
                import traceback
                traceback.print_exc()
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {e}")
        return False
    
    # Verificar errores sintácticos
    parser_errors = parser_error_listener.get_errors()
    if parser_errors:
        print("Errores sintácticos encontrados:")
        for error in parser_errors:
            print(f"  {error}")
        return False
    
    # Ejecutar análisis semántico
    print("Realizando análisis semántico...")
    analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    
    try:
        walker.walk(analyzer, tree)
    except Exception as e:
        print(f"Error durante el análisis semántico: {e}")
        return False
    
    # Verificar errores semánticos
    semantic_errors = analyzer.get_errors()
    if semantic_errors:
        print("Errores semánticos encontrados:")
        for error in semantic_errors:
            print(f"  {error}")
        return False
    
    print("Compilación exitosa. No se encontraron errores.")
    print("\n=== TABLA DE SÍMBOLOS ===")
    print("ÁMBITO".ljust(15) + "NOMBRE".ljust(15) + "TIPO".ljust(10) + "CONSTANTE".ljust(10) + "VALOR")
    print("-" * 70)
    for scope_name, name, symbol in analyzer.symbol_table.get_all_symbols_with_scopes():
        const_str = "Sí" if symbol.is_constant else "No"
        value_str = str(symbol.value) if symbol.value is not None else "N/A"
        print(f"{scope_name}".ljust(15) + f"{name}".ljust(15) + f"{symbol.type}".ljust(10) + f"{const_str}".ljust(10) + f"{value_str}")
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.txt [--debug]")
        return
    
    debug_mode = "--debug" in sys.argv
    
    input_file = None
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            input_file = arg
            break
    
    if not input_file:
        print("Debe especificar un archivo de entrada.")
        return
    
    try:
        compile_code(input_file, debug_mode)
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()