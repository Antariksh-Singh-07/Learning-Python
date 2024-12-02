y=int(input("Enter a Year :"))
if (y%400!=0 and y%100==0):
    print('This is not a Leap Year!')
elif (y%4==0 or y%400==0):
    print('This is a Leap Year !')
else:
    print('This is not a Leap Year!')