a=input('Enter the formula : ')
c=0
for i in a:
    if i=='(':
        c+=1
    elif i==')':
        c-=1
if c==0:
    print('Formula has same no.of open & closed brackets : ')
else:
    print('Formula has unequal no.of open & closed brackets : ')
