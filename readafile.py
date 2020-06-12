fp=open("to read in python.txt","r")
s=fp.read()
print(s)
fp.close()

fp=open("to read in python.txt","r")
s1=fp.read(20)
print(s1)

string=s
l=string.split()
print(l)
print("number of words in the file:" , len(l))
dic={}
for i in l:
    if i not in dic.keys():
        dic[i]=0
    dic[i]=dic[i]+1
print(dic)



