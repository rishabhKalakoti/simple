import re


def lexer(code):
	symbolTable = {\
		"VAR":[],\
		"NUM":[],\
		"FNAME":[],\
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
		[r' and | or ', "#LOGICOP"],\
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
		[r'not', "#NOTOP"],\
		[r'if', "#IF"],\
		[r'func', "#FUNC"],\
		[r'end', "#END"],\
		[r'loop', "#LOOP"],\
		[r'over', "#OVER"],\
		[r'next|out', "#BREAK"],\
		[r'\#FUNC[a-zA-z0-9_]', "#FUNC#SPACE#FNAME"],\
		]
	
	
	symbolTable["VAR"].extend(list(set(re.findall(r'\$[a-zA-Z0-9_]*', code))))
	symbolTable["NUM"].extend(list(set(re.findall(r'[0-9]+', code))))
	symbolTable["FNAME"].extend(list(set(re.findall(r'func [a-zA-Z0-9_]*', code))))
	

	code = re.sub(r'\#FUNC\#SPACE[a-zA-Z0-9_]*',"#CALLOP#FNAME",code)

	for i in range(len(regList)):
		code = re.sub(regList[i][0], regList[i][1], code)
	for i in range(len(symbolTable["FNAME"])):
		symbolTable["FNAME"][i]=re.sub(r'func ', "", symbolTable["FNAME"][i])
		code = re.sub(r'\#CALLOP[a-zA-Z0-9_]*',"#CALLOP#FNAME",code)
	code = re.sub(r'\#FUNC\#SPACE[a-zA-Z0-9_]*',"#FUNC#SPACE#FNAME",code)

	return code, symbolTable
