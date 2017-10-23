%{
#include "parser.tab.h"
#define YY_DECL extern int yylex()
int line_no = 1;
%}

%%
[ \t]          			;
=				{return '=';}
[\+\-\*\/]			{return ARITHOP;}
[0-9]+		  		{yylval.ival = atoi(yytext); return NUM;}
$[a-zA-Z0-9_]*	  		{yylval.sval = strdup(yytext); return VAR;}
\n				{++line_no; return ENDL;}
.				;
%%
/*
int yywrap()
{
	return 1;
}*/
