c=float(input("Enter temperature in Celcius: "))
if c>100:
    print("The temperature is above the boiling point")
elif c==100:
    print("The temperature is at the boiling point")
elif 100>c>0:
    print("The temperature is in the normal range")
elif c==0:
    print("The temperature is at the freezing point")
elif 0>c>-273.15:
    print("The temperature is below the freezing point")
elif c==-273.15:
    print("The temperature is absolute zero")
else:
    print("The temperature is invalid because it's below absolute zero")