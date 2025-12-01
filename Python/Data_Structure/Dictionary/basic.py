d={"name":"Abhishek", "age":20, "city":"Varanasi"}
print(d) #output:{'name': 'Abhishek', 'age': 20, 'city': 'Varanasi'}
print("Type:",type(d)) #output:Type: <class 'dict'>
print(d["name"]) #output:Abhishek
print(d["age"]) #output:20
print(d["city"]) #output:Varanasi

d2={}
print(type(d2)) #output: <class 'dict'>

dict={1:"Hello",2:"Hii"}
print(dict) #output:{1: 'Hello', 2: 'Hii'}
print(dict[1]) #output:Hello
print(dict[2]) #output: Hii
dict[2]="World" #updating
print(dict[2]) #output: World
print(dict) #output: {1: 'Hello', 2: 'World'}
dict.update({"name":"Abhishek"}) #creating
print(dict) #output:{1: 'Hello', 2: 'World', 'name': 'Abhishek'}
dict[4]=40 #creating
print(dict) #output:{1: 'Hello', 2: 'World', 'name': 'Abhishek', 4: 40}
del dict[4] #deleting
print(dict) #output:{1: 'Hello', 2: 'World', 'name': 'Abhishek'}

