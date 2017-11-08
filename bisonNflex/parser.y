%{
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern int yyparse();
extern FILE *yyin;
extern int line_no;
void yyerror(const char *s);
void assType(char* var);
void showerror(char* s);
int l=0;
int chk;
int i;
typedef struct node
{
	char type;
	char* name;
}element;
element variables[20];

%}
%union {
	int ival;
	float fval;
	char* sval;
}
%token <ival> NUM
%token <fval> FLOAT
%token <sval> VAR
%token <sval> STR
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
	asst 				{chk=1;}
	| conditional		{chk=0;}
	| loop_stmt			{chk=0;}
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
	logic_exp LOGICOP rel_exp	{chk=0;}
	| rel_exp					{if(chk==1) chk=1;}
	;
asst:
	VAR '=' logic_exp ENDLS		{assType($1);}	
	;
rel_exp:
	rel_exp RELOP arith_exp		{chk=0;}
	| arith_exp					{if(chk==1) chk=1;}
	;
arith_exp:
	arith_exp ARITHOP term		{chk=0;}
	| term						{if(chk==1) chk=1;}
	;
term:
	'(' logic_exp ')'			{chk=0;}
	| VAR
	| NUM						{
									if(variables[i].type=='N' && chk==1) variables[i].type='I';
									if(variables[i].type!='I' && chk==1) {chk=1; showerror("conflicting types");}
								}
	| FLOAT						{
									if(variables[i].type=='N' && chk==1) variables[i].type='F';
									if(variables[i].type!='F' && chk==1) {chk=1; showerror("conflicting types");}
								} 
	| STR						{
									if(variables[i].type=='N' && chk==1) variables[i].type='S';
									if(variables[i].type!='S' && chk==1) {chk=1; showerror("conflicting types");}
								}
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


void showerror(char* s)
{
	printf("%s on line %d\n", s, line_no);
	exit(-1);
}

void assType(char var[20])
{
	int j=0;
	int flag;
	flag=0;
	for(j=0; j<l; j++)
	{
		if(variables->name==var)
		{
			flag=1;
			i=j;
			break;
		}
	}
	if(flag==0)
	{
		variables[l].type='N';
		variables[l].name=strdup(var);
		i=l;
		l++;
	}
	flag=0;
}
