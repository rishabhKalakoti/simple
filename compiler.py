import syntax
import pre
import lex

fileName = "code.simple"
code = open(fileName, 'r').read()


code = pre.preprocessor(code)
symbolTable = dict()
code, symbolTable = lex.lexer(code)
if(syntax.syntaxChecker(code, symbolTable) == False):
	# print(syntax.ERROR)
	print("DEAD!!")
	exit()
# --------------- print lex output
print("-"*10, "LEX OUTPUT", "-"*10)
print(code)
print("")
# --------------- print symbol table
print("-"*10, "SYMBOL TABLE", "-"*10)
for element in symbolTable:
	print("#%s : %s" %(element,symbolTable[element]))
print("")
print("GOOD TO GO!")
