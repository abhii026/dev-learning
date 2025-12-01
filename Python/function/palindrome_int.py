def palindrome(num):
    rev=0
    # original=num
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num/=10
    print(rev)
palindrome(122)