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
// Expresiones con jerarquía de operaciones
expresion
    : expresionAditiva
    ;

expresionAditiva
    : expresionMultiplicativa (operadoresAditivos expresionMultiplicativa)*
    ;

expresionMultiplicativa
    : termino (operadoresMultiplicativos termino)*
    ;

operadoresAditivos
    : '+'
    | '-'
    ;

operadoresMultiplicativos
    : '*'
    | '/'
    | '%'
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