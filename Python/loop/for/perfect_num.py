n = int(input("Enter number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
