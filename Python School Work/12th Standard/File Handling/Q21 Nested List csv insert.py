import csv
lst = [['Name','Class','Stream'],['Antariksh','12th','Maths'],['idk this guy','21st','Drawing'],['idk this gal either','69th','Nursing']]
with open(r'.\Files Used\Nested List.csv','w',newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerows(lst)
with open(r'.\Files Used\Nested List.csv','r',newline='') as f:
    s = csv.reader(f,delimiter=',')
    for i in s: print(i)