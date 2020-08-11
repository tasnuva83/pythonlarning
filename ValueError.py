try:
    fir_number = int(input('number:'))
    sec_number = int(input('number:'))
    sum = fir_number + sec_number
    print(sum)
except ValueError as error:
    print('ValueError: invalid number')
print('after exception')

