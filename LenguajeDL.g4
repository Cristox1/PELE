grammar LenguajeDL;

// --- REGLAS SINTÁCTICAS (PARSER) ---
program: statement+ EOF ;

statement
    : assignment ';'            # assignStmt
    | expr ';'                  # exprStmt
    | 'print' '(' expr ')' ';' # printStmt
    ;

assignment: ID '=' expr ;

expr
    : 'not' expr                                        # NotExpr
    | '-' expr                                          # UnaryMinusExpr
    | expr op='**' expr                                 # PowExpr
    | expr op=('*'|'/'|'%') expr                       # MulDivModExpr
    | expr op=('+'|'-') expr                            # AddSubExpr
    | expr op=('<'|'<='|'>'|'>='|'=='|'!=') expr       # CompareExpr
    | expr op=('and'|'or') expr                         # LogicExpr
    | '[' expr (',' expr)* ']'                          # ArrayExpr
    | INT                                               # IntExpr
    | FLOAT                                             # FloatExpr
    | 'true'                                            # TrueExpr
    | 'false'                                           # FalseExpr
    | ID                                                # IdExpr
    | '(' expr ')'                                      # ParensExpr
    ;

// --- REGLAS LÉXICAS (LEXER) ---
POW  : '**' ;
MUL  : '*' ;
DIV  : '/' ;
MOD  : '%' ;
ADD  : '+' ;
SUB  : '-' ;
EQ   : '==' ;
NEQ  : '!=' ;
LTE  : '<=' ;
GTE  : '>=' ;
LT   : '<' ;
GT   : '>' ;
AND  : 'and' ;
OR   : 'or' ;
NOT  : 'not' ;
TRUE : 'true' ;
FALSE: 'false' ;

ID    : [a-zA-Z_][a-zA-Z0-9_]* ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT   : [0-9]+ ;
WS    : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;