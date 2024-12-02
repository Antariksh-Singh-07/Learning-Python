f = open(r".\Files Used\Article.txt", "r")
s = f.read()
s = s.lower()
x = ""
for i in range(len(s)):
    if s[i].isalpha():
        x += s[i]
    else:
        x += " "
the = to = 0
x = x.split()
print(
    f"here, \nThe appeared {x.count('the')} times & \nTo appeared {x.count('to')} Times"
)
