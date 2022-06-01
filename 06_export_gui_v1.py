"""Component 5 of Te Reo Māori Quiz
Export GUI after finishing a quiz - Incorporates 05_export_gui_v4
into 04_quiz_gui_v11
Created by Janna Lei Eugenio
1/06/2022
"""

import tkinter as tk
from tkinter import *
import random  # to select a random word from the list
import re  # need to import re in order to check if filename is valid


# Main window
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # main frame where all the pages are stored
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        # stores the pages
        self.pages = {}

        # adds all the classes to pages so can be shown
        for p in (MainMenu, Colours, Numbers, Days):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.pages[page_name] = frame
        self.show_page("MainMenu")

    # function to change pages
    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()


# Main menu
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Formatting variables
        background_colour = "white"

        # Main menu Screen GUI
        self.main_frame = tk.Frame(self, bg=background_colour,
                                   padx=10, pady=10)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Te Reo Māori Quiz Heading (row 0)
        self.main_heading = tk.Label(self.main_frame, text="Te Reo Māori Quiz",
                                     font="Helvetica 16 bold",
                                     bg=background_colour)
        self.main_heading.grid(row=0)

        # Introduction (row 1) - filler text for now
        self.main_intro_label = tk.Label(self.main_frame,
                                         text="(introduction)",
                                         font="Helvetica 10", pady=5,
                                         bg=background_colour)
        self.main_intro_label.grid(row=1)

        # Quiz select button frame (row 2)
        self.quiz_select_buttons_frame = tk.Frame(self.main_frame, pady=10,
                                                  bg=background_colour)
        self.quiz_select_buttons_frame.grid(row=2)

        # Colours quiz button (row 2, column 0)
        self.colours_button = tk.Button(self.quiz_select_buttons_frame,
                                        text="Colours", font="Helvetica 14",
                                        bg="#F8CECC",  # light red
                                        command=lambda:
                                        controller.show_page("Colours"))
        self.colours_button.grid(row=0, column=0)

        # Numbers quiz button (row 2, column 1)
        self.numbers_button = tk.Button(self.quiz_select_buttons_frame,
                                        text="Numbers 1-10",  # off white
                                        font="Helvetica 14", bg="#F5F5F5",
                                        command=lambda:
                                        controller.show_page("Numbers"))
        self.numbers_button.grid(row=0, column=1)

        # Days of the Week quiz button (row 2, column 2)
        self.days_button = tk.Button(self.quiz_select_buttons_frame,
                                     text="Days of the Week",  # light grey
                                     font="Helvetica 14", bg="#BAC8D3",
                                     command=lambda:
                                     controller.show_page("Days"))
        self.days_button.grid(row=0, column=2)


# Quiz GUI
class Colours(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#F8CECC"  # background = light red

        # Quiz frame
        self.colours_frame = tk.Frame(self, bg=background, padx=68, pady=25)
        self.colours_frame.grid()

        # Quiz heading (row 0)
        self.colours_heading = tk.Label(self.colours_frame,
                                        font="Helvetica 16 bold",
                                        bg=background, text="Colours")
        self.colours_heading.grid(row=0, column=1)

        # Quiz instructions (row 1)
        self.colours_text = tk.Label(self.colours_frame, font="Helvetica 10",
                                     bg=background, text="(intro)")
        self.colours_text.grid(row=1, column=1)

        # Button frame (row 2)
        self.buttons_frame = tk.Frame(self.colours_frame, bg=background)
        self.buttons_frame.grid(row=2, column=1)

        # Back button (column 0)
        self.back_bttn = tk.Button(self.buttons_frame, font="Helvetica 14",
                                   bg="white", text="Back to Main Menu",
                                   command=lambda:
                                   controller.show_page("MainMenu"))
        self.back_bttn.grid(row=0, column=0)

        # Start quiz button (column 1)
        self.start_button = tk.Button(self.buttons_frame, font="Helvetica 14",
                                      bg="white", text="Start Quiz",
                                      command=self.start_quiz)
        self.start_button.grid(row=0, column=1)

    def start_quiz(self):
        # changes the format of the window
        self.colours_frame.configure(padx=143, pady=32)
        self.colours_text.configure(font="Helvetica 14", text="question")
        # gets rid of the start and back button
        self.back_bttn.grid_remove()
        self.start_button.grid_remove()

        # adds an entry box
        self.answer_box = tk.Entry(self.buttons_frame)
        self.answer_box.grid()

        self.answer_button = tk.Button(self.buttons_frame, bg="white",
                                       font="Helvetica 14", text="Enter")
        self.answer_button.grid(row=1)

        quiz("C", self.colours_text, self.answer_button, self.answer_box,
             self.back_bttn, self.start_button, self.colours_frame)


class Numbers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#F5F5F5"  # background = off white

        # Quiz frame
        self.numbers_frame = tk.Frame(self, bg=background, padx=68, pady=25)
        self.numbers_frame.grid()

        # Quiz heading (row 0)
        self.numbers_heading = tk.Label(self.numbers_frame,
                                        font="Helvetica 16 bold",
                                        bg=background, text="Numbers 1-10")
        self.numbers_heading.grid(row=0, column=1)

        # Quiz instructions (row 1)
        self.numbers_text = tk.Label(self.numbers_frame, font="Helvetica 10",
                                     bg=background, text="(intro)")
        self.numbers_text.grid(row=1, column=1)

        # Button frame (row 2)
        self.buttons_frame = tk.Frame(self.numbers_frame, bg=background)
        self.buttons_frame.grid(row=2, column=1)

        # Back button (column 0)
        self.back_bttn = tk.Button(self.buttons_frame, font="Helvetica 14",
                                   bg="white", text="Back to Main Menu",
                                   command=lambda:
                                   controller.show_page("MainMenu"))
        self.back_bttn.grid(row=0, column=0)

        # Start quiz button (column 1)
        self.start_button = tk.Button(self.buttons_frame, font="Helvetica 14",
                                      bg="white", text="Start Quiz",
                                      command=self.start_quiz)
        self.start_button.grid(row=0, column=1)

    def start_quiz(self):
        # changes the format of the window
        self.numbers_frame.configure(padx=131, pady=32)
        self.numbers_text.configure(font="Helvetica 14", text="question")
        # gets rid of the start and back button
        self.back_bttn.grid_remove()
        self.start_button.grid_remove()

        # adds an entry box
        self.answer_box = tk.Entry(self.buttons_frame)
        self.answer_box.grid()

        self.answer_button = tk.Button(self.buttons_frame, bg="white",
                                       font="Helvetica 14", text="Enter")
        self.answer_button.grid(row=1)

        quiz("N", self.numbers_text, self.answer_button, self.answer_box,
             self.back_bttn, self.start_button, self.numbers_frame)


class Days(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#BAC8D3"  # background = light grey

        # Quiz frame
        self.days_frame = tk.Frame(self, bg=background, padx=68, pady=25)
        self.days_frame.grid()

        # Quiz heading (row 0)
        self.days_heading = tk.Label(self.days_frame, font="Helvetica 16 bold",
                                     bg=background, text="Days of the Week")
        self.days_heading.grid(row=0, column=1)

        # Quiz instructions (row 1)
        self.days_text = tk.Label(self.days_frame, font="Helvetica 10",
                                  bg=background, text="(intro)")
        self.days_text.grid(row=1, column=1)

        # Button frame (row 2)
        self.buttons_frame = tk.Frame(self.days_frame, bg=background)
        self.buttons_frame.grid(row=2, column=1)

        # Back button (column 0)
        self.back_bttn = tk.Button(self.buttons_frame, font="Helvetica 14",
                                   bg="white", text="Back to Main Menu",
                                   command=lambda:
                                   controller.show_page("MainMenu"))
        self.back_bttn.grid(row=0, column=0)

        # Start quiz button (column 1)
        self.start_button = tk.Button(self.buttons_frame, font="Helvetica 14",
                                      bg="white", text="Start Quiz",
                                      command=self.start_quiz)
        self.start_button.grid(row=0, column=1)

    def start_quiz(self):
        # changes the format of the window
        self.days_frame.configure(padx=114, pady=32)
        self.days_text.configure(font="Helvetica 14", text="question")
        # gets rid of the start and back button
        self.back_bttn.grid_remove()
        self.start_button.grid_remove()
        # adds an entry box
        self.answer_box = tk.Entry(self.buttons_frame)
        self.answer_box.grid()

        self.answer_button = tk.Button(self.buttons_frame, bg="white",
                                       font="Helvetica 14", text="Enter")
        self.answer_button.grid(row=1)

        quiz("D", self.days_text, self.answer_button, self.answer_box,
             self.back_bttn, self.start_button, self.days_frame)


# quiz function
def quiz(selection, q_displayed, enter, entry_box, back, start, frame):
    rounds = tk.IntVar()  # variable to make loop wait for button press
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
    # selects which list to use
    if selection == "C":
        questions = colours
    elif selection == "N":
        questions = numbers
    elif selection == "D":
        questions = days

    # total number of questions
    total = len(questions)

    # count up the amount of correct answers
    correct_answers = []

    # collects the quiz answers and score, later to be converted to a .txt file
    history = ['Word in Māori - Word in english : Your answer']

    # ask user questions
    while questions:
        # Asks the question
        question = random.choice(questions)  # select a random colour from list
        q_displayed.configure(text=question[0])
        questions.remove(question)

        # User inputs an answer
        enter.configure(command=lambda: check_answer(entry_box, question,
                                                     correct_answers, rounds,
                                                     history))
        enter.wait_variable(rounds)  # loop waits until button is pressed

    score = f'Score: {len(correct_answers)}/{total}'
    history.append(score)  # adds score to history

    # Score output
    q_displayed.configure(text=score)
    # gets rid of entry button and enter box
    enter.destroy()
    entry_box.destroy()
    # adds back the back to main menu button and start button for replay
    back.grid()
    start.grid()
    start.configure(text="Replay Quiz")
    frame.configure(padx=68, pady=25) # makes frame go back to normal size


# function to check if answer is correct
def check_answer(entry, question, correct, variable, data):
    answer = entry.get().lower()
    try:
        if answer == question[1] or answer == question[2]:
            entry.configure(bg="lime", fg="black")
            correct.append(1)  # adds an item to correct answers
        else:
            entry.configure(bg="red", fg="white")
    except IndexError:
        entry.configure(bg="red", fg="white")
    data.append(f'{question[0]} - {question[1]} : {answer}')  # adds result to
    entry.delete(0, END)  # clears the entry box                history
    variable.set(1)  # allows the loop to continue


# function to export results and score after quiz
def export_to_txt(data):
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

    for item in data:
        f.write(item + "\n")

    # close file
    f.close()


# MAIN ROUTINE
if __name__ == "__main__":
    root = MainWindow()
    root.title("Te Reo Māori Quiz")
    root.mainloop()
