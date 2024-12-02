h = int(input("Enter hour between 1-12 : "))
a = int(input("How many hours ahead : "))
i = h + a
if i > 12:
    i-=12
print("Time at that time would be", i, "o'clock")