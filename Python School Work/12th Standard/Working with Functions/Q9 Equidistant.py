def equidistant(x,y):
    e = (y-x)/3
    e1, e2, e3, e4 = x, x+e, y-e, y
    return e1,e2,e3,e4
a = float(input("Enter First Number: "))
b = float(input("Enter Last Number: "))
print(equidistant(a,b))