f = open(r".\Files Used\Article.txt", "r")
s = f.read()
up = low = space = spc = 0
for i in range(len(s)):
    if s[i].isupper():
        up += 1
    elif s[i].islower():
        low += 1
    elif s[i].isspace():
        space += 1
    else:
        spc += 1
print(
    f"The Number of Occurances everthing had is: \nUpper: {up} \nLower: {low} \nSpace: {space} \nSpecial:  {spc}"
)
