num=[10,20,30,40]
print(num[0])  # Output: 10
print(num[1])  # Output: 20
print(num[2])  # Output: 30
print(num[3])  # Output: 40
print(num[-1]) # Output: 40 (last element)
print(num[-2]) # Output: 30 (second last element)
print(num[1:3]) # Output: [20, 30] (slicing from index 1 to 2)
print(num[1:])  # Output: [20, 30, 40]
print(num[:2])  # Output: [10, 20] (slicing from
print(num[:])  # Output: [10, 20, 30, 40] (whole list)
print(num[-3:-1]) # Output: [20, 30] (slicing from -3 to -2)
print(num[-3:])  # Output: [20,30, 40] (slicing from -3 to end)
print(num)


num.append(50)  # Adding an element to the end
print(num)  # Output: [10, 20, 30, 40, 50]
num.insert(2, 25)  # Inserting 25 at index 2
print(num)  # Output: [10, 20, 25, 30, 40, 50]
num.remove(30)  # Removing the first occurrence of 30
print(num)  # Output: [10, 20, 25, 40, 50]
num.pop()  # Removing the last element
print(num)  # Output: [10, 20, 25, 40]
num.pop(1)  # Removing the element at index 1
print(num)  # Output: [10, 25, 40]
num.clear()  # Clearing the list
print(num)  # Output: []
num=[10,20,30,40]
num.extend([50, 60])  # Extending the list with another list
print(num)  # Output: [10, 20, 30, 40, 50, 60]
num.reverse()  # Reversing the list
print(num)  # Output: [60, 50, 40, 30, 20, 10]
num.sort()  # Sorting the list
print(num)  # Output: [10, 20, 30, 40, 50, 60]

for i in range(len(num)):
    print(num[i])  # Output: 10, 20, 30, 40, 50, 60 (each element in a new line)    
# This code demonstrates basic list operations in Python
# including indexing, slicing, adding, removing, and iterating through elements.
for i in num:
    print(i)  # Output: 10, 20, 30, 40, 50, 60 (each element in a new line)
# This code demonstrates how to check if a string is a palindrome

num[1]=208 #mutable
print(num)  # Output: [10, 208, 30, 40, 50, 60] (updated second element)