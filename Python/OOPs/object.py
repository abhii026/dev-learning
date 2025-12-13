class Student:
    college_name="XYZ"  #class variable
    def __init__(self,name): #Instance Variable
        self.name=name


s1=Student("Abhi")
print(f"Student1 name: {s1.name}\ncollege name: {Student.college_name}")
s2=Student("Aman")
print(f"\nStudent2 name: {s2.name}\ncollege name: {Student.college_name}")

# s1.name              # Instance variable
# s2.name              # Instance variable
# Student.college_name # Class variable
