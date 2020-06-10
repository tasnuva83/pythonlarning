string=input("enter sring:")
l=string.split()
print(l)
dic={}
for i in l:
    if i not in dic.keys():
        dic[i]=0
    dic[i]=dic[i]+1
print(dic)
