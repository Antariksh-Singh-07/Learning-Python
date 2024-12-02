#simple interest = prt/100
#amount payable = p + simple interest
p=float(input('Enter Principal: '))
r=float(input('Enter Rate: '))
t=float(input('Enter Time: '))
s=(p*r*t)/100
a=p+s
print('Payable Amount:',a)