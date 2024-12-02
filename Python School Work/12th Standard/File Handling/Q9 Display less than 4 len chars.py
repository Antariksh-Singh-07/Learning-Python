def DisplayWords():
    with open(r".\Files Used\Story.txt", "r") as f:
        s = f.readlines()
        for i in s:
            a = i.split()
            for j in a:
                if len(j) < 4:
                    print(j, end=" ")


DisplayWords()
