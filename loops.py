for i in range(6):
    print("Hello")
    
# Example 1: Print numbers 1 to 5
for i in range(1, 6):
    print(i)
    
#Example 2: Print 0 to 4
for i in range(5):
    print(i)
    
# Example 3: Step value
for i in range(1, 10, 2):
    print(i)
    
#for loop with string
name = "Shital"
for ch in name:
    print(ch)
    
#for loop with list
list = [10, 20, 30]
for l in list:
    print(l)
    
#Example: Print even numbers
for i in range(20):
    if i%2 == 0:
        print(i)
        
#break → stop loop
for i in range(11):
    if i == 9:
        break
    print(i)
    
#continue → skip current iteration
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
  
#####################################################
    
#PRACTICE TASKS
#Task 1 : Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
    

#Task 2:Print even numbers from 1 to 20
for i in range(1, 21):
    if i%2==0:
        print(i)
        
#Task 3:Print each character of your name
name = "Shital"
for ch in name:
    print(ch)
    
#Task 4:Print numbers from 10 to 1 (reverse)
for i in range(10, 0, -1):
    print(i)
    
##################################################
# while loop
#Print numbers 1 to 5
i = 1 
while i<=5:
    print(i)
    i+=1
    
#Using break in while loop
i = 1
while True:
    print(i)
    if i == 10:
        break
    i+=1
    
#Using continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#📝 PRACTICE TASKS (DO THIS)
#Task 1:Print numbers 1 to 10 using while loop
i = 1
while i <=10:
    print(i)
    i+=1
    
#Task 2:Take input from user repeatedly until they type "exit",Print "Hello" each time

while True:
    i = input("Type something: ")
    if i== "exit":  
        break
    print("Hello")