f1 = open(r".\Files Used\Poem.txt", "r")
f2 = open(r".\Files Used\Lines Check.txt", "w")
s = f1.readlines()
n = input("Enter the alphabet you want to check at the start of the line: ").lower()
x=0
for i in s:
    a = i.lower()
    if a[0] == n:
        x+=1
        f2.write(i)
print(f"The no. of times {n} appeared in the text = {x}")