a=str(input("Enter a string : "))
firstchar = a[0]
a= a.replace(firstchar, '$')
print(firstchar+a[1:])
