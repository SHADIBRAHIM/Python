from graphics.rect import *
from graphics.circle import *
from graphics.dgraphics.sphere import *
from graphics.dgraphics.cuboid import *

print("RECTANGLE")
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle:"))
print("Area of reactangle:",rectarea(l,b))
print("Perimeter of rectangle:",rectperimeter(l,b))
print("--------------------------------")

print("CIRCLE")
r=int(input("Enter radius of the circle: "))
print("Area of circle: ",cirarea(r))
print("Perimeter of circle: ",cirperimeter(r))
print("--------------------------------")

print("SPHERE")
r=int(input("Enter radius of the sphere:"))
print("Area of sphere: ",spharea(r))
print("Perimeter of sphere: ",sphperimeter(r))
print("--------------------------------")

print("CUBOID")
l=int(input("Enter length of cuboid: "))
w=int(input("Enter width of cuboid: "))
h=int(input("Enter height of cuboid: "))
print("Area of cuboid: ",cubarea(l,w,h))
print("Perimeter of cuboid: ",cubperimeter(l,w,h))
print("--------------------------------")

