n=int(input("Enter a number to input: "))
m=int(input("Enter a number to divide: "))
for i in range(1,n+1):
    if i%m==0 and i%2==0:
        print(i, "is even number")
    elif i%m==0 and i%2!=0:
        print(i, "is odd number")