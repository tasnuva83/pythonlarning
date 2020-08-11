class mobile():
    type='android'
    brand='samsung'
    color='gray'
    def mob_production(self):
        print("starting mobile production")
    def printdetails(self):
        print(self.type,self.color,self.brand)
x1= mobile()
print(x1)
x1.mob_production()
print(x1.type)
print(x1.brand)
print(x1.color)
x1.printdetails()

x2= mobile()
x2.color='white'
print(x2.type)
print(x2.brand)
print(x2.color)
x2.printdetails()