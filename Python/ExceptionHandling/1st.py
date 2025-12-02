a=int(input("Enter num: "))
b=10
print(b/a)

# case 1: a=2  output: 5.0
# case 2: a=5  output: 2.0
# case 3: a=0  output: ZeroDivisionError: division by zero


# Exception Handling 
# | **Keyword** | **Purpose**                                                                  |
# | ----------- | ---------------------------------------------------------------------------- |
# | **try**     | Wrap the block of code that might cause an exception (risky code).           |
# | **except**  | Handle the exception if it occurs.                                           |
# | **else**    | Run code **only if no exception occurs** in the try block.                   |
# | **finally** | Run code **no matter what**, whether exception occurs or not (cleanup code). |
# | **raise**   | Manually throw an exception.                                                 |
