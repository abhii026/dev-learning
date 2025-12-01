d={"name":"Abhishek", "age":20, "city":"Varanasi"}
for i in d:
    print(i,end=" ") #output: name age city   give keys.
for i in d:
    print(d[i],end=" ") #output: Abhishek 20 Varanasi
for i in d.values():
    print(i,end=" ") #output: Abhishek 20 Varanasi 