a=int(input("Enter the 1st side: "))
b=int(input("Enter the 2nd side: "))
c=int(input("Enter the 3rd side: "))
if a==b==c:
    print("The triangle is equilateral")
elif a==b or b==c or c==a:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")