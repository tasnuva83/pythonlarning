s1=set([7,9,12,7,9])
s2=set(['abc',12,'b','car',7,10,12])
s3=set([12,14,12,'ab'])

def output():
    print(s1)
    print(s2)
output()

def output_1():
    print(s1|s2)
output_1()

def output_2():
    print('b' in s1)
    print('abc' in s2)
    print('ab' in s3)
output_2()

def output_3():
    s2.discard(12)
    print(s2)
print(s2)
output_3()


