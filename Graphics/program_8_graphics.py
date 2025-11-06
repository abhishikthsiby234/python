import Graphics
from Graphics import circle,rectangle
from Graphics.threeDGraphics import cuboid,sphere
from Graphics.circle import *
rad1=float(input("enter the radius of the circle:"))
print("Area of circle is:",circle,area_circle(rad1))
print("perimeter of circle:",circle.perimeter_circle(rad1))
len1=float(input("enter the length of rectangle:"))
bredth1=float(input("enter the breadth of rectangle:"))
print("area of rectangle is:",rectangle.area_rec(len1,bredth1))
print("perimeter of rectangle is:",rectangle.perimeter_rec(len1,bredth1))
len2=float(input("enter the length of the cuboid:"))
bredth2=float(input("enter the bredth of the cuboid:"))
heigth=float(input("enter the height of cuboid:"))
print("perimeter of cuboid is:",cuboid.perimeter_cuboid(len2,bredth2,heigth))
rad2=float(input("enter the radius of sphere:"))
print("area of sphere is:",sphere.area_sphere(rad2))
print("perimeter of sphere is:",sphere.perimeter_sphere(rad2))
