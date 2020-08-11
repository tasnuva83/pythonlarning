
import sys
print("This is commandline program execution")
print(sys.version)
program_name = sys.argv[0]
print("sys.argv is:", sys.argv)
st=sys.argv[1]
print('the string:',st.capitalize())
st2=sys.argv[2]
print('the 2nd string:',st2.capitalize())
st3=sys.argv[3]
st4=sys.argv[4]
d= {st:st2, st3:st4}
print(d)