""" Reading and writing files in python
    Opening Files:
        use the build-in open() function to open the file
        r|w|a|r+
    Reading Files:
        .read() | .readline() | readlines()
    Writing to Files
        .write() | writelines()
"""
# try:
#     with open("sample.txt", "r") as file:
#         # content = file.readlines()
#         # print(content)
#         file.write("Hello World!")
#         file.writelines(["Alice", "Bob", "Cherry"])
# except FileNotFoundError:
#     print("File not found!")
    
    
# Exercise 1: Count the words and lines in a file

def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found!")

count_words_and_lines("sample.txt")

# Exercise 2: Write and Read a list of items

def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items: 
            file.write(item + "\n")

def read_items_from_file(filename): 
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("Items in the file: ")
            for item in items:
                    print(item.strip())
    except FileNotFoundError:
        print(f"File {filename} not found!")
        
fruits = ["Apple", "Banana", "Cheery", "Dates"]
write_item_to_file("fruits.txt", fruits)

read_items_from_file("fruits.txt")

""" 
Write a program to copy the contents of one file to another
Create a program that counts the number of occurrences of a
specific word in a text file
Write a program to log messages with timestamps into a file
"""