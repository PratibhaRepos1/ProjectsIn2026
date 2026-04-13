#write  function

def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(20,30))

import math as m
print(m.sqrt(16))

#Factorial function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# factorial of 5 is 5 = 5*4*3*2*1

print(factorial(5))