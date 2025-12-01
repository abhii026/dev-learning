def postive(l):
    for i in l:
        if i>=0:
            print(i,end=" ")
def negative(l):
    for i in l:
        if i<=0:
            print(i,end=" ")
def countPostNeg(l):
    pos=0
    neg=0
    for i in range(len(l)):
        if l[i]>0:
            pos+=1
        else:
            neg+=1
    return pos,neg

l=[10,12,-12,93,-10]
pos, neg = countPostNeg(l)
print(f"Positive numbers count: {pos}")
print(f"Negative numbers count: {neg}")
print("Positive number: ",end=" ")
postive(l)
print("\nNegative number are: ",end=" ")
negative(l)
