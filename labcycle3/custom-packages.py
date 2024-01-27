from graphics.dgraphics import cuboid
from graphics import circle,rectangle
from labcycle3.graphics.dgraphics import sphere

print("circle")
r=int(input("enter the radius of circle: "))
circle.areac(r)
circle.peric(r)

print("Rectangle")
l=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
rectangle.arear(l,b)
rectangle.perir(l,b)

print("cuboid")
l=int(input("enter the length of cuboid"))
b=int(input("enter the breadth of cuboid"))
h=int(input("enter the height of cuboid"))
cuboid.areacub(l,b,h)
cuboid.pericub(l,b,h)

print("Sphere")
r=int(input("enter the radius of sphere: "))
sphere.areas(r)
sphere.peris(r)
