f = open(r".\Files Used\Story.txt",'r')
s = f.readlines()
x=0
for i in s:
    for j in i:
        if j == '$':
            print(x)
            exit()
    x+=1
print(x)