import sys
print("This is commandline program execution")
print(sys.version)
program_name = sys.argv[0]
print("sys.argv is:", sys.argv)
s=sys.argv[1]
print('reverse of the string:',s[::-1])





