try:
    fp=open("to read python.txt","r")
    s=fp.read()
    print(s)
except FileNotFoundError as error:
    print('Error: file not found')
print('after exception')

try:
    import to_read
except ImportError as error:
    print('data not fount')
print('after exception')