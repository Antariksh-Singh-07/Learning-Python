f = open(r".\Files Used\STRS.txt",'w')
a = 'y'
x = 0
while a == 'y':
    x +=1
    n = input(f"Enter Line {x}: ")
    f.write(n)
    a = input("Do you want to continue (y/n): ")
    f.write('\n')
f.close()
