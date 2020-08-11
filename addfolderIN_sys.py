import sys

a = sys.path
print(a)
my_path = 'C:\\Users\\49176\\Python-code-master'
if my_path not in a:
    sys.path.append(my_path)
else:
    print('no need to add path')

print(a)


