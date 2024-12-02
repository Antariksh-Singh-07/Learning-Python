import pickle
k = {}
with open(r".\Files Used\member.dat","wb") as f:
    n = int(input("How many Inputs: "))
    for i in range(n):
        mno = int(input("Member No.: "))
        mn = input("Member Name: ")
        k['MemberNo.'],k['Name']=mno,mn
        pickle.dump(k,f)
