FileHandle=open("name.txt","r")
LINEOFTEXT=FileHandle.readline()
print
while len(LINEOFTEXT)>0:
    print(LINEOFTEXT)
    LINEOFTEXT=FileHandle.readline()
FileHandle.close()
