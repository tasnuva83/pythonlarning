list=[]
lower=int(input("enter the lower range:"))
upper=int(input("enter the upper range:"))
for x in range(lower, upper+1):
    if (x%7==0) and (x%5!=0):
        list.append(str(x))
print(','.join(list))
