def TZeros(x):
    fact,zeros,y = x,0,10
    while x>1:
        fact*=x-1
        x-=1
    while fact%y == 0:
        zeros += 1
        y *=10
    return zeros
num = int(input("Enter the number whose factorial's trailing zero count you wish for: "))
print(f"The number of trailing zeros of {num}! is {TZeros(num)}")