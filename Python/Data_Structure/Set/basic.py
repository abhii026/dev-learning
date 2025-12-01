# s={}
# it is dictonary

s={1,2,3,4,5,5}
print(s)
#output: {1, 2, 3, 4, 5} it remove duplicate value like 5.

a={1,2,3,8,4,"Abhi",2}
for i in a:
    print(i,end=" ")
# output:1 2 3 4 Abhi 8




# Key Features
# Unordered: No fixed order; indexing and slicing are not supported.
# No Duplicates: Automatically removes repeated values.
# Mutable: You can add or remove elements after creation.
# Heterogeneous: Can store different data types (int, float, str, etc.).
# Fast Operations: Optimized for membership testing (like checking if an item exists).
# Used for Mathematical Operations: Supports union, intersection, difference, etc.