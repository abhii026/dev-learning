#if_elif ladder problem

temp=int(input("Enter temperature in celsius: "))

if(temp<0):
    print(f"Freezing Cold, temperature= {temp}'C.")
elif(temp>0 and temp<10):
    print(f"Very Cold, temperature= {temp}'C.")
elif(temp>10 and temp<20):
    print(f"Cold, temperature= {temp}'C.")
elif(temp>20 and temp<30):
    print(f"Pleasent, temperature= {temp}'C.")
elif(temp>30 and temp<40):
    print(f"Hot, temperature= {temp}'C.")
else:
    print(f"Very Hot, temperature= {temp}'C.")
