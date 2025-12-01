tuple=(10,"Abhi",2.32,10)
# print(tuple)
# print(tuple[0])
# print(tuple[1])
# print(tuple[2])
# print(tuple[3])
index=tuple.index("Abhi")
print(index)
count=tuple.count(10)
print(count)
print("Using loop: ",end=" ")
for i in tuple:
    print(i,end=" ")
# print("\n")
# for i in range(len(tuple)):
#     print(tuple[i],end=" ")
# print(type(tuple))
#TUPLE UNPACKINg
a,b,c,d=(1,2,"Abhi",32.1)
print(a)
print(b)
print(c)
print(d)
# Key Features

# Immutable: Elements cannot be modified, added, or removed.

# Ordered: Maintains insertion order and supports indexing.

# Allows Duplicates: Same value can appear multiple times.

# Heterogeneous: Can store different data types (int, str, float, etc.).

# Faster than lists: Due to immutability, tuples perform faster.

# Hashable: Tuples can be used as dictionary keys (if elements are also immutable).