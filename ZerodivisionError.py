try:
    fir_number = int(input('number:'))
    sec_number = int(input('number:'))
    sum = fir_number / sec_number
    print(sum)
except ZeroDivisionError as error:
    print('ZeroDivisionError:division by zero')
print('after exception')
