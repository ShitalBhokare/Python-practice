# functions is a block of reusable code
# it runs only when called

#function without parameter
def greet():
    print("Hello!!")
greet()

# function with parameter
def greet(name):
    print("Hello",name)
    
greet("Shital")
greet("Rutuja")

# addition of two numbers
def add(a, b):
    print(a+b)

add(10, 30)
add(10,3)

# difference between print and return 

# print can't be reusable
# print not get value value to caller

def add(a, b):
    print(a+b)

result = add(10, 30)
print(result)   # ans is none because it does not get value back to caller

# return get value back to caller, it is reusable

def add(a, b):
    return a+b 

result = add(10, 30)
print(result) # ans is 40 

# multiple return values 

def calculate(a, b):
    return a+b , a-b, a*b, a/b 

add, sub, mul, div = calculate(40,5)
print(add, sub, mul, div)

# default parameter
def greet(name = "user"):
    print("Hello", name)
    
greet()
greet("shital")

#keyword arguments
# It helps to avoid confusion . 
# No need to follow the order. overcome the drawback in arguments

def student(name, age):
    print(name, age)
    
student(name="Shital", age = 23)


# function with loop and condition
def check_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))


# scope
a = 10  #global - accessible outside the function

def test():
    b = 5  # local - not accessible outside the function
    print(b)
    
test()
print(a)

#########################################################

#Task 1:Create a function to add two numbers and return result
def add(a, b):
    return a+b 
print(add(10,20))

#Task 2:Create a function to check even or odd
def even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(10))

#Task 3:Create a function that takes a list and returns sum of elements
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [1,6,4,8,2] 
result = sum_of_list(my_list)
print(result)