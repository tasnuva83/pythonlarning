try:
    class circle:
        def __init__(self, r):
            radius = r

        def area(self):
            pi = 3.14
            pi * self.radius ** 2
            print('area:', pi * self.radius ** 2)

    circle1=circle(3)
    circle1.area()
except AttributeError as error:
    print('AttributeError occured')
print('after exception')

