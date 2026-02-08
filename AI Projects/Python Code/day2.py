# Example 1: Checking a condition
num = 40
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")
    
# Example 2: Nested conditions
age = 35
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")
        
# Loops
# for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
# Loop with range
for i in range(5): 
    print(i)

#while loop
count = 5
while count > 0:
    print(count)
    count -=1

print("outside while loop")

# using break and continue for control flow

for i in range(10):
    if i == 5:
        break
    print(i)
print("outside For loop")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
# Exercise 1: check if the Number is Prime
num = int(input("Enter a number: "))
if(num > 1 ):
    for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    
# Exercise 2: Create a Menu-Driven Caculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiple(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "division by zero is not allowed"
    
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "5":
        print("Exiting Program.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result: ", add(num1,num2))
    elif choice == "2":
        print("Result: ", subtract(num1,num2))
    elif choice == "3":
        print("Result: ", multiple(num1,num2))
    elif choice == "4":
        print("Result: ", divide(num1,num2))
    else:
        print("Invalid choice. Please enter the correct choice.")