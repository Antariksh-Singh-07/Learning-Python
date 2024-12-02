a=input('Enter any digit: ')
list(a)
if a[-1]==4:
    print("ends with 4")
elif a[-1]==8:
    print("ends with 8")
else:
    print("ends with neither")

#Alternative Method
str(a)
if a.endswith('4')==True:
    print("ends with 4")
elif a.endswith("8")==True:
    print("ends with 8")
else:
    print("ends with neither")