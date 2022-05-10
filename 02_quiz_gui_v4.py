"""Component 2 of Te Reo Māori Quiz
Version 3 of the Quiz GUI - development so that theres one class to display the
the quiz window
Created by Janna Lei Eugenio
10/05/2022
"""

from tkinter import *
from functools import partial  # to prevent unwanted windows


# Main menu
class Main:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "white"

        # Main menu Screen GUI
        self.main_frame = Frame(bg=background_colour, padx=10, pady=10)
        self.main_frame.grid()

        # Te Reo Māori Quiz Heading (row 0)
        self.main_heading = Label(self.main_frame, text="Te Reo Māori Quiz",
                                  font="Helvetica 16 bold",
                                  bg=background_colour)
        self.main_heading.grid(row=0)

        # Introduction (row 1) - filler text for now
        self.main_intro_label = Label(self.main_frame, text="(introduction)",
                                      font="Helvetica 10", pady=5,
                                      bg=background_colour)
        self.main_intro_label.grid(row=1)

        # Quiz select button frame (row 2)
        self.quiz_select_buttons_frame = Frame(self.main_frame, pady=10,
                                               bg=background_colour)
        self.quiz_select_buttons_frame.grid(row=2)

        # Colours quiz button (row 2, column 0)
        self.colours_button = Button(self.quiz_select_buttons_frame,
                                     text="Colours", font="Helvetica 14",
                                     bg="#F8CECC",  # light red
                                     command=self.select_colours)
        self.colours_button.grid(row=0, column=0)

        # Numbers quiz button (row 2, column 1)
        self.numbers_button = Button(self.quiz_select_buttons_frame,
                                     text="Numbers 1-10", font="Helvetica 14",
                                     bg="#F5F5F5",  # off white
                                     command=self.select_numbers)
        self.numbers_button.grid(row=0, column=1)

        # Days of the Week quiz button (row 2, column 2)
        self.days_button = Button(self.quiz_select_buttons_frame,
                                  text="Days of the Week", font="Helvetica 14",
                                  bg="#BAC8D3",  # light grey
                                  command=self.select_days)
        self.days_button.grid(row=0, column=2)

    def select_colours(self):
        open_quiz = Quiz(self)
        # Changes heading and background to match button
        open_quiz.quiz_box.configure(bg="#F8CECC")  # background = light red
        open_quiz.quiz_heading.configure(bg="#F8CECC", text="Colours")

    def select_numbers(self):
        open_quiz = Quiz(self)
        # Changes heading and background to match button
        open_quiz.quiz_box.configure(bg="#F5F5F5")  # background = off white
        open_quiz.quiz_heading.configure(bg="#F5F5F5", text="Numbers 1-10")

    def select_days(self):
        open_quiz = Quiz(self)
        # Changes heading and background to match button
        open_quiz.quiz_box.configure(bg="#BAC8D3")  # background = light grey
        open_quiz.quiz_heading.configure(bg="#BAC8D3", text="Days of the Week")


class Quiz:
    def __init__(self, partner):
        # Disables all quiz select buttons
        partner.colours_button.config(state=DISABLED)
        partner.numbers_button.config(state=DISABLED)
        partner.days_button.config(state=DISABLED)

        # Sets up child window
        self.quiz_box = Toplevel(width=500, height=500)

        # When user dismisses quiz window - reactivates all buttons
        self.quiz_box.protocol('WM_DELETE_WINDOW', partial(
            self.close_quiz, partner))

        # Quiz heading (row 0)
        self.quiz_heading = Label(self.quiz_box, font="Helvetica 16 bold")
        self.quiz_heading.grid(row=0)

    # Function to enable buttons on main menu
    def close_quiz(self, partner):
        partner.colours_button.config(state=NORMAL)
        partner.numbers_button.config(state=NORMAL)
        partner.days_button.config(state=NORMAL)
        self.quiz_box.destroy()


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Māori Quiz")
    something = Main(root)
    root.mainloop()

