import random

x = "Awesome"

def mydef():
    x="fantastic"
    print("pythyon is ", x)


mydef()
print("python is ",x)

print(random.randrange(1,10))

#Multiline Strings
a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# print(a)

b = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(b)

# string in python

a = "Hello World"
print(a[1])
print(len(a))

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, free is present.")

# slice in the string
b = "Hello, World!"
print(b[-5:-2])

x = 'Welcome'
print(x[3:5])

c = "cherry"
print(c.upper())

d = "DEAR"
print(d.lower())

#remove white space
txt1 = "  Hey  whats goin on!  "
print(txt1.strip())

#replace the string

e = "str"

print(e.replace("st","er"))

#split
txt2 = "Good, Morning"
print(txt2.split(","))

#F-String

age =35
txt3 = f"My name is John, I am {age}"
print(txt3)

greet = "Good Afternoon"
txt4 = f"Hey John, {greet} How are you?"
print(txt4)

price = 67
txt5 = f" The is product price is {price:.2f} dollars"
print(txt5)

txt9 = "Hello World"
x = txt9[2:5]
print(x)

x = "Welcome"
print(x[3:])

txt = " Hello World "
print(txt.strip())


print(10 > 9)
print(10 == 9)
print(10 < 9)

a =3
b =33
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")
    
print(bool("Hello"))
print(bool(0))

class myClass():
    def __len__(self):
        return 0
myobj = myClass()
print(bool(myobj))

print(15 % 4)

x = 5
x <<= 3
print(x)

# The Walrus Operator 

numbers = [1,2,3.4,5]
if (count := len(numbers)) > 3:
    print(f"List has {count} element")

#Identity Operators: is is not

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

print(2 + 3 * 4)