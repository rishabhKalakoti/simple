%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern int yyparse();
extern FILE *yyin;
extern int line_no;
void yyerror(const char *s);
%}
%union {
	int ival;
	char *sval;
}
%token <ival> NUM
%token <sval> VAR
%token END ENDL
%token ARITHOP

%%
stmt:
	dec_list
	;
dec_list:
	dec_list dec
	| dec
	;
dec:
	asst
	;
asst:
	VAR '=' arith_exp ENDLS
	;
arith_exp:
	arith_exp ARITHOP term
	| term
	;
term:
	NUM 
	| VAR
	;
ENDLS:	ENDLS ENDL
	| ENDL
	;
%%

int main() {
	yyin=fopen("code.simple","r");
	do {
		yyparse();
	} while (!feof(yyin));
	printf("All correct!\n");
	
}

void yyerror(const char *s) {
	printf("Syntax error on line %d\n", line_no);
	exit(-1);
}
