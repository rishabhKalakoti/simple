import syntax
import pre
import lex

fileName = "code.simple"
code = open(fileName, 'r').read()

# -------- getting file after preprocessor output
code = pre.preprocessor(code)
# -------- getting output after lexical analysis
symbolTable = dict()
code, symbolTable = lex.lexer(code)
#print("")
if(syntax.syntaxChecker(code, symbolTable) == False):
	# print(syntax.ERROR)
	print("DEAD!!")
	exit()

print("-"*10, "LEX OUTPUT", "-"*10)
print(code)
print("")
print("-"*10, "SYMBOL TABLE", "-"*10)
for element in symbolTable:
	print("#%s : %s" %(element,symbolTable[element]))
print("")
print("GOOD TO GO!")

