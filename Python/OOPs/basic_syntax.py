class Student:                     # Class definition
    name = "Abhishek"              # Class attribute (shared by all objects)

    def hello(self):               # Instance method
        print("Abhi")              # Prints greeting

    print("It executes once, at the time of class creation, not object creation")
                                   # This line runs once when the class is created

print(Student().name)              # Accessing class attribute using an object
Student().hello()                  # Calling instance method using an object
