grammar LenguajeDL; // <-- ¡ESTO DEBE COINCIDIR CON EL NOMBRE DEL ARCHIVO!

// --- REGLAS SINTÁCTICAS (PARSER) ---
program: statement+ EOF ;

statement: assignment ';'       # assignStmt
         | expr ';'             # exprStmt
         | 'print' '(' expr ')' ';' # printStmt
         ;

assignment: ID '=' expr ;

expr: '-' expr                  # UnaryMinusExpr  
    | expr op=('*'|'/') expr    # MulDivExpr
    | expr op=('+'|'-') expr    # AddSubExpr
    | '[' expr (',' expr)* ']'  # ArrayExpr
    | INT                       # IntExpr
    | FLOAT                     # FloatExpr
    | ID                        # IdExpr
    | '(' expr ')'              # ParensExpr
    ;

// --- REGLAS LÉXICAS (LEXER) ---
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

ID    : [a-zA-Z_][a-zA-Z0-9_]* ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT   : [0-9]+ ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;