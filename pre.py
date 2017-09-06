"""
	This is the Pre-Processor for 'simple' language.
	The preprocessor has the following functions as of now:
	
	- remove comments from the program
	- remove empty lines
	- import the code of the imported files // not designing yet
"""

fileName = "code.simple"
code = open(fileName, 'r').read()

index=[]
# ------------ remove comments
codeBlock = code.split("\n")
for i in range(len(codeBlock)):
	codeBlock[i] = codeBlock[i].strip()
	if(codeBlock[i].startswith("#")):
		index.append(i)
		pass
i=len(index)-1
print(i)
while i>-1:
	codeBlock.pop(index.pop(i))
	
cat='\n'
code = cat.join(codeBlock)
print(code)
