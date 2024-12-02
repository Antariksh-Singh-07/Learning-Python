s1=input('Enter first string : ')
s2=input('Enter second string : ')
small=s1
large=s2
if len(s1)>len(s2):
    large=s1
    small=s2
print(small)
l=len(large)
for i in range (l//2):
    print(' '*(i),large[i],' '*(l-i),large[l-i-1])
