grammar PELE;

// REGLAS LÉXICAS

TRUE  : 'true' ;
FALSE : 'false' ;
STRING: '"' ~'"'* '"' ; // Reconoce cualquier cosa entre comillas dobles
ID    : [a-zA-Z_][a-zA-Z0-9_]* ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT   : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;


// REGLAS SINTÁCTICAS
program: statement+ EOF ;

statement: assignment ';'             # assignStmt
         | expr ';'                   # exprStmt
         | 'mostrar' '(' expr ')' ';' # mostrarStmt
         ;

assignment: ID '=' expr ;

expr: '-' expr                                # UnaryMinusExpr
    | expr op='**' expr                       # PowerExpr
    | expr op=('*'|'/'|'%') expr              # MulDivModExpr
    | expr op=('+'|'-') expr                  # AddSubExpr
    | expr op=('<'|'<='|'>'|'>='|'=='|'!=') expr # RelationalExpr
    | '[' expr (',' expr)* ']'                # ArrayExpr
    | TRUE                                    # BoolExpr
    | FALSE                                   # BoolExpr
    | STRING                                  # StringExpr     
    | INT                                     # IntExpr
    | FLOAT                                   # FloatExpr
    | ID                                      # IdExpr
    | '(' expr ')'                            # ParensExpr
    ;




