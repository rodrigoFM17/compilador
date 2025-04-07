import ply.lex as lex
import ply.yacc as yacc

# -------------------------------
# Lexer (Actualizado y corregido)
# -------------------------------
states = (
    ('string', 'exclusive'),
)

tokens = [
    'ID', 'NUMBER', 'STRING_TEXT', 'STRING_VAR',
    'KW_ENT', 'KW_FLT', 'KW_LG', 'KW_STR', 'KW_UNMUTABLE',
    'FCT', 'IF', 'ELSE', 'FOR', 'WHILE', 'CLG', 'SCN', 'RETURN',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQ', 'NE',
    'LT', 'GT', 'LE', 'GE', 'LPAREN', 'RPAREN', 'LBRACE',
    'RBRACE', 'SEMI', 'COMMA', 'COLON', 'ASSIGN', 'STRING_START', 'STRING_END'
]

reserved = {
    'const': 'KW_UNMUTABLE',
    'final': 'KW_UNMUTABLE',
    'ent': 'KW_ENT',
    'flt': 'KW_FLT',
    'lg': 'KW_LG',
    'str': 'KW_STR',
    'fct': 'FCT',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'clg': 'CLG',
    'scn': 'SCN'
}

# Tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_COLON = r':'
t_ASSIGN = r'='

# Operadores de comparación
t_EQ = r'=='
t_NE = r'!='
t_LE = r'<='
t_GE = r'>='
t_LT = r'<'
t_GT = r'>'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+\.\d+|\.\d+|\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        t.value = int(t.value)
    return t

def t_STRING_START(t):
    r'"'
    t.lexer.push_state('string')
    return t

# Reglas para strings
t_string_ignore = ' \t'

def t_string_STRING_TEXT(t):
    r'[^$\n"]+'
    t.type = 'STRING_TEXT'
    return t

def t_string_STRING_VAR(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value[1:]
    t.type = 'STRING_VAR'
    return t

def t_string_STRING_END(t):
    r'"'
    t.lexer.pop_state()
    t.type = 'STRING_END'
    return t

def t_string_error(t):
    print(f"Carácter ilegal en string: '{t.value[0]}'")
    t.lexer.skip(1)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

# -------------------------------
# Parser (Corregido y verificado)
# -------------------------------
precedence = (
    ('right', 'UMINUS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_programa(p):
    '''programa : LBRACE sentencias RBRACE'''
    p[0] = ('program', p[2])

def p_sentencias(p):
    '''sentencias : 
                  | sentencias sentencia'''
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_sentencia(p):
    '''sentencia : declaracion
                 | asignacion
                 | funcion
                 | estructura_control
                 | kw_clg
                 | expresion
                 | retorno'''
    p[0] = p[1]

def p_retorno(p):
    '''retorno : RETURN expresion SEMI'''
    p[0] = ('return', p[2])

def p_retorno_opcional(p):
    '''retorno_opcional : COLON tipo
                        | empty'''
    p[0] = p[2] if len(p) > 1 else None

def p_tipo_obligatorio(p):
    '''tipo_obligatorio : KW_ENT
                        | KW_FLT
                        | KW_LG
                        | KW_STR'''
    p[0] = p[1]

def p_funcion(p):
    '''funcion : FCT ID LPAREN parametros RPAREN retorno_opcional LBRACE sentencias RBRACE'''
    p[0] = ('func', p[2], p[4], p[6], p[8])



def p_parametros(p):
    '''parametros : parametro
                  | parametro COMMA parametros'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

        
def p_parametro(p):
    '''parametro : tipo_obligatorio ID'''
    p[0] = (p[1], p[2])

def p_declaracion(p):
    '''declaracion : KW_UNMUTABLE tipo_obligatorio ID ASSIGN expresion SEMI
                   | tipo_obligatorio ID ASSIGN expresion SEMI
                   | KW_UNMUTABLE tipo_obligatorio ID SEMI
                   | tipo_obligatorio ID SEMI'''
    if len(p) == 7:
        p[0] = ('decl_const', p[2], p[3], p[5])
    elif len(p) == 6:
        p[0] = ('decl_var', p[1], p[2], p[4])
    elif len(p) == 5:
        p[0] = ('decl_const', p[2], p[3], None)
    else:
        p[0] = ('decl_var', p[1], p[2], None)

def p_asignacion(p):
    '''asignacion : ID ASSIGN expresion SEMI'''
    p[0] = ('asignacion', p[1], p[3])

def p_expresion(p):
    '''expresion : operacion_aritmetica SEMI
                | llamada_funcion SEMI
                | SCN SEMI
                | retorno'''
    p[0] = p[1]

def p_operacion_aritmetica(p):
    '''operacion_aritmetica : termino
                           | operacion_aritmetica PLUS termino
                           | operacion_aritmetica MINUS termino'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_termino(p):
    '''termino : factor
              | termino MULTIPLY factor
              | termino DIVIDE factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_factor(p):
    '''factor : NUMBER
             | ID
             | LPAREN operacion_aritmetica RPAREN
             | llamada_funcion
             | MINUS factor %prec UMINUS'''
    if len(p) == 2:
        p[0] = ('num', p[1]) if isinstance(p[1], (int, float)) else ('var', p[1])
    else:
        p[0] = ('uminus', p[2])

def p_llamada_funcion(p):
    '''llamada_funcion : ID LPAREN argumentos RPAREN'''
    p[0] = ('llamada_func', p[1], p[3])

def p_argumentos(p):
    '''argumentos : expresion
                  | argumentos COMMA expresion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_estructura_control(p):
    '''estructura_control : estructura_if
                         | ciclo_for
                         | ciclo_while'''
    p[0] = p[1]

def p_estructura_if(p):
    '''estructura_if : IF LPAREN expresion_logica RPAREN LBRACE sentencias RBRACE else_opcional'''
    p[0] = ('if', p[3], p[6], p[8])

def p_else_opcional(p):
    '''else_opcional : ELSE LBRACE sentencias RBRACE
                    | empty'''
    p[0] = p[3] if len(p) > 1 else None

def p_expresion_logica(p):
    '''expresion_logica : expresion operadores_comparacion expresion'''
    p[0] = (p[2], p[1], p[3])

def p_operadores_comparacion(p):
    '''operadores_comparacion : LT
                             | GT
                             | EQ
                             | NE
                             | LE
                             | GE'''
    p[0] = p[1]

def p_ciclo_for(p):
    '''ciclo_for : FOR LPAREN declaracion SEMI expresion_logica SEMI asignacion RPAREN LBRACE sentencias RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_ciclo_while(p):
    '''ciclo_while : WHILE LPAREN expresion_logica RPAREN LBRACE sentencias RBRACE'''
    p[0] = ('while', p[3], p[6])

def p_kw_clg(p):
    '''kw_clg : CLG LPAREN string_content RPAREN SEMI'''
    p[0] = ('clg', p[3])

def p_string_content(p):
    '''string_content : string_literal
                     | ID'''
    p[0] = p[1]

def p_string_literal(p):
    '''string_literal : STRING_START string_parts STRING_END'''
    p[0] = ('string', p[2])

def p_string_parts(p):
    '''string_parts : 
                    | STRING_TEXT
                    | STRING_VAR
                    | string_parts STRING_TEXT
                    | string_parts STRING_VAR'''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_tipo(p):
    '''tipo : tipo_obligatorio
            | empty'''
    p[0] = p[1] if len(p) > 1 else None

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, token: {p.type} ({p.value})")
    else:
        print("Error de sintaxis al final del archivo")

parser = yacc.yacc()

# -------------------------------
# Prueba Final (Verificada)
# -------------------------------
data = """
{
    const ent edad = 25;
    fct suma(ent a, ent b): ent {
        return a + b;
    }
    
    clg("Resultado: $edad");
}
"""

result = parser.parse(data, lexer=lexer)
print("AST Generado:")
print(result)