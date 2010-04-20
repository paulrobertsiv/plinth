grammar Expr;

options {
    language=Python;
    output=AST;
    ASTLabelType=CommonTree;
}

prog: ( stat {print $stat.tree.toStringTree();} )+ ;

stat:expr NEWLINE        -> expr
    |'=' ID expr NEWLINE -> ^('=' ID expr)
    |NEWLINE             ->
    ;

expr: LPAREN! ('+'^|'*'^|'-'^) (atom|expr) (atom|expr) RPAREN!
    ;

atom:INT
//    |FLOAT
    |ID
    |'('! expr ')'!
    ;

ID:('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'?'|INT)* ;
INT:'0'..'9'+ ;
//FLOAT:('0'..'9')*'.'('0'..'9')+

LPAREN:'(' ;
RPAREN:')' ;

NEWLINE:'\r'? '\n' ;
WS:(' '|'\t'|'\n'|'\r')+ {self.skip()} ;
