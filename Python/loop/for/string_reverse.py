n=input("Enter string: ")
rev_n=""
for i in range(len(n)-1,-1,-1):
    rev_n+=n[i]
print(f"Reversed string of {n} is {rev_n}.")