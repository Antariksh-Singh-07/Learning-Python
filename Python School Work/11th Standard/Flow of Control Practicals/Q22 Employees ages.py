n=int(input("Enter the number of data to be taken: "))
x,y,z=0,0,0
for i in range(1,n+1):
     a=int(input("Enter the age of your nth employee: "))
     if 26<=a<=35:
          x+=1
     elif 36<=a<=45 :
          y+=1
     elif 46<=a<=55 :
          z+=1
print("Employees in age group 26-35: ",x)
print("Employees in age group 36-45: ",y)
print("Employees in age group 46-55: ",z)
print("Employees that don't lie in any group: ",n-(x+y+z))