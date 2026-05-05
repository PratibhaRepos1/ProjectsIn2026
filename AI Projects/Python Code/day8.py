# tuples in python

mytuple = ("apple", "banana","cherry")

# stored multiple items in single variables, A tuple is a collection which is ordered and unchangeable.
# items are ordered, unchangeable, and allow duplicate values

thistuple = ("apple", "banana", "cherry", "apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))

# create a tuple with One item
onetuple = ("one",)
print(type(onetuple))

# tuple with different data types
tuple1 = ("one", 1, True, 1.0, "abd")
print(type(tuple1))

# Access Tuple Items
print(tuple1[1])
print(tuple1[-2])

#Range of Indexes
print(tuple1[1:3])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruit tuple")

#Convert the tuple into a list to be able to change it:
x = (1,2,3,4)
y = list(x)
y[1] = 9
x = tuple(y)

print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Create a new tuple with the value "orange", and add that tuple:
a = (1,2,3)
b = (4,5,6)
a += b
print(a)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
fruits = ("apple", "banana", "cherry")
y = list(fruits)
y.remove("apple")
fruits = tuple(y)

print(fruits)

#The del keyword can delete the tuple completely:
thistuple = (True, False)
del thistuple
# print(thistuple)

#Packing a tuple:
names = ("John", "Sky")

#in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(Johny, Ski) = names

print(Johny)
print(Ski)

myqueue = (1,2,3,4,5,6,7,8,9)
for q in range(len(myqueue)):
    print(myqueue[q])
    
#while loop
numbers = (12,45,89,23,21)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
    
print("************************************")
#Join two tuples:
tuple1 = (1,2,3)
tuple2 = (4,5,6)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple.count(4))