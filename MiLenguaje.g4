grammar MiLenguaje;

// Parser Rules
programa
    : sentencia* EOF
    ;

sentencia
    : declaracion
    | asignacion
    | estructuraDeControl
    | llamadaFuncion ';'?
    | kwClg ';'?
    | funcionConRetorno
    | funcionSinRetorno
    | retornoSentencia ';'
    ;

declaracion
    : kwUnmutable? tipo ID ('=' (expresion | kwScn))? ';'
    ;

asignacion
    : ID '=' expresion ';'
    ;

// Expresiones sin recursión a la izquierda
expresion
    : termino (operadoresAritmeticos termino)*
    ;

termino
    : llamadaFuncion
    | '(' expresion ')'
    | ID
    | NUMERO_VALORES
    | STRING
    ;

funcionConRetorno
    : 'fct' ID '(' parametros? ')' ':' tipo '{' sentencia* '}'
    ;

funcionSinRetorno
    : 'fct' ID '(' parametros? ')' '{' sentencia* '}'
    ;

parametros
    : tipo ID (',' tipo ID)*
    ;

llamadaFuncion
    : ID '(' (expresion (',' expresion)*)? ')'
    ;

estructuraDeControl
    : estructuraIf
    | cicloFor
    | cicloWhile
    ;

estructuraIf
    : 'if' '(' expresionLogica ')' '{' sentencia* '}' ('else' '{' sentencia* '}')?
    ;

expresionLogica
    : expresion operadoresComparacion expresion
    ;

cicloFor
    : 'for' '(' (declaracion | asignacion | ';') expresionLogica ';' asignacionFor ')' '{' sentencia* '}'
    ;

asignacionFor
    : ID '=' expresion
    ;

cicloWhile
    : 'while' '(' expresionLogica ')' '{' sentencia* '}'
    ;

tipo
    : kwEnt
    | kwFlt
    | kwLg
    | kwStr
    ;

kwClg
    : 'clg' '(' (expresion | STRING ('$' ID)* | ID) ')'
    ;

retornoSentencia
    : 'rtn' expresion
    ;

kwScn
    : 'scn' '(' ')'
    ;

operadoresAritmeticos
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'    // Agregado el operador módulo que podría estar faltando
    ;

operadoresComparacion
    : '=='
    | '!='
    | '<'
    | '>'
    | '<='
    | '>='
    ;

kwUnmutable
    : 'const'
    | 'final'
    ;

kwEnt : 'ent';
kwFlt : 'flt';
kwLg : 'lg';
kwStr : 'str';

// Lexer Rules
ID : [a-zA-Z][a-zA-Z0-9_]* ;  // Permitir guiones bajos en identificadores
NUMERO_VALORES : [0-9]+ ('.' [0-9]+)? 'l'? ;
STRING : '"' .*? '"' ;
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' .*? '\r'? '\n' -> skip ;