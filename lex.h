char var[20][20];
int varCount=0;
char num[20][20];
int numCount=0;

char Table[13][100]={
					"#COMPOP: == != < > <= >=",
					"#RELPOP: and or",
					"#ARITHOP: + - * /",
					"#NEWLINE: \\n",
					"#IF: if",
					"#END: end",
					"#LOOP: loop",
					"#OVER: over",
					"#NOT: not",
					"#BREAK: next out",
					"#FUNC: func",
					"#COMMA: ,",
					"#CALLOP: `",
					};

// addSymbol(yytext, "#VAR");
void addSymbol(char text[20], char type[10])
{
	int i;
	if(type=="#VAR")
	{
		int flag;
		flag=0;
		for (i=0; i<varCount;i++)
		{
			if(var[i] == text)
				flag=1;
		}
		if(flag!=1)
			strcpy(var[varCount++],text);
	}
	if(type=="#NUM")
	{
		strcpy(num[numCount++],text);
	}
}

void printTable()
{
	int i;
	printf("\n#VAR: ");
	for(i=0; i<varCount; i++)
	{
		printf("%s ", var[i]);
	}
	printf("\n#NUM: ");
	for(i=0; i<numCount; i++)
	{
		printf("%s ", num[i]);
	}
	for(i=0; i<13; i++)
	{
		printf("\n%s", Table[i]);
	}
}
