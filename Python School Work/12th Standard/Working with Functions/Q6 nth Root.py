def nthRoot(x,n=2):
    sol = x ** 1/n
    return sol

x = float(input("Enter the term x: "))
n = float(input("Enter the term n: "))
print(nthRoot(x,n))