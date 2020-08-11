try:
    info = {'name': 'elee', 'country': 'serbia', 'age': 22}
    print(info['nam'])
except KeyError as error:
    print('KeyError exception occured')
print('after exception')

