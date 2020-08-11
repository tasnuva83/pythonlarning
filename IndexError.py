try:
    list=["foo","bar","baz","bon"]
    print(list[5])
except IndexError as error:
    print('Indexerror exception occured')
print('after exception')
