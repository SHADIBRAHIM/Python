class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        b=2*(self.length+self.breadth)
        return b
a=int(input("Enter length of rectangle1: "))
b=int(input("Enter breadth of rectangle1: "))
obj=rectangle(a,b)
print("Area of rectangle1:",obj.area())
print("Perimeter of rectangle1: ",obj.perimeter())
print("-------------------------------------")
c=int(input("Enter length of rectangle2: "))
d=int(input("Enter breadth of rectangle2: "))
obj1=rectangle(c,d)
print("Area of rectangle2:",obj1.area())
print("Perimeter of rectangle2: ",obj1.perimeter())
print("-------------------------------------")
if obj.area()==obj1.area():
    print("Both rectangles have same area")
elif obj.area()>obj1.area():
    print("Reactangle 1 have bigger area")
else:
    print("Rectangle 2 have bigger area")

