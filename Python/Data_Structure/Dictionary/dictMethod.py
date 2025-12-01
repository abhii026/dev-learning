d={"name":"Abhishek", "age":20, "city":"Varanasi"}
print(d) #ouput: {'name': 'Abhishek', 'age': 20, 'city': 'Varanasi'}
d2=d.get("age")
print(d2) #output:20
print(d.items()) #output:dict_items([('name', 'Abhishek'), ('age', 20), ('city', 'Varanasi')])
d.clear()
print(d) #output: {}




# #Deep copy
# a=[1,2,3,4]
# print(a) #ouput:[1,2,3,4]
# b=a
# b[0]=10
# print(a) #ouput: [10,2,3,4]

# #shallow copy
# a=[1,2,3,4]
# print(a) #ouput:[1,2,3,4]
# b=a.copy()
# b[0]=10
# print(a) #ouput: [1,2,3,4]
# print(b) #ouput: [10,2,3,4]
