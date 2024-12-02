import pickle
with open(r".\Files Used\staff.dat","rb") as f:
    a = True
    while a==True:
        try:
            s = pickle.load(f)
            if s["Staff Code"] == "S0105":
                print(s)
        except EOFError:
            a = False