from random import randrange
def Random_Number(n):
    a = 10**n
    b = 10**(n-1)
    num = randrange(b,a)
    return num

n = int(input("Input n: "))
print(Random_Number(n))