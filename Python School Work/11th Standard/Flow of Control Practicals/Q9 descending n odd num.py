a=int(input("Enter n: "))
if a%2==0:
    for i in range(a-1,0,-2) :
        print(i, end=" ")
else:
    for i in range(a,0,-2) :
        print(i, end=" ")