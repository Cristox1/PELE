grammar PELE;

// LÉXICOS
TRUE    : 'true' ;
FALSE   : 'false' ;
STRING  : '"' ~["]* '"' ;

SI      : 'si' ;
SINO    : 'sino' ;
MOSTRAR : 'mostrar' ;
MIENTRAS: 'mientras' ;
POR     : 'por' ;
FOR     : 'for' ;
IN      : 'in' ;
FUNCION : 'funcion' ;
RETORNAR: 'retornar' ;

// Identificador y números
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
INT     : [0-9]+ ;

// Espacios y comentarios
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;

// SINTÁCTICAS
program : block EOF ;

block
    : statement*
    ;

statement
    : assignment ';'                                       # assignStmt
    | expr ';'                                             # exprStmt
    | MOSTRAR '(' expr ')' ';'                             # mostrarStmt
    | ifStatement                                          # ifStmt
    | MIENTRAS '(' expr ')' '{' block '}'                  # cicloWhile
    | POR '(' assignment ';' expr ';' assignment ')' '{' block '}'   # cFor
    | FOR '(' ID IN expr ')' '{' block '}'                 # forEach
    | functionDecl                                         # functionDeclStmt
    | RETORNAR expr ';'                                    # returnStmt
    ;

ifStatement
    : SI '(' expr ')' '{' block '}' ( SINO '{' block '}' )?
    ;

functionDecl
    : FUNCION ID '(' params? ')' '{' block '}'
    ;

params
    : ID (',' ID)*
    ;

assignment
    : ID '=' expr
    ;

expr
    : '-' expr                                # UnaryMinusExpr
    | expr '**' expr                          # PowerExpr
    | expr ('*' | '/' | '%') expr             # MulDivModExpr
    | expr ('+' | '-') expr                   # AddSubExpr
    | expr ('<' | '<=' | '>' | '>=' | '==' | '!=') expr   # RelationalExpr
    | '[' (expr (',' expr)*)? ']'             # ArrayExpr
    | TRUE                                    # BoolExpr
    | FALSE                                   # BoolExpr
    | STRING                                  # StringExpr
    | INT                                     # IntExpr
    | FLOAT                                   # FloatExpr
    | ID '(' (expr (',' expr)*)? ')'          # FuncCallExpr
    | ID                                      # IdExpr
    | '(' expr ')'                            # ParensExpr
    ;