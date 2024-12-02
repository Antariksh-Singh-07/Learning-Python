a=input('Enter the string : ')
b=a.split()
c=''
for i in b:
    if len(i)>len(c):
        c=i
print(c)