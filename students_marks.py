print("marks obtainen in Math:")
math=input()
print("marks obtained in Physics:")
phy=input()
print("marks obtained in Chemistry:")
che=input()
print("marks obtained in Biology:")
bio=input()
print("marks obtained in Literature:")
lit=input()
if math>='60' and phy>='60' and che>='60' and bio>='60' and lit>='60':
    print("first division")
elif math>='50' and phy>='50' and che>='50' and bio>='50' and lit>='50':
    print("second division")
elif math>='40' and phy>='40' and che>='40' and bio>='40' and lit>='40':
    print("third division")
else:
    print("fail")
