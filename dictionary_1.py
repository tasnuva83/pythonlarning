persons=["verena", "paula", "daria"]
countries=["germany","columbia","russia","maxico"]
d={}
y=0
for x in persons:
    d[x]=countries[y]
    y=y+1
print(d)
for key,value in d.items():
    print(key, value)
countries_person=zip(countries, persons)
print(countries_person)
d2=dict(countries_person)
print(d2)
for key,value in d2.items():
    print(key,value)