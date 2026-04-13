#integers and flaots

age = 25
height = 6.7

#strings
name = "John"
greeting = "Good Morning" + name

#list and tuple
numbers = [1,2,3,4]
names = ["Alice", "Jack"]

coordinates = (10,23)

#dictionary
person = {"name": "Alice", "age": 23}

#boolean
flag = True

print("Hello AI World!")

#Define variables of different data types
integer_var1 = 10
float_var1 = 3.4
string_var1 = "AI"
list_var1 = [1,4,8]
tuple_var1 = (5,10,15)
dict_var1 = {"name": "Raj", "role": "Engineer"}
bool_var1 = True


print("Integer: ", integer_var1)
print("Float:", float_var1)
print("String:", string_var1)
print("List:",list_var1)
print("Tuple:",tuple_var1)
print("Dictionary:", dict_var1)
print("Boolean:",bool_var1)


#Exmple  : Checking  condition
num2 = 2
if num2 > 0:
    print('number is positive')
elif num2 == 0:
    print('number is ero')
else:
    print('number is negtive')
    
    
# for loop
# loop through list of items

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#loop with range 
for i in range(5):
    print(i)
    
# while loop
count = 20

while count > 2:
    print(count)
    count -=2

print("outside while loop")
    
    
#using break nd continue 

for i in range(20):
    if i == 6:
        break

print(i)
print("continue:")

for j in range(20):
   if j % 2 == 0:
       continue
   print("j:",j)
    
print("outside continue")
    