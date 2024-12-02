a=input("Enter your sentence:")
b=a.split()
c=len(a)
print('The number of words are:',len(b))
print('The number of characters are:',c)
d=0
for i in a:
    if i.isalnum():
        d+=1
p=(d/c)*100
print('Percentage of Alphanum is:',p,'%')