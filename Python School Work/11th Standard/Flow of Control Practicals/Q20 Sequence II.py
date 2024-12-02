x=int(input("print which sequence sum shall be printed [1/2]: "))
if x==1:
    a=2
    b=9
    c=1
    e=0
    for i in range(7):
            d=a/b
            e+=(d*c)
            a+=3
            b+=4
            c*=-1
    print("Sum of the sequence is",e)
elif x==2:
    n=int(input("Enter value of n: "))
    e=0
    for i in range(1,n+1,2):
        e=e+i**2
    print("Sum of the sequence is",e)
else:
    print('Wrong initial Input !')