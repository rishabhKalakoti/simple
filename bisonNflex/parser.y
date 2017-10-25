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
	float fval;
	char *sval;
}
%token <ival> NUM
%token <fval> FLOAT
%token <sval> VAR
%token ENDL
%token ARITHOP
%token RELOP
%token END
%token IF
%token ELSE
%token LOOP
%token OVER
%token NOTOP
%token LOGICOP
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
	| conditional
	| loop_stmt
	;
loop_stmt:
	LOOP IF '(' logic_exp ')' ENDLS dec_list END LOOP ENDLS
	| LOOP VAR OVER NUM ENDLS dec_list END LOOP ENDLS
	;
conditional:
	IF '(' logic_exp ')' ENDLS dec_list  ELSE conditional		
	| IF '(' logic_exp ')' ENDLS dec_list  ELSE ENDLS dec_list END IF ENDLS
	| IF '(' logic_exp ')' ENDLS dec_list END IF ENDLS	
	;
logic_exp:
	logic_exp LOGICOP rel_exp
	| rel_exp
	;
asst:
	VAR '=' logic_exp ENDLS
	;
rel_exp:
	rel_exp RELOP arith_exp
	| arith_exp
	;
arith_exp:
	arith_exp ARITHOP term
	| term
	;
term:
	'(' logic_exp ')'
	| NUM 
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
