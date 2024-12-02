import pickle

k = []


def CreateFile():
    with open(r".\Files Used\Book.dat", "wb") as f:
        n = int(input("How Many Inputs:"))
        for i in range(n):
            BNo = input("Book No.: ")
            BNa = input("Book Name: ")
            BAu = input("Book Author: ")
            BPr = input("Book Price: ")
            k.append(BNo)
            k.append(BNa)
            k.append(BAu)
            k.append(BPr)
            pickle.dump(k, f)


def CountRec(Author):
    with open(r".\Files Used\Book.dat", "rb") as f:
        a = True
        x = 0
        while a == True:
            try:
                s = pickle.load(f)
                if s[2] == Author:
                    x += 1
            except EOFError:
                a = False
    return x


CreateFile()
print(f"The no. of Books by the author given is: {CountRec('Sumita Arora')}")
