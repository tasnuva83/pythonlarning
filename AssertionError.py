try:
    def get_age(x):
        assert x>18, 'age should be above 18'
        print('your age is:', x)
    get_age(12)
except AssertionError as error:
    print('age should be above 18')
print('after exception')