import pickle
with open(r".\Files Used\Company.dat","rb") as f:
    a = True
    while a==True:
        try:
            s = pickle.load(f)
            if s['CompID'] == 1005:
                print(s)
        except EOFError:
            a = False