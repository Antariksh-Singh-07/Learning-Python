l=input('Enter Numbers: ')
print(list(l))
for i in range(len(l)):
    if l[i]==l[-i-1]:
        print("This is a palindrome")
        break
    else:
        print("This is NOT a palindrome")
        break