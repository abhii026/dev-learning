l=[10,20,5,40,30,35]
max=l[0]
second_max=l[0]
for i in range(len(l)):
    if l[i]>max:
        second_max=max
        max=l[i]
    elif l[i]>second_max:
        second_max=l[i]
print(f"The second largest number in the list is: {second_max}.")