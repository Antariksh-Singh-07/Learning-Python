def countLETTER(a):
    f = open(r".\Files Used\Article.txt", "r")
    s = (f.read()).lower()
    print(f"{a} appeared {s.count(a)} time(s) throughout the text.")

a = input("Which letter to count ?: ").lower()
countLETTER(a)
