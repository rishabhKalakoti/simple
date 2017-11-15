import re
f=open("code.c", "r").read()
f=re.sub(r'\t', "",f)
l=f.split("\n")
arr=[]
arr1=dict()

dType=["int","char","float"]
for x in l:
    #print(x)
    s=re.search(r'([a-zA-Z]+) ([a-zA-Z]+)\[(.*)\]\;',x)
    if(s!=None):
        if(s.group(1) in dType):
            arr.append([s.group(2),s.group(3),s.group(1)])
            N=int(s.group(3))
        else:
            print("Unspecified Type")
            exit(-1)
    else:
        r=re.search(r'([a-zA-Z]+)\[(.*)\]\=(.*)\;',x)
        if(r!=None):
            for i in range(len(arr)):
                if r.group(1) == arr[i][0]:
                    if(int(r.group(2))>=int(arr[i][1])):
                        print("Array index out of bound")
                        exit(-1)
                    exp=r.group(3)
                    if arr[i][2]=="int":
                        if (re.match(r'[0-9]+$',exp.strip())==None):
                            print("Type mismatch error")
                            exit(-1)
                        
                    elif arr[i][2]=="char":
                        if (re.match(r"\'[a-zA-Z1-9_]\'$",exp.strip())==None):
                            print("Type mismatch error")
                            exit(-1)
                        
                    elif arr[i][2]=="float":
                        if (re.match(r'[0-9]+\.[0-9]+$',exp.strip())==None):
                            print("Type mismatch error")
                            exit(-1)
                        
                    arr1[r.group(2)]=exp
print("Input 0 for entering index else any to exit")
ch=str(input())
while(ch=='0'):
    print("input index")
    a=int(input())
    if a>=N:
        print("Array out of index")
    elif a in arr1:
        print("Value:", arr1[str(a)])
    else:
        print("No value assigned")
    print("Input 0 for entering index else any to exit")
    ch=str(input())
print("All Good!")
print(arr1)
#print(arr)
