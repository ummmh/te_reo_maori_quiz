"""Component 3 of Te Reo Māori Quiz
second version - allows user to select which quiz to take
Created by Janna Lei Eugenio
17/05/2022
"""

import random  # to select a random word from the list


# quiz function
def quiz(selection):
    # separate lists relating to quiz selection
    colours = [["Mā", "white"], ["Whero", "red"], ["Kākāriki", "green"],
               ["Mangu", "black"], ["Pango", "black"], ["Kōwhai", "yellow"],
               ["Parauri", "brown"], ["Kikorangi", "blue"],
               ["Karaka", "orange"], ["Waiporoporo", "purple"],
               ["Kiwikiwi", "grey"]]

    numbers = [["Tahi", "one", "1"], ["Rua", "two", "2"],
               ["Toru", "three", "3"], ["Whā", "four", "4"],
               ["Rima", "five", "5"], ["Ono", "six", "6"],
               ["Whitu", "seven", "7"], ["Waru", "eight", "8"],
               ["Iwa", "nine", "9"], ["Tekau", "ten", "10"]]

    days = [["Rāhina", "monday"], ["Rātū", "Tuesday"], ["Rāapa", "wednesday"],
            ["Rāpare", "thursday"], ["Rāmere", "friday"],
            ["Rāhoroi", "saturday"], ["Rātapu", "sunday"]]

    # list containing the questions and answers
    questions = []

    if selection == "C":
        questions = colours
    elif selection == "N":
        questions = numbers
    elif selection == "D":
        questions = days

    # total number of questions
    total = len(questions)

    for item in questions:  # for testing
        print(item)
    print()

    # count up the amount of correct answers
    correct_answers = 0

    # ask user questions
    while questions:
        # Asks the question
        question = random.choice(questions)  # select a random colour from list
        print(question[0])
        questions.remove(question)

        # User inputs an answer
        answer = input().lower()
        if answer == question[1] or answer == question[2]:
            print("correct\n")
            correct_answers += 1
            #print(f"correct answers = {correct_answers}")  # for testing
        else:
            print("incorrect")
            print(f"the correct number was {question[1]}\n")
            #print(f"correct answers = {correct_answers}")  # for testing

    # Score output
    print(f"Score: {correct_answers}/{total}")


# main
# quiz input for testing - later will be based on the button on main GUI
quiz_selection = input("enter quiz selection: ").upper()
quiz(quiz_selection)
