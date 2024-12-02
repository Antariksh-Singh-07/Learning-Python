f = open(r".\Files Used\phno.txt",'r')
s = f.readlines()
for i in s:
    z = i.split()
    print(f"→ {z[0].ljust(9)} | {z[1]}",end="\n")