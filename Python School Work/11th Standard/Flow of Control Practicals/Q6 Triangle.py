a=float(input('Enter 1st side of a Triangle:'))
b=float(input('Enter 2nd side of a Triangle:'))
c=float(input('Enter 3rd side of a Triangle:'))
if a+b>c and b+c>a and c+a>b:
    print('Those sides will form a Triangle !')
else:
    print('Those sides will not form a Triangle')