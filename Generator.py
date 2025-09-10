
# ------------------------------
# Normal Function with return
# ------------------------------

# A normal function that returns a list of squares

def square_list(n):
    result=[]
    for i in range(1, n+1):
        result.append(i*i)
    return result
    
print(square_list(5))


# ------------------------------
# Generator Function with yield
# ------------------------------

# Generator function using yield
def square_list(n):
    for i in range(1,n+1):
        yield i*i      # Generates values one at a time
        
gen=square_list(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Each next() continues from where it stopped


# ------------------------------
# Using Generator in a Loop
# ------------------------------
def square_list(n):
    for i in range(1,n+1):
        yield i*i 
        
gen=square_list(10)
for j in gen:
    print(j)


# ------------------------------
# Handling StopIteration
# ------------------------------
def square_list(n):
    for i in range(1,n+1):
        yield i*i 
        
gen=square_list(20)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break


# ------------------------------
# Handling StopIteration
# ------------------------------
gen_exe=(i*i for i in range(1,10))

for j in gen_exe:
    print(j)
        
    
    



