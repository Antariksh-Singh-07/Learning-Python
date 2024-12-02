p = float(input("Enter principal : "))
r = float(input("Enter rate : "))
t = float(input("Enter time : "))
s = (p*r*t) / 100
c = p*((1+(r/100))**t)-p
print("Simple interest = ", s)
print("Compound interest = ", c)