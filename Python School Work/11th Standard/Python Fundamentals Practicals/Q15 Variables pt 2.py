x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter 3rd number: "))
print("The three numbers :", x,y,z)
x,y = x+y, y+z
print("After swapping :", x,y)
