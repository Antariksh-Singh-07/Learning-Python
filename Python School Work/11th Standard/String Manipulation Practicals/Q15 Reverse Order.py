a=input("Enter a String to be reversed: ")
b=a.split()
c=""
for i in range(len(b)):
    c=(b[i])[-1::-1]
    print(c,end=' ')