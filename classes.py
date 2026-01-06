# class is the blueprint (designing)
# object is the real instance created from a class
# one class -> many object 

class Student:
    pass

#creating object 

s1 = Student()
s2 = Student()

# constructor

class Student:
    def __init__(self, name , age):  # __init__ is constructor
        self.name = name  # self stores the name inside the THIS object 
        self.age = age
        
s1 = Student("Shital", 22)
s2 = Student("Rutuja", 27)

print(s1.name , s1.age)
print(s2.name, s2.age)


# adding methods

class Student:
    def __init__(self, name,age):
        self.name = name 
        self.age = age
        
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        
s1 = Student("Shital", 22)
s1.display()
        
"""Task:
Create a class Employee with:
attributes: name, salary
method: show_details()
Create 2 objects and print their details."""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show_details(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        
s1 = Employee("Rupali", 30000)
s1.show_details()