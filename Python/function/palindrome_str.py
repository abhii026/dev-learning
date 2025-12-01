def palindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev+=st[i]
    if rev==st:
        print(f"{st} is a palindrome")
    else:
        print(f"{st} is not a palindrome")
inp=input("Enter string (Captial/Small): ")
palindrome(inp)