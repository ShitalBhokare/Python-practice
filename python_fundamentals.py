# Variables = named memory location that stores data 
x = 5
print(x)
y = 10
print(y)
z = x+y 
print(z)

# multiple assignments
a, b, c = 5, 6 ,7
print(a+b+c)

# same value to multiple variables
a=b=c=10
print(a+b+c)

#########################################################

#data types
# a) Numeric types 

a = 10      # int 
b = -5      # int 
print(a, b)

pi = 3.14       #float
price = 99.99   #float
print(pi, price)

x = 2 +3j  #complex
print(x)

# b) text type 

name = "shital"  # string 
city = 'Pune'   # string
print(name , city)

is_active = True    # boolean
is_logged_in = False  # boolean
print(is_active, is_logged_in)

############################################################

# output -> print()

print("Hello world")
print(10)

# printing multiple values

name = "Shital"
age = 22
print(name, age)

# Input -> input()

name = input("Enter your name: ")

###################################################

# type casting

age = int("25")  #string to int
num = str(10)    #int to string
price = float(100)  # int to float
print(age, num, price)

####################################################

#task
"""Write this program:
1️⃣ Take name
2️⃣ Take age
3️⃣ Take city
4️⃣ Print all details"""

name = "shital"
age = 22
city = "shirdi"

print("My name is", name )
print("My age is", age)
print("I live in",city)

######################################################

# operators
# 1) Arithmetic operators

a= 10 
b = 3 
print(a+b)   # addition
print(a-b)   # subtraction
print(a*b)   # multiplication
print(a/b)   # division
print(a//b)  # floor division
print(a%b)   # modulus
print(a**b)  # power

# 2) Assignment operator

a = 10
a+=5
print(a)

a = 10
a-=5
print(a)

# 3) comparison operators

a = 10
b = 5
print(a==b)
print(a != b)
print(a < b)
print(a > b)
print(a <=b)
print(a >= b)

# 4) logical operator

age = 25

print(age>18 and age<30)
print(age>18 or age<30)
print(not(age>18))

# 5) identify operator

a = 10
b= 20
print(a is b)
print(a is not b)

# 6) membership operator

name = "shital"
print("s" in name)
print("h" not in name)

# operator precedence
"""
Order of execution:
1 .()
2. **
3. * / // %
4. + -
5. Comparison
6. Logical"""

result = 10 + 2 * 3
print(result)

result = (10 + 2) * 3 
print(result)

######################################################

"""
📝 PRACTICE TASK (VERY IMPORTANT)

Write a program:
1️⃣ Take two numbers from user
2️⃣ Print:
Addition
Subtraction
Multiplication
Division
Modulus"""

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(f"Addition:{n1+n2}")
print(f"Subtraction:{n1-n2}")
print(f"Multiplication:{n1*n2}")
print(f"Division:{n1/n2}")
print(f"Modulus:{n1%n2}")

######################################################

# control statements

# 1) If statement
age = 23
if age >= 18:
    print("You are an adult")
    
# 2) if-else statement
age = 23
if age >= 15:
    print("You can vote")
else:
    print("You cannot vote")
    
    
# 3)if-elif-else statement
marks = 85
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 36:
    print("Grade D")
else:
    print("Fail")
    
# Nested if statements
age = 22
citizen = True
if age >= 18:
    if citizen:
        print("Eligible for vote")
    else:
        print("You are not citizen of India")
else:
    print("Under age")
    
#######################################################

#🟢 PRACTICE TASKS – if / else / elif 

"""
✅ Task 1: Even or Odd
Take a number from the user.
If number is even → print "Even number"
Else → print "Odd number"""

num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    

"""✅ Task 2: Positive, Negative, or Zero
Take a number.
If > 0 → "Positive"
If < 0 → "Negative"
Else → "Zero"""

num = int(input("Enter the number: "))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")
    
    
"""✅ Task 3: Largest of Two Numbers
Take two numbers.
Print which number is greater
If both are equal, print "Both are equal"""

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print(f"{n1} is greater")
elif n1 < n2:
    print(f"{n2} is greater")
else:
    print("both are equal")
    

"""✅ Task 4: Simple Login System
Take:
username
password
Conditions:
If username == "admin" and password == "1234" → "Login successful"
Else → "Invalid credentials"""

uname = input("enter username: ")
pword = input("Enter password")
if uname == "admin" and pword == "1234":
    print("Login successfully")
else:
    print("Invalid credentials")


"""✅ Task 5: Leap Year Checker
Take a year.
If leap year → "Leap year"
Else → "Not a leap year"""

year = 2024
if (year % 4 == 0 and year % 100 != 0 )or (year % 400 == 0):
    print("leap year")
else:
    print("Not a leap year")
    

"""✅ Task 6: Electricity Bill
Take units from user:
Units ≤ 100 → ₹0
101–200 → ₹5 per unit
200 → ₹10 per unit
Print total bill."""

units = int(input("Enter electricity units:"))
if units <= 100:
    bill = 0
elif units <=200:
    bill = (units - 100) * 5
else:
    bill = (100 * 0) + (100 * 5) + (units - 200) * 10
    
print(f"{bill}")

########################################################

