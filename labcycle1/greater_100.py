n=int(input("enter the number of values:"))
a=[]
for i in range(0,n):
    value=int(input("enter the value:"))
    if value>100:
        a.append("over")
    else:
        a.append("value")
print(a)