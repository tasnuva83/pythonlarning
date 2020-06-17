list=[23,24,25,26,24,24]
def length(l):
    print(l)
    print(len(l))
length(list)

def countoccurence(x):
    print(list.count(x))
countoccurence(24)
countoccurence(25)

def removelement(x):
    print(list.remove(x))
    print("after remove the list:", list)
removelement(25)
removelement(23)

def copy_list():
    print(list)
    print(list.copy())
copy_list()


