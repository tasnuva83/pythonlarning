fp=open("new_textappend.txt",'a')
lines=["\njava is another one", "\njava is also good"]
output=fp.writelines(lines)
print(output)
