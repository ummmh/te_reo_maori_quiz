"""Component 3 of Te Reo Māori Quiz
Main quiz function (only colours for now for testing)
Created by Janna Lei Eugenio
13/05/2022
"""

import random  # to select a random word from the list

# list containing the questions and answers
COLOURS = [["Mā", "white"], ["Whero", "red"], ["Kākāriki", "green"],
           ["Mangu", "black"], ["Pango", "black"], ["Kōwhai", "yellow"],
           ["Parauri", "brown"], ["Kikorangi", "blue"], ["Karaka", "orange"],
           ["Waiporoporo", "purple"], ["Kiwikiwi", "grey"]]
total = len(COLOURS)  # total number of questions

for i in COLOURS:  # for testing
    print(i)
print()

# count up the amount of correct answers
correct_answers = 0

# main routine
while COLOURS:
    # Asks the question
    question = random.choice(COLOURS)  # select a random colour from list
    print(question[0])
    COLOURS.remove(question)

    # User inputs an answer
    answer = input().lower()
    if answer == question[1]:
        print("correct\n")
        correct_answers += 1
        print(correct_answers)  # for testing
    else:
        print("incorrect")
        print(f"the correct number was {question[1]}\n")

# Score output
print(f"\nScore: {correct_answers}/{total}")
