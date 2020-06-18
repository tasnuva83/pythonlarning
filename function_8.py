def numbers_inrange():
    list = [x for x in range(2000,3201) if x%7==0 and x%5!=0]
    print(list)

numbers_inrange()
