import csv
c= open("csv3.csv")
d = csv.reader(c)
for i in d:
    print('  '.join(i))