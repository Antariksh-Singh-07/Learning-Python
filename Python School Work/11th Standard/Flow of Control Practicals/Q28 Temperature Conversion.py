a=float(input('Enter the Temperature: '))
x=input('Is the Temperature in Celcius or Fahrenheit [C/F]: ')
if x.lower()=='c':
    t=((a*9)/5)+32
else:
    t=((a-32)/9)*5
print("The temperature in the other unit is:",t)