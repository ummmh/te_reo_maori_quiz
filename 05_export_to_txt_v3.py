"""Component 5 of Te Reo Māori Quiz
Writes the test data into a .txt file
Source: https://www.quru99.com?reading-and-writing-files-in-python.html
Created by Janna Lei Eugenio
31/05/2022
"""

import re

# Data to be outputted
data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    name = input("Enter a filename: ")

    # regular expression to check file name-can be upper or lower case letters,
    valid_char = "[A-Za-z0-9_]"  # numbers or underscores
    for letter in name:
        if re.match(valid_char, letter):
            continue
        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = f"no {letter}'s allowed"
        has_error = "yes"

    if name == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":  # describe problem
        print(f"Invalid filename - {problem}")
        print()
    else:
        print("You entered a valid filename")  # allow valid file name

# add .txt suffix
filename = name + ".txt"

# create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

# close file
f.close()
