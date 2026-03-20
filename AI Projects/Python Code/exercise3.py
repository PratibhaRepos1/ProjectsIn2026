# Exercise 1: Manipulate Data in a Dictionary
person = {"name": "John", "age": 34, "Developer": True}
print(person)
# Add new key value pair
person["address"] = "123 main ST"

# update age
person["age"] = 32

# Remove key with value

if "Developer" in person:
    del person["Developer"]

print(person)

# Exercise 2: Word Frequency Counter
sentence = input("Enter a Sentence: ")

# Split the sentence into words
words = sentence.split()

# initialize Dictionary
word_count = {}

# Count word freuence
for word in words:
    word = word.lower()
    
    if word in word_count:
        word_count[word] += 1
    else: 
        word_count[word] = 1
print(word_count)

# Write a program to reverse a list and remove duplicates using a set
# Create a program that stores student grades in a dictionary and calculates the average grade