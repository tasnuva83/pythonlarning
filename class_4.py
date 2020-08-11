class circle:
    def __init__(self,r):
        self.radius=r
        print('this is a circle')


    def area(self):
        pi=3.14
        pi*self.radius**2
        print('area:',pi*self.radius**2)
    def perimeter(self):
        pi = 3.14
        2*pi*self.radius
        print('perimeter:',2*pi*self.radius)

circle1=circle(3)
circle1.area()
circle1.perimeter()