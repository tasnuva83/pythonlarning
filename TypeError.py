try:
   a = '10'
   b = 20
   c = a+b
   print(c)
except TypeError as error:
    print('TypeError exception occured ')
print('after exception')
