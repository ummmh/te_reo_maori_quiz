"""Component 5 of Te Reo Māori Quiz
Combines 05_export_to_txt_v1 with 05_export_to_txt_v3
Source: https://www.quru99.com?reading-and-writing-files-in-python.html
Created by Janna Lei Eugenio
31/05/2022
"""

import random  # to select a random word from the list
import re  # need to import re in order to check if filename is valid


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

    days = [["Rāhina", "monday"], ["Rātū", "tuesday"], ["Rāapa", "wednesday"],
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

    # count up the amount of correct answers
    correct_answers = 0

    # collects the quiz answers and score, later to be converted to a .txt file
    history = ['Word in Māori - Word in english : Your answer']

    # ask user questions
    while questions:
        # Asks the question
        question = random.choice(questions)  # select a random colour from list
        print(question[0])
        questions.remove(question)

        # User inputs an answer
        answer = input().lower()
        try:
            if answer == question[1] or answer == question[2]:
                print("correct\n")
                correct_answers += 1
            else:
                print("incorrect")
                print(f"the correct answer was {question[1]}\n")
        except IndexError:
            print("incorrect")
            print(f"the correct answer was {question[1]}\n")
        history.append(f'{question[0]} - {question[1]} : {answer}')

    # Score output
    score = f'Score: {correct_answers}/{total}'
    history.append(score)
    export_to_txt(history)


def export_to_txt(data):
    list = data
    has_error = "yes"
    while has_error == "yes":
        has_error = "no"
        filename = input("Enter a filename: ")

        # regular expression to check name-can be upper or lower case letters,
        valid_char = "[A-Za-z0-9_]"  # numbers or underscores
        for letter in filename:
            if re.match(valid_char, letter):
                continue
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = f"no {letter}'s allowed"
            has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # describe problem
            print(f"Invalid filename - {problem}")
            print()
        else:
            print("You entered a valid filename")  # allow valid file name

    # add .txt suffix
    filename = filename + ".txt"

    # create file to hold data
    f = open(filename, "w+", encoding='utf-8')

    for item in list:
        f.write(item + "\n")

    # close file
    f.close()


# main
# quiz input for testing
quiz_selection = input("enter quiz selection: ").upper()
quiz(quiz_selection)
