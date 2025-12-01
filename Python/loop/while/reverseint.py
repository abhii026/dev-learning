n=int(input("Enter number: "))
orignal=n
rev=0
while(n>0):
    rem=n%10
    rev=rem+rev*10
    n=n//10
if(rev==orignal):
    print(f"{orignal} is palindrome")
else:
    print(f"{orignal} is not palindrome")
