list1=[1,5,11,24]
list2=[2,13,28,32,43]
print("List1:",list1)
print("List2:",list2)
print("length of list1=",len(list1))
print("length of list2=",len(list2))
if len(list1)==len(list2):
    print("length of list are same")
else:
    print("length are not same")
    print("sum of list1=",sum(list1))
    print("sum of list2=",sum(list2))
if (sum(list1)==sum(list2)):
        print("sum of two list are same")
else:
        print("sum of list are not same")
        check=any(item in list1 for item in list2)
        print("any value occur in both:",check)
