# Create a Text Cleaner

import re

def clean_text(text):
    #Remove punctuations
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

# input_text = input("Enter some text: ")
# cleaned_text = clean_text(input_text)
# print("Cleaned Text: ", cleaned_text)


# Check if a String is a Palindrome for example madam

def is_palindrome(text): 
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text1 = input("Enter a string: ")
if is_palindrome(input_text1):
    print(f'"{input_text1}" is a plaindrome.')
else: 
    print(f'"{input_text1}" is not a palindrome.')

# Write a program to count the number of vowels in a string
# Create a program to find and replace all email addresses in a text using regex
# Write a program to reverse the words in a sentence (not the letters)