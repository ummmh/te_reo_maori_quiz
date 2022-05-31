"""Component 5 of Te Reo Māori Quiz
Writes the test data into a .txt file
Source: https://www.quru99.com?reading-and-writing-files-in-python.html
Created by Janna Lei Eugenio
31/05/2022
"""

# Data to be outputted
data = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

# assume valid data for now
filename = input("Enter a filename (leave off the extension): ")

# add .txt suffix
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

# close file
f.close()
