class mobile:
    count=0
    def __init__(self, x,y,z):
        self.model =x
        self.color =y
        self.price =z
        mobile.count+=1
    def displaymodel(self):
        print('model:', self.model)
    def printdetails(self):
        print('Price:', self.price,'Color:', self.color,'Model:', self.model)
    def increasedprice(self):
        self.price+=100
        print('increased price:', self.price)
    def __str__(self):
        return 'model displaying:' +self.model
mobile1= mobile('Galaxy 7','white',800)
mobile1.displaymodel()
mobile1.printdetails()
print('Display code:', mobile.count)
mobile1.increasedprice()
print(mobile1)
mobile2= mobile('Galaxy note8','black',1200)
mobile2.displaymodel()
mobile2.printdetails()
print('Display code:', mobile.count)
mobile2.increasedprice()
print(mobile2)
mobile3= mobile('Galaxy 6','black',500)
mobile3.displaymodel()
mobile3.printdetails()
print('Display code:', mobile.count)
mobile3.increasedprice()
print(mobile3)