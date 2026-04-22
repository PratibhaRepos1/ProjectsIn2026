import sys
print("Hello World")
print(sys.version)

if 5 > 2:
    print("Five is greater than 2")
    
x = 5
y = "How are you?"

# This is single line comment

''' This is
Multi
line
comments
'''

print("Hi"); print("How are you?"); print("bye bye!");

print("Hey", end=" ")
print("I will print on the same line.")

name = "John"
print(type(name))

a,b,c = "apple", "banana", "cherry"
print(a,b,c)

d = e = f = "fruits"
print(e)

names = ["Ryan", "John", "Smita"]
name1, name2, name3 = names
print(name1)
print(name2)
print(name3)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)