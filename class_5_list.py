class list:
    def __init__(self):
        self.name = ['adiy', 'tom','clara','artur','eric']

    def printlist(self):
        print(self.name)

    def length(self):
        print(len(self.name))

    def remove(self,x):
        self.name.remove(x)
        print('the new list after remove:', self.name)

    def append(self,x):
        self.name.append(x)
        print('the new list after adding:', self.name)

list1= list()
list1.printlist()
list1.length()
list1.remove('tom')
list1.append('paulina')

class list():

    def __init__(self):
        user_input= input('names are:')
        self.name= user_input.split()


    def printlist(self):
        print(self.name)

    def append(self,x):
        x = input('new name:')
        self.name.append(x)
        print('the new list after adding:', self.name)

    def remove(self,x):
        x = input('remove name:')
        self.name.remove(x)
        print('the new list after remove:', self.name)


list1= list()
list1.printlist()
list1.append('')
list1.remove('')