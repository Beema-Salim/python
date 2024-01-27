import csv
c=open("csv3.csv")
d=csv.DictReader(c)
print("name and course")
for i in d:
    print(i['Student'],i['Course'])