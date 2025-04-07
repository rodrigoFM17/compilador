import ply.yacc as yacc
from lexico import tokens, lexer

# Precedencia de operadores
precedence = (
    ('right', 'UMINUS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

# Regla inicial corregida
def p_programa(p):
    '''programa : LBRACE sentencias RBRACE
               | sentencias'''
    p[0] = ('programa', p[1] if len(p) == 2 else p[2])

def p_sentencias(p):
    '''sentencias : sentencia
                  | sentencias sentencia'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_sentencia(p):
    '''sentencia : declaracion
                 | asignacion
                 | funcion
                 | estructura_control
                 | kw_clg
                 | expresion
                 | retorno'''  # <- Nueva regla
    p[0] = p[1]

def p_retorno(p):
    '''retorno : RETURN expresion SEMI'''
    p[0] = ('return', p[2])

def p_funcion(p):
    '''funcion : FCT ID LPAREN parametros RPAREN COLON tipo LBRACE sentencias RBRACE
               | FCT ID LPAREN RPAREN COLON tipo LBRACE sentencias RBRACE
               | FCT ID LPAREN parametros RPAREN LBRACE sentencias RBRACE
               | FCT ID LPAREN RPAREN LBRACE sentencias RBRACE'''
    if len(p) == 11:  # Con parámetros y tipo retorno
        p[0] = ('func_con_retorno', p[2], p[4], p[7], p[9])
    elif len(p) == 10:  # Sin parámetros con tipo retorno
        p[0] = ('func_con_retorno', p[2], [], p[6], p[8])
    elif len(p) == 9:  # Con parámetros sin tipo retorno
        p[0] = ('func_sin_retorno', p[2], p[4], p[7])
    else:  # Sin parámetros ni tipo retorno
        p[0] = ('func_sin_retorno', p[2], [], p[6])

# Modifica la regla del factor
def p_factor(p):
    '''factor : NUMBER
             | ID
             | LPAREN operacion_aritmetica RPAREN
             | llamada_funcion
             | MINUS factor %prec UMINUS'''  # Aquí aplicamos la precedencia
    if len(p) == 2:
        if isinstance(p[1], (int, float)):
            p[0] = ('num', p[1])
        else:
            p[0] = ('var', p[1])
    else:
        if p[1] == '-':
            p[0] = ('uminus', p[2])
        else:
            p[0] = p[2]


def p_declaracion(p):
    '''declaracion : KW_UNMUTABLE tipo ID ASSIGN expresion SEMI
                   | tipo ID ASSIGN expresion SEMI
                   | KW_UNMUTABLE tipo ID SEMI
                   | tipo ID SEMI'''
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
                | SCN SEMI'''
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

def p_parametros(p):
    '''parametros : parametro
                  | parametros COMMA parametro'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_parametro(p):
    '''parametro : tipo ID'''
    p[0] = (p[1], p[2])

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
    '''string_content : ID
                     | string_literal'''
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
    '''tipo : KW_ENT
           | KW_FLT
           | KW_LG
           | KW_STR'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, token: {p.type} ({p.value})")
    else:
        print("Error de sintaxis al final del archivo")

# Construir el parser
parser = yacc.yacc()

data = """
{
    const ent edad = 25;
    fct suma(ent a, ent b): ent {
        return -a + b;
    }
    
    clg("Resultado: $edad");
}
"""

result = parser.parse(data, lexer=lexer)
print(result)