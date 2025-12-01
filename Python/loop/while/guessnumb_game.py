import random
num= random.randint(1,11)
tries=0
while True:
    guess=int(input("Please guess the number: "))
    if(num==guess):
        tries+=1
        print("You are right.")
        break
    elif(guess<num):
        tries+=1
        print("go a little higher.")
    elif(guess>num):
        tries+=1
        print("go a little lower.")
    else:
        tries+=1
        print("You are wrong")

print(f"you guess in {tries} time.")
# print(num)