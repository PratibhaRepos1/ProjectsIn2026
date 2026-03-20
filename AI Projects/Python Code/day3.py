import math
print(math.sqrt(16))

def add_number(a,b):
    c = a + b
    return c

result = add_number(7,2)
print("Sum: ", result)

#local scope
def greet():
    message = "Hello World"
    print(message)
    
greet()

greeting = "Hi"
# Global Scope
def say_hello():
    print(greeting + " from inside function")
    
say_hello()

print(greeting + " outside the function")

#what are Modules? Importing Modules

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def print_factorial(n):
    result = factorial
    
