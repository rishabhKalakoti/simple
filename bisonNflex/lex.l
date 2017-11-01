%{
#include "parser.tab.h"
#define YY_DECL extern int yylex()

int line_no = 1;
%}

%%
[ \t]          			;
(==|<=|>=|<|>)			{return RELOP;}
not				{return NOTOP;}
and|or				{return LOGICOP;}
[=\(\)]				{return yytext[0];}
[\+\-\*\/]			{return ARITHOP;}
[0-9]+		  		{yylval.ival = atoi(yytext); return NUM;}
$[a-zA-Z0-9_]*	  		{yylval.sval = strdup(yytext); return VAR;}
\n				{++line_no; return ENDL;}
if				{return IF;}
end				{return END;}
else				{return ELSE;}
loop				{return LOOP;}
over				{return OVER;}
.				{return yytext[0];}
%%
/*
int yywrap()
{
	return 1;
}*/
