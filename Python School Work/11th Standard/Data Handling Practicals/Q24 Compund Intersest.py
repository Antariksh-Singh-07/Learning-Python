#compound interest = p(1+r)^t
p=float(input('Enter Principal: '))
r=float(input('Enter Rate: '))
t=float(input('Enter Time: '))
c=p*(1+r/100)**t
print('Amount Payable:',c)