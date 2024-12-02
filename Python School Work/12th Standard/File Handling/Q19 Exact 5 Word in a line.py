def Show_Words():
    with open(r".\Files Used\NOTES.txt","r+") as f:
        s = f.readlines()
        for i in s:
            x = i.split()
            l = len(x)
            if l == 5:
                print(i)
Show_Words()