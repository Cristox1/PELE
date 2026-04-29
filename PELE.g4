grammar PELE;

// REGLAS LEXICAS
TRUE    : 'true' ;
FALSE   : 'false' ;
STRING  : '"' ~["]* '"' ; 
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;

// REGLAS SINTACTICAS
program : block EOF ;

block
    : statement+
    ;

statement
    : functionDecl               # funcDeclStmt
    | returnStatement            # retStmt
    | assignment ';'             # assignStmt
    | expr ';'                   # exprStmt
    | 'mostrar' '(' expr ')' ';' # mostrarStmt
    | ifStatement                # ifStmt
    | whileStatement             # whileStmt
    | forStatement               # forStmt
    ;

// Estructura: funcion nombre(a, b) { ... }
functionDecl
    : 'funcion' ID '(' (ID (',' ID)*)? ')' '{' block '}'
    ;

// Estructura: retornar expr;
returnStatement
    : 'retornar' expr ';'
    ;

// Estructura: si (cond) { ... } sino (cond) { ... } entonces { ... }
ifStatement
    : 'si' '(' expr ')' '{' block '}' 
      ('sino' '(' expr ')' '{' block '}')* 
      ('entonces' '{' block '}')?
    ;

// Estructura: mientras (cond) { ... }
whileStatement
    : 'mientras' '(' expr ')' '{' block '}'
    ;

// Estructura: por (inicializacion; condicion; actualizacion) { ... }
// Ejemplo: por (i = 0; i < 10; i = i + 1) { ... }
forStatement
    : 'por' '(' assignment ';' expr ';' assignment ')' '{' block '}'
    ;

assignment
    : ID '=' expr
    ;

expr
    : '-' expr                                          # UnaryMinusExpr
    | expr '**' expr                                    # PowerExpr
    | expr ('*' | '/' | '%') expr                       # MulDivModExpr
    | expr ('+' | '-') expr                             # AddSubExpr
    | expr ('<' | '<=' | '>' | '>=' | '==' | '!=') expr # RelationalExpr
    | '[' expr (',' expr)* ']'                          # ArrayExpr
    | TRUE                                              # BoolExpr
    | FALSE                                             # BoolExpr
    | STRING                                            # StringExpr
    | INT                                               # IntExpr
    | FLOAT                                             # FloatExpr
    | ID '(' (expr (',' expr)*)? ')'                    # FuncCallExpr
    | ID                                                # IdExpr
    | '(' expr ')'                                      # ParensExpr
    ;