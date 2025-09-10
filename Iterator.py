# ------------------------------
# Normal List Iteration
# ------------------------------

num=[10,20,30,40]
# Accessing by index directly
print(num[0])   # -> prints 10  





# Using a for loop (automatic iteration)
for i in num:
    print(i)   # Prints: 10, 20, 30, 40
    



    
# ------------------------------
# Using iter() and next() manually
# ------------------------------    
it = iter(num)        # Create an iterator object from the list
print(next(it))       # Prints 10
print(next(it))       # Prints 20
print(next(it))       # Prints 30
print(next(it))       # Prints 40
# After this, if you call next(it) again, it will raise StopIteration




# ------------------------------
# Handling StopIteration manually with try-except
# ------------------------------
while True: 
    try:
        print(next(it))   # Keep fetching next element
    except StopIteration: # When no more elements left, exit loop
        break
    



# ------------------------------
# Custom Iterator Example
# ------------------------------
class Count:
    
    def __init__(self, start, stop):
        self.current = start   # Starting point
        self.stop = stop       # End point
        
    def __iter__(self):
        return self            # Returns the iterator object itself
    
    def __next__(self):
        if self.current <= self.stop:  # Check if not crossed stop value
            val = self.current
            self.current += 1          # Move to next number
            return val                 # Return current number
        else:
            raise StopIteration        # End iteration when stop reached

# Using custom iterator
numbers = Count(1, 10)
for i in numbers:   # for loop internally calls iter() and next()
    print(i)        # Prints 1 to 10
