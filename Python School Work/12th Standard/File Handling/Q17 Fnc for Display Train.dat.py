import pickle
with open(r".\Files Used\train.dat","rb") as f:
    a = True
    while a==True:
        try:
            s = pickle.load(f)
            if s["To"] in "Delhi":
                print(s)
        except EOFError:
            a = False