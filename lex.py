import re


def lexer(code):
	symbolTable = {\
		"VAR":[],\
		"NUM":[],\
		"RELOP":["==",">","<",">=","<=","!="],\
		"ARITHOP":["+","-","*","/"],\
		"LOGICOP":["and","or"],\
		"NOTOP":["not"],\
		"IF":["if"],\
		"FUNC":["func"],\
		"END":["end"],\
		"LOOP":["loop"],\
		"OVER":["over"],\
		"LPAREN":["("],\
		"RPAREN":[")"],\
		"ASSTOP":["="],\
		"BREAK":["next", "out"],\
		"SPACE":[" "],\
		"CALLOP":["`"],\
		"COMMA":[","],\
		}
	
	regList=[\
		[r'\n', "#NEWLINE"],\
		[r' ', "#SPACE"],\
		[r'`', "#CALLOP"],\
		[r',', "#COMMA"],\
		[r'\(', "#LPAREN"],\
		[r'\)', "#RPAREN"],\
		[r'=', "#ASSTOP"],\
		[r'".*?"', "#STR"],\
		[r'\$[a-zA-Z0-9_]*', "#VAR"],\
		[r'[0-9]+', "#NUM"],\
		[r'==|>|<|>=|<=|!=', "#RELOP"],\
		[r'\+|\-|\*|\/', "#ARITHOP"],\
		[r' and | or ', "#LOGICOP"],\
		[r'not', "#NOTOP"],\
		[r'if', "#IF"],\
		[r'func', "#FUNC"],\
		[r'end', "#END"],\
		[r'loop', "#LOOP"],\
		[r'over', "#OVER"],\
		[r'next|out', "#BREAK"],\
		]
	
	
	symbolTable["VAR"].extend(list(set(re.findall(r'\$[a-zA-Z0-9_]*', code))))
	symbolTable["NUM"].extend(list(set(re.findall(r'[0-9]+', code))))

	for i in range(len(regList)):
		code = re.sub(regList[i][0], regList[i][1], code)

	return code, symbolTable
