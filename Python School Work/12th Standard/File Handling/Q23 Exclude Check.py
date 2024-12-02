import csv
with open(r".\Files Used\Poems.csv","r",newline="") as f, open(r".\Files Used\Poems[e].csv","w",newline="") as fn:
    s = csv.reader(f)
    sn = csv.writer(fn)
    for i in s:
        if (i[0]).lower() == 'check':
            pass
        else:
            sn.writerow(i)