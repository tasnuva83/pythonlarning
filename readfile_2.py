with open("to read in python.txt","r") as fp:
    for i in fp:
        print(i)

fp=open("to read in python.txt","r")
s=fp.readlines()
print(s)
print(s[0:2])
print(s[-1])
print(s[-3:7])
print(len(s))

