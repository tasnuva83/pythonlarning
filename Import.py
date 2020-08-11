try:
    import dictionary_1
except ImportError as error:
    print('data not found')

print('after exception')
print(dictionary_1.persons)
print(dictionary_1.d)
print(dictionary_1.d2)


try:
    from dictionary_1 import d, d2

except ImportError as error:
    print('data not found')

print(d)
print(d2['russia'])

try:
    from dictionary_1 import d as d_alt, d2 as d2_alt
except ImportError as error:
    print('data not found')

d = {'verena': 'germany', 'laura': 'columbia', 'daria': 'russia'}
print(d_alt)
print(d)
print(dictionary_1.__file__)
