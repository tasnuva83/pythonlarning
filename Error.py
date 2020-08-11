try:
    list=["foo","bar","baz","bon"]
        print(list[2])

except IndentationError as error:
    print('unexpected indent occured')

print('after exception')