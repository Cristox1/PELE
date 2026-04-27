grammar PELE;

// REGLAS LÉXICAS
TRUE    : 'true' ;
FALSE   : 'false' ;
STRING  : '"' ~["]* '"' ; // Comillas dobles escapadas
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
INT     : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;

// REGLAS SINTÁCTICAS
program : block EOF ;

block
    : statement+
    ;

statement
    : assignment ';'        # assignStmt
    | expr ';'              # exprStmt
    | 'mostrar' '(' expr ')' ';' # mostrarStmt
    | ifStatement           # ifStmt
    ;

ifStatement
    : 'si' '(' expr ')' '{' block '}' ('sino' '{' block '}')?
    ;

assignment
    : ID '=' expr
    ;

expr
    : '-' expr                          # UnaryMinusExpr
    | expr '**' expr                    # PowerExpr
    | expr ('*' | '/' | '%') expr       # MulDivModExpr
    | expr ('+' | '-') expr             # AddSubExpr
    | expr ('<' | '<=' | '>' | '>=' | '==' | '!=') expr # RelationalExpr
    | '[' expr (',' expr)* ']'          # ArrayExpr
    | TRUE                              # BoolExpr
    | FALSE                             # BoolExpr
    | STRING                            # StringExpr
    | INT                               # IntExpr
    | FLOAT                             # FloatExpr
    | ID '(' (expr (',' expr)*)? ')'    # FuncCallExpr
    | ID                                # IdExpr
    | '(' expr ')'                      # ParensExpr
    ;