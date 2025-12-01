# Pattern 1
# 1  
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

print("Pattern 1")
n=5
for i in range(1,n+1):
    for j in range(i):
        print((i+j)%2, end=" ")
    print(" ")

# Pattern 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


print("\nPattern 2")
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

# Pattern 3
# *
# * *
# * * *
# * * * *
# * * * * *
print("\nPattern 3")
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")

# Pattern 4
# *           *
#   *       *
#     *   *      
#       *
#     *   *
#   *       *
# *           *
print("\nPattern 4")
n=7
for i in range(n):
    for j in range(n):
        if(i==j or j==n-i-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print(" ")