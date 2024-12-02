while True :
    s=input('Enter the sentences [Typing q will break the chain]: ')
    n=''
    if s.lower()=='q' :
        break
    for i in s :
        if i.islower()==True :
            n+=i.upper()
        elif i.isupper()==True :
            n+=i.lower()
        else :
            n+=i
    print(n)
