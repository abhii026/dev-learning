l=[10,12,-12,93,-10]
pos=0
neg=0
for i in range(len(l)):
    if l[i]>0:
        pos+=1
    else:
        neg+=1
print(f"Positive numbers count: {pos}")
print(f"Negative numbers count: {neg}")