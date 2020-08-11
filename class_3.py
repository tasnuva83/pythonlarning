class rectangle:
    count = 0
    def __init__(self,x,y):
        self.length = x
        self. width = y

        rectangle.count+=1
    def width(self):
        print('Width:', self.width)
    def length(self):
        print('Length:', self.length)
    def area(self):
        self.length*self.width
        print('Area:', self.length*self.width)
        print('found Area', rectangle.count)
    def compare(self):
        if self.length==self.width:
            print('Not a rectangle')
        else:
            print('Its a rectangle')
    def compare2(self,x):
        if self.length==x.length:
            print('both parameter is same')
        else:
            print('parameter is not same')


rectangle1=rectangle(10,20)
rectangle1.area()
rectangle1.compare()

rectangle2=rectangle(15,10)
rectangle2.area()
rectangle2.compare()

rectangle1.compare2(rectangle2)

rectangle3=rectangle(15,15)
rectangle3.area()
rectangle3.compare()

rectangle2.compare2(rectangle3)