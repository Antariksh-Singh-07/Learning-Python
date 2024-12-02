import pickle
from random import randint as ri
def AddStudent():
    with open(r".\Files Used\Students.dat",'ab') as f:
        k={}
        a=input('Do you want to Input data (y/n): ').lower()
        if a == 'y':
            while a == 'y':
                n=input("Name: ")
                r=int(input("Roll no.: "))
                p= int(input("Phy Marks: "))
                c= int(input("Chem Marks: "))
                m= int(input("Maths Marks: "))
                cs= int(input("CS Marks: "))
                e= int(input("Eng Marks: "))
                k["Name"],k["Roll"],k["Phys"],k["Chem"],k["Maths"],k["Cs"],k["Eng"] = n,r,p,c,m,cs,e
                pickle.dump(k,f)
                a=input('Do you want to continue the Inputs (y/n): ').lower()
        else:
            pass
def GetStudent():
    with open(r".\Files Used\Students.dat",'rb') as f:
        a=True
        x,y=-1,0
        while a==True:
            try:
                x+=1
                k=pickle.load(f)
                p=(k["Phys"]+k["Chem"]+k["Maths"]+k["Cs"]+k["Eng"])/5
                if p<76:
                    y+=1
                else:
                    print(f'{k["Name"]} got {p}%')
            except EOFError:
                print()
                a=False
        if x == y:
            print("No one Scored more than 75%, what a shame lol!")
        f.close()
AddStudent()
GetStudent()