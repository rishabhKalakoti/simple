"""
	
"""

import re
ERROR=""

def syntaxChecker(code):
	if(not isStmtList(code)):
		return False
	return True

def isStmtList(code):
	# <func_dec> | <var_dec> | <control_dec>
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
	return True

def isLoopStmt(loopStmt):
	return True

def isStmt(stmt):
	# ----------- <var_asst><function_call>
	if stmt=="#SPACE":
		return True
	print(stmt)
	if not (isFunctionCall(stmt) or isVarAsst(stmt)):
		return False
	return True

def isVarAsst(stmt):
	if stmt==None:
		print("xxx")
	print(re.match(r'\#VAR(\#SPACE)?\#ASSTOP.*$', stmt, re.I))
	if not re.match(r'\#VAR(\#SPACE)?\#ASSTOP.*$', stmt, re.I):
		return False
	print(re.match(r'\#VAR(\#SPACE)?\#ASSTOP.*$', stmt, re.I))
	return True

def isFunctionCall(stmt):
	if not re.match(r'\#CALLOP\#FNAME\#LPAREN(.*)\#RPAREN$', stmt, re.I):
		return False
	print(re.match(r'\#CALLOP\#FNAME\#LPAREN(.*)\#RPAREN$', stmt, re.I))
	#----------( incomplete )---------
	print(stmt)
	return True
