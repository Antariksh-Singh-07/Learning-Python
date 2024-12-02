a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))
if a>b and a>c:
    l=a
    if b>c:
        m=b
        s=c
    elif c>b:
        m=c
        s=b
elif b>a and b>c:
    l=b
    if a>c:
        m=a
        s=c
    elif c>a:
        m=c
        s=a
elif c>b and c>a:
    l=c
    if b>a:
        m=b
        s=a
    elif a>b:
        m=a
        s=b
print("Largest:",l)
print("Middle:",m)
print("Smallest:",s)