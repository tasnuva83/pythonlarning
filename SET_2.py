s1=set([7,9,12,7,9])
s2=set(['abc',12,'b','car',7,10,12])
s3=set([12,14,12,'ab'])
s=s1^s2^s3
print(s)
print(s1.issubset (s))
print(s2.issubset (s))
print(s3.issubset (s))