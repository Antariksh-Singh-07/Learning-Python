def min_num(x,y):
    if int(x[-1])<int(y[-1]):
        return x
    else:
        return y
    
x = input("Enter a number x:")
y = input("Enter a number y:")
print(f"The number with smallest once digit is {min_num(x,y)}")