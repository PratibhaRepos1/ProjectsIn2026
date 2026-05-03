# list in python
fruits = ['apple', 'banana', 'cherry', "orange", "kiwi", "melon", "mango"]
print(type(fruits))

print(fruits[2:5])
print(fruits[:4])
print(fruits[2:])

# append()

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist.insert(1,"Pear")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)

# Add any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#loop the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
    
# shorthand for loop
[print(x) for x in thislist]

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)