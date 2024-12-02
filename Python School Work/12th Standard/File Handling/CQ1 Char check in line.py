f1 = open(r".\Files Used\Article.txt", "r")
f2 = open(r".\Files Used\Lines with a.txt", "w")
s = f1.readlines()
for i in range(len(s)):
    if "a" in (s[i].lower()):
        f2.write(s[i])
