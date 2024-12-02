n=int(input("Enter number n>20 : "))
for i in range(11,n+1):
    print(i,end="\n")
    if i%3==0 and i%7==0:
        print("TipsyTopsy")
    elif i%7==0:
        print("Topsy")
    elif i%3==0:
        print("Tipsy")