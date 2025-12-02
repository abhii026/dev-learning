# age=int(input("Your age: "))
# if(age<10 or age>18):
#     raise ValueError("Your age must be between 10 and 18.")
# else:
#     print("Welcome to the club.")


# case 1: 
# age=15
# output:Welcome to the club.

# case 2:
# age=8
# output:
# 
#     raise ValueError("Your age must be between 10 and 18.")
# ValueError: Your age must be between 10 and 18.

age=int(input("Your age: "))
try:

    if(age<10 or age>18):
        raise ValueError("Your age must be between 10 and 18.")
    else:
        print("Welcome to the club.")
except Exception as err:
    print(f"There is an error {err}")


# case 1:
# age=5
# output: There is an error Your age must be between 10 and 18.

# case 2:
# age=17
# output:Welcome to the club.


