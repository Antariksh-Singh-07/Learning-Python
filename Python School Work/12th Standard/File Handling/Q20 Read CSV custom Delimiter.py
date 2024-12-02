import csv
with open(r".\Files Used\train.csv","r",newline="") as f:
    s = csv.reader(f,  delimiter="\t")
    for i in s:
        print(i)