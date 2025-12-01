a=[1,1,1,1,2,2,3,3,4,5,5,6]
dict={}
for i in a:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
print(dict) #output:{1: 4, 2: 2, 3: 2, 4: 1, 5: 2, 6: 1}