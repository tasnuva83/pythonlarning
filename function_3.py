def calculatevolume(length,width,height):
    volume=length*width*height
    print("the volume of the area is:", volume)
    return volume
v= calculatevolume(3,2,3)
print(v)
x=int(input("enter length:"))
y=int(input("enter width:"))
z=int(input("enter height:"))
output= calculatevolume(x,y,z)
print(output)