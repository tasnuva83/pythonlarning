print("enter buying price")
buying=float(input())
print("enter celling price")
selling=float(input())
result=selling-buying
if result>=00.0:
    print("profit =", result)
else:
    print("loss:", result)