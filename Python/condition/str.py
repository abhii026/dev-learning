a="abhi123!@#"
dig=0
char=0
spchr=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchr+=1;

print(f"Digit is {dig}\nAlphabet is {char}\nSpecial character is {spchr}.")