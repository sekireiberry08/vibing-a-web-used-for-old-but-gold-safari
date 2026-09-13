grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls EOF;
decls: decl decls | decl;
decl: vardecl|funcdecl;
vardecl: typ_ listid ';';
typ_: 'int'|'float';
listid: ID ',' listid | ID;
funcdecl: typ_ ID paramdecl body;
paramdecl: '(' paramlist ')';
paramlist: params | ;
params: param ';' params | param;
param: typ_ listid;
body: '{' inner '}';
inner: member inner | ;
member: vardecl | stmt;
stmt: assignment | call | retur_;
assignment: ID '=' expr ';';
call: ID '(' exprlist ')' ';';
exprlist: expr ',' exprlist | expr;
retur_: 'return' expr ';';
expr: expr0 '+' expr | expr0;
expr0: expr1 '-' expr1 | expr1;
expr1: expr1 ('*'|'/') operand | operand;
operand: INTLIT | FLOATLIT | ID | call_ | '(' expr ')'; 
call_: ID '(' exprlist ')';
ID	 	 : [a-zA-Z]+ ;
INTLIT	 :[0-9]+;
FLOATLIT : [0-9]+'.'[0-9]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
