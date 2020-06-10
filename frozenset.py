cities=set()
cities={"krakaw", "warsaw", "vilnius", "riga"}
print(cities)
cities.add("oslo")
print(cities)
cities=frozenset(['riga', 'warsaw', 'vilnius', 'oslo', 'krakaw'])
print(cities)
cities.add("stolkholm")