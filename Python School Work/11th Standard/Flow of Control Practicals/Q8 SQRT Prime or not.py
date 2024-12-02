import math
n=int(input("Enter a number: "))
s=int(math.sqrt(n))
flag=True
if s>1:
    for i in range(2,s):
        if s%i==0:
            flag=False
            break
    if flag==False:
        print(n,"square root isn't prime")
    else:
        print(n,"sqaure root is prime")   
else:
    print(n,"sqaure root isn't prime")