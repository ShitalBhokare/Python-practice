# List - mutable , square bracket
fruits = ["apple", "banana", "mango"]

#accessing items in the list
print(fruits[0])
print(fruits[1:])
print(fruits[-1])
print(fruits[:])
print(fruits[1:2])
print(fruits[::-1])

# add item at the end of the list
fruits.append("guava")
print(fruits[:])

# insert item at any index in the list
fruits.insert(2, "grapes")
print(fruits)

# remove the item from the list
fruits.remove("grapes")
print(fruits)

# remove item by index
fruits.pop(3)
print(fruits)

# looping through list
for fruit in fruits:
    print(fruit)
    
# sort 
fruits.sort()
print(fruits)

# reverse
fruits.reverse()
print(fruits)

# size / length
print(len(fruits))

#######################################################
# tuples - immutable, round brackets/ paranthesis.
colors = ("red", "blue", "black","yellow")
# accessing
print(colors[0])
print(colors[-1])
print(colors[:])
print(colors[::-1])

# looping through tuple
for color in colors:
    print(color)
    
#######################################################
# dictionaries - key value pair
person = {
    "name" : "shital",
    "age" : 22,
    "city": "shirdi"
}

#accessing the values/item
print(person["name"])
print(person.get("age"))

#adding / updating values
person["age"] = 30                # update
person["state"] = "Maharastra"    #adding
print(person)

#removing values
person.pop("state")
print(person)

del person["age"]
print(person)

# looping through dictionary
for key in person:
    print(key, ":" , person[key])
    
    # OR 
    
for key, value in person.items():
    print(key, ":", value)
    
######################################################

"""Task 1: List
Create a list of 5 numbers
Print each number multiplied by 2"""

numbers = [1, 3, 6, 8, 4]
for number in numbers:
    print(number*2)
    

"""Task 2: Tuple
Create a tuple of 4 strings (names)
Print the first and last name"""  

names = ("Rupali", "Prachi", "Daya", "Ashwini")
print(names[0])
print(names[-1])


"""Task 3: Dictionary
Create a dictionary with keys: "name", "age", "city"
Print all key-value pairs
Update "age" and add "phone"
Remove "city"""

person= {
    "name" : "Rutuja",
    "age" : 27,
    "city": "Shrirampur"
}
for key in person:
    print(key , ":" , person[key])
    
person["age"] = 33
person["phone"]=1234343456
print(person)

person.pop("city")
print(person)