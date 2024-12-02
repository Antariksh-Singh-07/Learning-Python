a=eval(input('Enter the list : '))
print(a)
b=int(input('Enter number to increment the list : '))
for i in range(len(a)):
    c=a[i]
    c+=b
    print('List after incremation :',(c))
