# 3. Testing of OOP programmes
#  code below are from geom.py
# geometry module: geom.py
from cmath import rect


class Rectangle: # rectangle class
    # make a rectangle using top left and bottom right coordinates
    def __init__(self,tl,br):
        self.tl=tl
        self.br=br
        self.width=abs(tl.x-br.x)  # width
        self.height=abs(tl.y-br.y) # height

    def area(self): # gets area of rectangle
        return self.width*self.height


class Coordinate: # coordinate class
     def __init__(self,x,y):
        # make coordinate obj with a reference (self), an x and a y
        self.x=x
        self.y=y


     def distance(self,another): # distance between 2 coordinates
        import math
        xdist=abs(self.x-another.x)
        ydist=abs(self.y-another.y)
        return math.sqrt(xdist**2+ydist**2) # pythagoras theorem


# test function for distance between coordinates
def test_function():
    print("="*20, "Testing coordinate distance method", "="*20)
    coors_1 = Coordinate(3, 4)
    coors_2 = Coordinate(5, 7)
    actual = coors_1.distance(coors_2)
    print("Distance of between Coordinate of point(x = 3 and y = 4 ) and Coordinate of point(x = 5 and y = 7) is expected to be 3.605551275463989 ")
    print("actual result %s \n \n" % actual)
    print("="*20, "Testing rectangle area method ", "="*20)
    rectangle = Rectangle(coors_1, coors_2)
    area = rectangle.area()
    print("Area of rectangle of created with Coordinate of point(x = 3 and y = 4 ) and Coordinate of point(x = 5 and y = 7) is expected to be 6")
    print("actual result %s \n \n" % area)


test_function()