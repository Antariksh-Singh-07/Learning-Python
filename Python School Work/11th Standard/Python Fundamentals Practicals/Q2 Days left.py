m=int(input('How many days are there in the current month ? : '))
if m < 28 or m > 31 :
    print('A month like that does not exists')
    exit()
d=int(input('what is the date today ? :'))
if d <= 0 or d > 31 :
    print('A date like that does not exists')
    exit()
else :
    print(m-d, 'days are left in the current month')