# Shows the top (n) no. of repeated digits
from random import randint
lst = [randint(1,10) for i in range(50)]
print(f"list = {lst}")
set = set(lst)
occured = []
for i in set:
    var = lst.count(i)
    occured.append(float(f"{var}.{i}"))
occured.sort(reverse=True)
occured = [str(i) for i in occured]
n = 3
for i in range(n):
    num = int((occured[i].split("."))[1])
    occurance = int((occured[i].split("."))[0])
    print(f"{i+1} rank = {num} : occured {occurance} times")