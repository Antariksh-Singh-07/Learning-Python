a=input("print 1st or 2nd series [i/ii]: ")
if a.lower()=='i':
    for i in range(1,41,3):
        print(i,end=(' '))
elif a.lower()=='ii':
    b=1
    for i in range(1,41,3):
        print(i*b,end=(' '))
        b=b*-1