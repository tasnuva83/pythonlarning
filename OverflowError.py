
try:
    fir_number = int(input('number:'))
    sec_number = int(input('number:'))
    fir_number=fir_number**1000
    sum = fir_number / sec_number
    print(sum)
except OverflowError as error:
    print('OverflowError: Number too large')
print('after exception')
