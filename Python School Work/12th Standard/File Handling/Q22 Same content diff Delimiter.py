import csv
def Copy():
    r = csv.reader(open(r".\Files Used\train.csv","r",newline=""), delimiter=",")
    w = csv.writer(open(r".\Files Used\train[e].csv","w",newline=""), delimiter="$")
    w.writerows(r)