a=input('Enter the string : ')
d=0
b=''
for i in a:
    if i.isdigit():
        b+=i
        d+=int(i)
if not b:
    print(a,"doesn't contain any digit ")
else:
    print(a,"has the digits",b,"which sum to",d)
