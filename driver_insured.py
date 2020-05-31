print("enter your name:")
name=input()
print("enter your marital status:")
status=input()
print("enter your sex:")
sex=input()
print("enter your age:")
age=input()
if status=='married':
    print('congratulation', name,'you are eligible for insured')
elif status=='unmarried' and sex=='male' and age>='30':
    print('congratulation', name,'you are eligible for insured')
elif status=='married' and sex=='female' and age>='25':
    print('congratulation', name, 'you are eligible for insured')
else:
    print('sorry', name, 'you are not eligible for insured')