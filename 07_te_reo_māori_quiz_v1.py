"""Assembled Te Reo Māori Quiz
version 1 (based off of 06_export_gui_v2) - has not been tested yet
Created by Janna Lei Eugenio
3/06/2022
"""

import tkinter as tk
from tkinter import *
import random  # to select a random word from the list
import re  # need to import re in order to check if filename is valid

history = []  # history list to collect results to be exported to txt file


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
        for p in (MainMenu, Colours, Numbers, Days, Export):
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
                                   padx=70, pady=24)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Te Reo Māori Quiz Heading (row 0)
        self.main_heading = tk.Label(self.main_frame, text="Te Reo Māori Quiz",
                                     font="Helvetica 16 bold",
                                     bg=background_colour)
        self.main_heading.grid(row=0)

        # Introduction (row 1) - filler text for now
        self.main_intro_label = tk.Label(self.main_frame,
                                         text="Welcome!\nPlease press a button"
                                              " to start!",
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
                                        text="Numbers",  # off white
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
        self.colours_frame = tk.Frame(self, bg=background, padx=48, pady=30)
        self.colours_frame.grid()

        # Quiz heading (row 0)
        self.colours_heading = tk.Label(self.colours_frame,
                                        font="Helvetica 16 bold",
                                        bg=background, text="Colours")
        self.colours_heading.grid(row=0, column=1)

        # Quiz instructions (row 1)
        self.colours_text = tk.Label(self.colours_frame, font="Helvetica 10",
                                     bg=background, text="This is the colours "
                                                         "quiz\nWhen you start"
                                                         " the quiz, a random "
                                                         "colour will be "
                                                         "diplayed in Māori"
                                                         "\nType the english "
                                                         "translation in the "
                                                         "textbox and hit "
                                                         "enter")
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

        # Export button (column 2) - (hidden until the quiz is finished)
        self.export_button = tk.Button(self.buttons_frame, font="Helvetica 14",
                                       bg="#647687", fg="white",
                                       text="Export Score", command=lambda:
                                       controller.show_page('Export'))

    def start_quiz(self):
        # changes the format of the window
        self.colours_frame.configure(padx=180, pady=34)
        self.colours_text.configure(font="Helvetica 14", text="question")
        # gets rid of the start and back button
        self.back_bttn.grid_remove()
        self.start_button.grid_remove()
        self.export_button.grid_remove()

        # adds an entry box
        self.answer_box = tk.Entry(self.buttons_frame)
        self.answer_box.grid()

        self.answer_button = tk.Button(self.buttons_frame, bg="white",
                                       font="Helvetica 14", text="Enter")
        self.answer_button.grid(row=1)

        quiz("C", self.colours_text, self.answer_button, self.answer_box,
             self.back_bttn, self.start_button, self.export_button,
             self.colours_frame)


class Numbers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#F5F5F5"  # background = off white

        # Quiz frame
        self.numbers_frame = tk.Frame(self, bg=background, padx=12, pady=30)
        self.numbers_frame.grid()

        # Quiz heading (row 0)
        self.numbers_heading = tk.Label(self.numbers_frame,
                                        font="Helvetica 16 bold",
                                        bg=background, text="Numbers")
        self.numbers_heading.grid(row=0, column=1)

        # Quiz instructions (row 1)
        self.numbers_text = tk.Label(self.numbers_frame, font="Helvetica 10",
                                     bg=background, text="This is the numbers"
                                                         " quiz\nWhen you "
                                                         "start the quiz, a"
                                                         " random number from"
                                                         " 1-10 will be"
                                                         " displayed in Māori"
                                                         "\nType the number or"
                                                         " english translation"
                                                         " in the textbox and"
                                                         " hit enter")
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

        # Export button (column 2) - (hidden until the quiz is finished)
        self.export_button = tk.Button(self.buttons_frame, font="Helvetica 14",
                                       bg="#647687", fg="white",
                                       text="Export Score", command=lambda:
                                       controller.show_page('Export'))

    def start_quiz(self):
        # changes the format of the window
        self.numbers_frame.configure(padx=181, pady=34)
        self.numbers_text.configure(font="Helvetica 14", text="question")
        # gets rid of the start and back button
        self.back_bttn.grid_remove()
        self.start_button.grid_remove()
        self.export_button.grid_remove()

        # adds an entry box
        self.answer_box = tk.Entry(self.buttons_frame)
        self.answer_box.grid()

        self.answer_button = tk.Button(self.buttons_frame, bg="white",
                                       font="Helvetica 14", text="Enter")
        self.answer_button.grid(row=1)

        quiz("N", self.numbers_text, self.answer_button, self.answer_box,
             self.back_bttn, self.start_button, self.export_button,
             self.numbers_frame)


class Days(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#BAC8D3"  # background = light grey

        # Quiz frame
        self.days_frame = tk.Frame(self, bg=background, padx=52, pady=30)
        self.days_frame.grid()

        # Quiz heading (row 0)
        self.days_heading = tk.Label(self.days_frame, font="Helvetica 16 bold",
                                     bg=background, text="Days of the Week")
        self.days_heading.grid(row=0, column=1)

        # Quiz instructions (row 1)
        self.days_text = tk.Label(self.days_frame, font="Helvetica 10",
                                  bg=background, text="This is the days of the"
                                                      " week quiz\nWhen you"
                                                      " start the quiz, a"
                                                      " random day will be"
                                                      " displayed in Māori"
                                                      "\nType the english "
                                                      "translation in the "
                                                      "textbox and hit enter")
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

        # Export button (column 2) - (hidden until the quiz is finished)
        self.export_button = tk.Button(self.buttons_frame, font="Helvetica 14",
                                       bg="#647687", fg="white",
                                       text="Export Score", command=lambda:
                                       controller.show_page('Export'))

    def start_quiz(self):
        # changes the format of the window
        self.days_frame.configure(padx=151, pady=34)
        self.days_text.configure(font="Helvetica 14", text="question")
        # gets rid of the start and back button
        self.back_bttn.grid_remove()
        self.start_button.grid_remove()
        self.export_button.grid_remove()
        # adds an entry box
        self.answer_box = tk.Entry(self.buttons_frame)
        self.answer_box.grid()

        self.answer_button = tk.Button(self.buttons_frame, bg="white",
                                       font="Helvetica 14", text="Enter")
        self.answer_button.grid(row=1)

        quiz("D", self.days_text, self.answer_button, self.answer_box,
             self.back_bttn, self.start_button, self.export_button,
             self.days_frame)


class Export(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#647687"  # dark grey

        # Export frame
        self.export_frame = tk.Frame(self, bg=background, padx=99, pady=10)
        self.export_frame.grid()

        # Export Heading (row 0)
        self.export_heading = tk.Label(self.export_frame, bg=background,
                                       fg="white", font="Helvetica 16 bold",
                                       text="Export")
        self.export_heading.grid(row=0)

        # Export instructions (row 1)
        self.export_instructions = tk.Label(self.export_frame, bg=background,
                                            fg="white", font="Helvetica 10",
                                            text="Please enter a file name - "
                                                 "your answers and quiz\n"
                                                 "results will be exported to "
                                                 "a text file and will\nappear"
                                                 " in the same folder as this"
                                                 " program")
        self.export_instructions.grid(row=1)

        # File name entry (row 2)
        self.filename_entry = tk.Entry(self.export_frame)
        self.filename_entry.grid(row=2)

        # Buttons frame (row 3)
        self.export_buttons_frame = tk.Frame(self.export_frame, bg=background,
                                             pady=10)
        self.export_buttons_frame.grid(row=3)

        # Back button (column 0)
        self.back_bttn = tk.Button(self.export_buttons_frame, bg="white",
                                   font="Helvetica 14",
                                   text="Back to Main Menu",
                                   command=lambda:
                                   controller.show_page('MainMenu'))
        self.back_bttn.grid(row=0, column=0)

        # Export button (column 1)                       button colour is grey
        self.export_bttn = tk.Button(self.export_buttons_frame, bg="#BAC8D3",
                                     font="Helvetica 14", text="Export",
                                     command=lambda:
                                     self.export_to_txt(history))
        self.export_bttn.grid(row=0, column=1)

    def export_to_txt(self, data):
        # reg expression to check name-can be upper or lower case letters,
        valid_char = "[A-Za-z0-9_]"  # numbers or underscores
        has_error = "no"
        filename = self.filename_entry.get()
        print(filename)  # for testing purposes

        for letter in filename:
            if re.match(valid_char, letter):  # if the filename is valid
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
            # displays the error
            self.export_instructions.configure(
                text=f"Invalid filename - {problem}")
            # changes the entry colour
            self.filename_entry.configure(bg="red")
        else:
            # add .txt suffix
            filename = filename + ".txt"
            # create file to hold data
            f = open(filename, "w+", encoding='utf-8')
            # writes the data to a text file
            for item in data:
                f.write(item + "\n")
            # close file
            f.close()

            # 'closes' the export page
            self.controller.show_page('MainMenu')


# quiz function
def quiz(selection, q_displayed, enter, entry_box, back, start, export, frame):
    global history
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
    history.append('Word in Māori - Word in english : Your answer')

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
    export.grid(row=0, column=2)  # reveals the export button
    frame.configure(padx=32, pady=43)  # makes frame go back to normal size


# function to check if answer is correct
def check_answer(entry, question, correct, variable, data):
    answer = entry.get().lower()
    try:
        if answer == question[1] or answer == question[2]:
            entry.configure(bg="lime")
            correct.append(1)  # adds an item to correct answers
        else:
            entry.configure(bg="red", fg="white")
    except IndexError:
        entry.configure(bg="red", fg="white")
    data.append(f'{question[0]} - {question[1]} : {answer}')  # adds result to
    entry.delete(0, END)  # clears the entry box                history
    variable.set(1)  # allows the loop to continue


# MAIN ROUTINE
if __name__ == "__main__":
    root = MainWindow()
    root.title("Te Reo Māori Quiz")
    root.mainloop()
