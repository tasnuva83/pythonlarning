persons=["verena", "paula", "daria"]
countries=["germany","columbia","russia"]
data={"verena":"germany","paula":"columbia","daria":"russia"}
data['jelena']='russia'
print(data)
data_2={"chia":"taiwan","ina":"indonasia"}
data.update(data_2)
print(data)
del data ["paula"]
print(data)
print("enter persons name:")
name=input()
if name in data.keys():
    print(data[name])
else:
    print("the name is not present in the data")
