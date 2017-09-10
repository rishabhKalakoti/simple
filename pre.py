"""
	This is the Pre-Processor for 'simple' language.
	The preprocessor has the following functions as of now:
	
	- remove comments from the program
	- remove empty lines, tabs, multiple spaces
	- import the code of the imported files // not designing yet
"""
import re

def preprocessor(code):
	# ------------ remove comments
	code = re.sub(r'#.*(\n)', "\n", code)
	# ------------ remove empty lines
	code = re.sub(r'\n+', "\n", code)
	code = code.strip()
	# ------------ remove tabs
	code = re.sub(r'\t+', "", code)
	# ------------ remove multi spaces
	code = re.sub(r' +', " ", code)
	return code
