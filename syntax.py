import re
ERROR=""

def syntaxChecker(code, symbolTable):
	if(not isStmtList(code)):
		return False
	return True

def isStmtList(code):
	# <func_def> | <func_dec> | <var_dec> | <control_dec>
	# ----------- func def
	funcDef = re.findall(r'\#FUNC.*?\#END\#SPACE\#FUNC', code)
	for stmt in funcDef:
		if not isFuncDef(stmt):
			return False
	code = re.sub(r'\#FUNC.*?\#END\#SPACE\#FUNC', "", code)
	
	# ----------- if stmt
	ifStmt = re.findall(r'\#IF.*?\#END\#SPACE\#IF', code)
	for stmt in ifStmt:
		if not isIfStmt(stmt):
			return False
	code = re.sub(r'\#IF.*?\#END\#SPACE\#IF', "", code)
	# ----------- loop stmt
	loopStmt = re.findall(r'\#LOOP.*?\#END\#SPACE\#LOOP', code)
	for stmt in loopStmt:
		if not isLoopStmt(stmt):
			return False
	code = re.sub(r'\#LOOP.*?\#END\#SPACE\#LOOP', "", code)
	# ----------- simple stmt
	for stmt in code.split("#NEWLINE"):
		if not isStmt(stmt):
			return False
	
	return True

def isFuncDef(stmt):
	return True

def isIfStmt(ifStmt):
	ifObj = re.match(r'\#IF\#LPAREN(.*)\#RPAREN(.*)\#END\#SPACE\#IF', ifStmt)
	if not isLogicExp(ifObj.group(1)):
		return False
	if not isStmtList(ifObj.group(2)):
		return False
	if ifObj==None:
		return False
	return True

def isLoopStmt(loopStmt):
	return True

def isStmt(stmt):
	# ----------- <var_asst><function_call>
	if stmt=="#SPACE":
		return True
	if not (isFunctionCall(stmt) or isVarAsst(stmt)):
		return False
	return True

def isVarAsst(stmt):
	stmt=re.sub(r'\#SPACE', "", stmt)
	if stmt=="":
		return True
	if not re.match(r'\#VAR(\#SPACE)?\#ASSTOP.*$', stmt, re.I):
		return False
	if not isArithExp(re.match(r'\#VAR(\#SPACE)?\#ASSTOP(.*)$', stmt, re.I).group(2)):
		return False
	return True

def isFunctionCall(stmt):
	if not re.match(r'\#CALLOP\#FNAME\#LPAREN(.*)\#RPAREN$', stmt, re.I):
		return False
	#----------( incomplete )---------arguments not done yet
	
	return True

def isLogicExp(stmt):
	if re.match(r'(\#SPACE)?\#NOT(\#SPACE)?(.*)(\#SPACE)?',stmt)!=None:
		if isLogicExp(re.match(r'(\#SPACE)?\#NOT(\#SPACE)?(.*)(\#SPACE)?',stmt).group(3)):
			return True
		return False
	if(re.match(r'\#LOGICOP',stmt)==None):
		if not isRelExp(stmt):
			return False
	if re.search(r'\#LOGICOP', stmt)!=None:
		for exp in re.split(r'\#LOGICOP', stmt):
			if not (isLogicExp(exp)):
				return False
	if(stmt==""):
		return False
	return True

def isRelExp(stmt):
	stmt=re.sub(r'\#SPACE', "", stmt)
	if stmt=="" or stmt==None:
		return True
	for exp in re.split(r'\#RELOP', stmt):
		if not (isArithExp(exp)):
			return False
	return True

def isArithExp(stmt):
	for term in re.split(r'\#ARITHOP', stmt):
		if not (isTerm(term)):
			return False
	return True

def isTerm(term):
	if re.match(r'\#VAR|\#NUM|#LPAREN.*\#RPAREN$', term)==None:
		return False
	if re.match(r'\#LPAREN(.*)\#RPAREN$', term)!=None:
		if not isArithExp(re.match(r'\#LPAREN(.*)\#RPAREN$', term).group(1)):
			return False
	return True
