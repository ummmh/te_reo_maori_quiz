"""Component 3 of Te Reo Māori Quiz
third version - uses dictionaries instead of lists
Created by Janna Lei Eugenio
18/05/2022
"""

import random  # to select a random word from the list


# quiz function
def quiz(selection):
    # separate dictionaries relating to quiz selection
    colours = {"Mā": "white", "Whero": "red", "Kākāriki": "green",
               "Mangu / Pango": "black", "Kōwhai": "yellow",
               "Parauri": "brown", "Kikorangi": "blue", "Karaka": "orange",
               "Waiporoporo": "purple", "Kiwikiwi": "grey"}

    numbers = {'Tahi': ["one", "1"], 'Rua': ["two", "2"],
               'Toru': ["three", "3"], 'Whā': ["four", "4"],
               'Rima': ["five", "5"], 'Ono': ["six", "6"],
               'Whitu': ["seven", "7"], 'Waru': ["eight", "8"],
               'Iwa': ["nine", "9"], 'Tekau': ["ten", "10"]}

    days = {'Rāhina': "monday", 'Rātū': "tuesday", 'Rāapa': "wednesday",
            'Rāpare': "thursday", 'Rāmere': "friday", 'Rāhoroi': "saturday",
            'Rātapu': "sunday"}

    # which quiz user is playing
    if selection == "C":
        selection = colours
    elif selection == "N":
        selection = numbers
    elif selection == "D":
        selection = days

    # list containing the questions and answers
    questions = list(selection.items())
    random.shuffle(questions)

    # total number of questions
    total = len(questions)

    # count up the amount of correct answers
    correct_answers = 0

    # ask user questions
    for word in questions:
        # select a random word from dictionary
        question = word
        print(question[0])

        # User inputs an answer
        guess = input().lower()
        if guess in question[1]:
            print("correct\n")
            correct_answers += 1
        else:
            print("incorrect")
            print(f"the correct answer was {question[1]}\n")

    # Score output
    print(f"Score: {correct_answers}/{total}")


# main
# quiz input for testing - later will be based on the button on main GUI
quiz_selection = input("enter quiz selection: ").upper()
quiz(quiz_selection)
