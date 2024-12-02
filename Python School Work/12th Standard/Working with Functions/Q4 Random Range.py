from random import randrange

def rr(x,y):
    return (randrange(x,y+1))

inp_1 = int(input("Enter Range's 1st Value: "))
inp_2 = int(input("Enter Range's 2nd Value: "))

for i in range(0,3):
    print(rr(inp_1, inp_2))