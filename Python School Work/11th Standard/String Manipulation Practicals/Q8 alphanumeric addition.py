a=int(input('Enter your integer : '))
b=input('Enter the alphanumeric : ')
s=''
d=''
for i in b:
    if i.isdigit():
        s+=i
if s:
    d=int(s)
print(a,'+',d,'=',a+d)
