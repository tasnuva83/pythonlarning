string=input("enter sring:")
words=string.split()
print(words)
dic={}
for i in words:
    alphabet = i[0]
    if alphabet not in dic:
        dic[alphabet]=[]
    dic[alphabet].append(i)

print(dic)