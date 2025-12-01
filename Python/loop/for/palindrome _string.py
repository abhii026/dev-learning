str=input("Enter string(write in captial/ small ony): ")
rev_str=""
for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]
if(str==rev_str):
    print(f"{str} is palindrome.")
else:
    print(f"{str} is not palindrome.")