import pickle
fin = open(r".\Files Used\sports.dat",'rb')
fout = open(r".\Files Used\Athletes.txt",'w')
a=True
while a==True:
    try:
        s=pickle.load(fin)
        if s[0]=='Athletics':
            fout.write(s)
    except EOFError:
        print("End of File")
        a=False