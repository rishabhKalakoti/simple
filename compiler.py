import pre
import lex

fileName = "code.simple"
code = open(fileName, 'r').read()

# -------- getting file after preprocessor output
code = pre.preprocessor(code)
print(code)
print("")
# -------- getting output after lexical analysis
symbolTable = dict()
code, symbolTable = lex.lexer(code)

print(code)
print(symbolTable)
