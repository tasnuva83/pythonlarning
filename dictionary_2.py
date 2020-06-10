persons=["verena", "paula", "daria"]
countries=["germany","columbia","russia"]
data={"verena":"germany","paula":"columbia","daria":"russia"}
copy_data={}
for i in data:
    copy_data[data[i]]= i

print(copy_data)
inverse=dict()
for key in data:
    val=data[key]
    if val not in inverse:
        inverse[val]=key

print(inverse)
