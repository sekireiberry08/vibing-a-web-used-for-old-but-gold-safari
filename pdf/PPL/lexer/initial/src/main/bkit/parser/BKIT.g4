grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;

ID : ( '0' | [1-9] ( '_'* [0-9] )* ) { self.text = self.text.replace('_', '') } ;
SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .  {raise ErrorToken(self.text)};

