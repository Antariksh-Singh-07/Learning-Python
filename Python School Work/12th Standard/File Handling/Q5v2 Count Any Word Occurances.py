def countWORD(a):
    f = open(r".\Files Used\Article.txt", "r")
    s = (f.read()).lower()
    x = ""
    for i in range(len(s)):
        if s[i].isalpha():
            x += s[i]
        else:
            x += " "
    x = x.split()
    print(f"{a.title()} appeared {x.count(a.lower())} time(s) throughout the text.")

a = input("Which word to count ?: ")
countWORD(a)
