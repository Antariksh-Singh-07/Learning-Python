n=int(input('Enter a single digit number smaller than 8: '))
if n > 7:
    print('Enter a number smalled than 8')
    exit()
print(n*100+(n+1)*10+n+2)