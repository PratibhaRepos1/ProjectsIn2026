import re
# working with the Strings, string manupulations like concatentation, Slicing, Formatting

first = "Hello"
second = "World"

result = first + " " + second
# print(result)

text = "Python Programming"

# print(text[0:6])
# print(text[-11:])

name = "Alice"
age = 23
# print(f"My name is {name} and I am {age} years old")

# split(), join(), replace() strip()

sentence = "Python is fun"
words = sentence.split() # default is space character here
print(words)

new_sentence = " ".join(words)
print(new_sentence)

text1 = "I love Java"
updated_text1 = text1.replace("Java", "Python")
print(updated_text1)

messy = "    Hello, Wrold     "
clean_text = messy.strip() # strip only remove the space between front and end
print(clean_text)

""" Regular Expressions for Pattern Matching - way to search, match, pattern to search the string or manupulate also there is re module
re.search(pattern,string)
re.findall(pattern,string)
re.sub(pattern,replacement,string)
"""
call_me = "Contact me at 123-456-7890"
digits = re.findall(r"\d+",call_me)
print(digits)

updated_phone = re.sub(r"\d", "X", call_me)
print(updated_phone)

