while True:
    a=int(input('Enter the number to convert into roman : '))
    n=(1000,900,500,400,100,90,50,40,10,9,5,4,1)
    r=('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
    R=''
    for i in range (len(n)):
        c=int(a/n[i])
        R+=str(r[i])*c
        a-=n[i]*c
    print(R)
    if a=='':
        break
