file_1 = input("Enter file name to copy from: ")
file_2 = input("Enter file name to append to: ")
f1 = open(f".\\Files Used\\{file_1}",'r')
f2 = open(f".\\Files Used\\{file_2}",'a')
s1 = f1.read()
s2 = f2.write(s1)