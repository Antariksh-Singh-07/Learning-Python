a=eval(input('Enter the list containing any number between 1-12 : '))
for i in range (len(a)):
    c=a[i]
    if a[i]>10:
        c=10
    print(c,end=',')
