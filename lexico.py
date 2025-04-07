import ply.lex as lex

states = (
    ('string', 'exclusive'),
)

tokens = [
    'ID', 'NUMBER', 'STRING_TEXT', 'STRING_VAR',
    'KW_ENT', 'KW_FLT', 'KW_LG', 'KW_STR', 'KW_UNMUTABLE',
    'FCT', 'IF', 'ELSE', 'FOR', 'WHILE', 'CLG', 'SCN',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQ', 'NE', 'RETURN',
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
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE     = r'/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_SEMI       = r';'
t_COMMA      = r','
t_COLON      = r':'
t_ASSIGN     = r'='

# Operadores de comparación
t_EQ  = r'=='
t_NE  = r'!='
t_LE  = r'<='
t_GE  = r'>='
t_LT  = r'<'
t_GT  = r'>'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
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