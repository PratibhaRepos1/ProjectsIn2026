print("Today is a good day to learn python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world!")

# Variables in Python
celsius_temp = 25
print(celsius_temp)

a,b,c = 1,2,3
print(b)

age, name = 34, "Alice"

print(age)
print(name)

# naming conventions
total_count = 100

'''
Rules:
Avoid Leading Underscores
No special Characters or spaces 
can not use reserved words
case sensitivity
use descriptive names and snake_case
'''

# Numbers: int and float
age = 40
temperature = 20.1

# 2. Booleans: logical values, True or False
print(age == 40)
print(age < 30)

# tuples
coordinates = (34.12, -34.5333)

# sets
ip_addresses = ('100.80.1.2', '5.4.2.5')

# FroznSets
frozen_user_ids = frozenset([1001, 1005,524])

# dictionaries
person = {'name': 'Alice', 'age': 30, 'is_employed': True}

# static Vs Dynamic typing
print(2+2*2**2)
print(19 // 3)
print(18 % 3, 15 / 3, 16 // 3, 2 ** 3)

print(700 == 7_0_0)

x = 8
x **=3
x /= 4

print(x)

name = 'Alice'
id1 = id(name)
name = 'Emma'
id2 = id(name)
print(id1)
print(id2)

x = 12
id1 = id(x)

x = +5
id2 = id(x)

print(id1 == id2)

# python string basics
model_summary = 'This AI model predicts stock trends.'
prediction_message = "AI will revolutionize industries!"

print("AI says, I'm here to assist you.")

ai_response = """Hello there!
I'm an AI here to help.
Feel free to ask me anything."
"""
print(ai_response)

ai_prompt = 'Welcome to AI Bot\nYour virtual assistant\nHere to assist with all things tech!'

print(ai_prompt)

print('\\ is essential for handling escape charaters in Python.')