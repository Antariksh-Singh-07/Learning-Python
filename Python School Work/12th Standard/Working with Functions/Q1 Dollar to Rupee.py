def conv_void(d,c):
    print(f"{d} Dollars will be {d*c} Rupees !")
def conv_non_void(d,c):
    return (d*c)

d = float(input("Enter amount in Dollars: "))
c = float(input("How much rupees is worth 1 Dollar: "))
conv_void(d,c)
print(f"{d} Dollars will be {conv_non_void(d,c)} Rupees !")