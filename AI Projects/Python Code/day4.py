# Data Structures, Lists , Tuples, Dictionaries, Sets
numbers = [1,2,3,4]

fruits = ["apple", "banana", "cherry"]

mixed = [2, "banana", True]
print("-----Lists in Python--------")
print(numbers[2])
print(fruits[0])
print(mixed[-1])

fruits.append("orange")
fruits.insert(1,"grape")

# print(fruits)

# fruits.remove("banana")

# print(fruits)

# del fruits[0]
# print(fruits)

# fruits.pop()
# print(fruits)

# slicing list - getting element from particular place

sliced_fruits = fruits[1:3]
print(sliced_fruits)

# Tuples are ordered mutable collections, tuples are immutability can not be modify

colors = ("red", "green", "blue")
single_item = ("glass",  )
print("-----Tuples in Python--------")
print(single_item)

print(colors[0])

# Dictionaries Key value pairs for fast lookup

print("-----Dictionaries in Python--------")
student = {"name": "Alice", "age": 23, "grade": "A"}
student["subject"] = "Math"
print(student)

print(student["name"])

# delete the key
# del student["grade"]
# print(student)

# student.pop("subject")
# print(student)

# iterate
for key,value in student.items():
    print(key,value)
    
# Sets: unorder collections of unique items
print("-----Sets in Python--------")
numbers = {1,2,3,4}

empty_set = set()

print(numbers)
numbers.add(5)
print(numbers)
numbers.remove(2)

print(numbers)
# Set Operations

set1 = {1,2,3, 5,6}
set2 = {3,4,5,6}
# union will done by | symbol
print(set1 | set2)

# intersection will done by & symbol, it shows match elements in both sets
print(set1 & set2)

# differeniates will done by - symbol
print(set1 - set2)