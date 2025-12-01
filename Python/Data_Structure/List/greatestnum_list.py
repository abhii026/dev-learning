l=[1,2,3,4,5,8,20,1,345]
max=l[0]
index=0
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
        index=i
print(f"The greatest number in the list is: {max} at index {index}.") 

