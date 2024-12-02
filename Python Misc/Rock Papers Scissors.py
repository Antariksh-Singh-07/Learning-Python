import random 
yn='y'
while True :
    c=input("What will you choose r/p/s: ")
    choice=c.lower()
    l=["r","p","s"]
    pcchoice=random.choice(l)
    if choice==pcchoice:
        print('Draw !')
    elif (choice=='r' and pcchoice=='p') or (choice=='p' and pcchoice=='s') or (choice=='s' and pcchoice=='r'):
        print('You Lost hahahahaha !')
    elif (choice=='r' and pcchoice=='s') or (choice=='p' and pcchoice=='r') or (choice=='s' and pcchoice=='p'):
        print('You won !')
    else:
        print('Invalid Input')
    yn=input("Do you wanna play another game [y/n]: ")
    if yn.lower()=='y':
        continue
    else:
        break