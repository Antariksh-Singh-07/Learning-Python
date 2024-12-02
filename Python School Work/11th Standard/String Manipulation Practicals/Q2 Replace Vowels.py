a=input('Enter  the string : ')
b=''
for i in a :
    l=i.lower()
    if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':
        b+='*'
    else :
        b+=i
print(b)