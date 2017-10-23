parser.tab.c parser.tab.h: parser.y
	bison -d parser.y

lex.yy.c: lex.l parser.tab.h
	flex lex.l

out: lex.yy.c parser.tab.c parser.tab.h
	gcc parser.tab.c lex.yy.c -lfl -o out
