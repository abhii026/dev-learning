l=[1,2,3,5,4]
flag=True
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        flag=False
        break
if flag:
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.") 