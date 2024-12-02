low = open(r".\Files Used\Lower.txt", "w")
up = open(r".\Files Used\Upper.txt", "w")
space = open(r".\Files Used\Space.txt", "w")
spc = open(r".\Files Used\Special.txt", "w")
l = ["y", "yes", "yup"]
q = "y"
while q in l:
    s = input("Input any string: ")
    for i in range(len(s)):
        if s[i].isupper():
            up.write(s[i])
        elif s[i].islower():
            low.write(s[i])
        elif s[i].isspace():
            space.write(s[i])
        else:
            spc.write(s[i])
    q = input("Want to continue Inputs?: ").lower()
