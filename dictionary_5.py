price = {'bread':2, 'apple':5, 'milk':3, 'benana':2}
total=sum(price.values())
print("the total sum of values is :",total)
m_price=1
for i in price:
    m_price=m_price*price[i]
print("the multiplication of values is:", m_price)
