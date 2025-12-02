a=int(input("Enter num: "))
b=10
try:
    print(b/a)
# except Exception as err:
except ZeroDivisionError:
    # print(f"Sorry there is an error: {err}")
    print(f"Sorry there is an error")
else:
    print("No error")
finally:
    print("I will run no matter run will come or not")
# print("No division")

# case 1: a=0 output: Sorry there is an error: division by zero
# No division


# case 2: a=2 output: 5.0 No error