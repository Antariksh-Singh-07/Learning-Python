c=int(input("Enter how many Items you bought: "))
if c<10:
    print("Total cost =", c*120)
elif c<100:
    print("Total cost =", c*100)
else:
    print("Total cost =", c*70)