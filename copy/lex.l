%{
#include "parser.tab.h"
#define YY_DECL extern int yylex()
int line_no = 1;
%}

%%
[ \t]          			;

[\+\-\*\/]			{return ARITHOP;}
[0-9]+		  		{return NUM;}
[a-zA-Z0-9_]*	  		{return VAR;}
\n				{++line_no; return ENDL;}
.				{return yytext[0];}
%%
/*
int yywrap()
{
	return 1;
}*/
