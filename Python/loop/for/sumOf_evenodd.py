n=int(input("Enter range: "))
even=0
odd=0
for i in range(1,n+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(f"Sum of even is {even} and odd is {odd}")