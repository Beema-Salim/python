class rectangle:
    def __init__(self,l,b):
      self._l1=l
      self._b2=b
    def area(self):
        area1=self._l1*self._b2
        return area1
    def __lt__(self,obj):
        if(self.area()<obj.area()):
            return "The area of Rectangle1 is less than Rectangle2"
        else:
            return "The area of Rectangle2 is less than Rectangle1"
print("Rectangle1")
l=int(input("Enter the length of rectangle1"))
b = int(input("Enter the breadth of rectangle1"))
obj1=rectangle(l,b)
print("The area is")
print(obj1.area())
print("Rectangle2")
l = int(input("Enter the length of rectangle2"))
b = int(input("Enter the breadth of rectangle2"))
obj2 = rectangle(l,b)
print("The area is")
print(obj2.area())
print("Now comparing the rectangles")
print(obj1<obj2)

