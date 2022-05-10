"""Component 2 of Te Reo Māori Quiz
Version 3 of the Quiz GUI - buttons are enabled again after quiz window is
dismissed
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
        Colours(self)

    def select_numbers(self):
        Numbers(self)

    def select_days(self):
        Days(self)


class Colours:
    def __init__(self, partner):
        background = "#F8CECC"  # light red

        # disables all quiz select buttons
        partner.colours_button.config(state=DISABLED)
        partner.numbers_button.config(state=DISABLED)
        partner.days_button.config(state=DISABLED)

        # Sets up child window
        self.colours_box = Toplevel()

        # when user dismisses quiz window - reactivates all buttons
        self.colours_box.protocol('WM_DELETE_WINDOW', partial(
            self.close_colours, partner))

        # Sets up GUI frame
        self.colours_frame = Frame(self.colours_box, bg=background, padx=10,
                                   pady=10)
        self.colours_frame.grid()

        # Quiz heading (row 0)
        self.colours_heading = Label(self.colours_frame, bg=background,
                                     text="Colours", font="Helvetica 16 bold")
        self.colours_heading.grid()

    # function to enable buttons on main menu
    def close_colours(self, partner):
        partner.colours_button.config(state=NORMAL)
        partner.numbers_button.config(state=NORMAL)
        partner.days_button.config(state=NORMAL)
        self.colours_box.destroy()


class Numbers:
    def __init__(self, partner):
        background = "#F5F5F5"  # off white

        # disables all quiz select buttons
        partner.colours_button.config(state=DISABLED)
        partner.numbers_button.config(state=DISABLED)
        partner.days_button.config(state=DISABLED)

        # Sets up child window
        self.numbers_box = Toplevel()

        # when user dismisses quiz window - reactivates all buttons
        self.numbers_box.protocol('WM_DELETE_WINDOW', partial(
            self.close_numbers, partner))

        # Sets up GUI frame
        self.numbers_frame = Frame(self.numbers_box, bg=background, padx=10,
                                   pady=10)
        self.numbers_frame.grid()

        # Quiz heading (row 0)
        self.numbers_heading = Label(self.numbers_frame, bg=background,
                                     text="Numbers 1-10",
                                     font="Helvetica 16 bold")
        self.numbers_heading.grid()

    # function to enable buttons on main menu
    def close_numbers(self, partner):
        partner.colours_button.config(state=NORMAL)
        partner.numbers_button.config(state=NORMAL)
        partner.days_button.config(state=NORMAL)
        self.numbers_box.destroy()


class Days:
    def __init__(self, partner):
        background = "#BAC8D3"  # light grey

        # disables all quiz select buttons
        partner.colours_button.config(state=DISABLED)
        partner.numbers_button.config(state=DISABLED)
        partner.days_button.config(state=DISABLED)

        # Sets up child window
        self.days_box = Toplevel()

        # when user dismisses quiz window - reactivates all buttons
        self.days_box.protocol('WM_DELETE_WINDOW', partial(
            self.close_days, partner))

        # Sets up GUI frame
        self.days_frame = Frame(self.days_box, bg=background, padx=10,
                                   pady=10)
        self.days_frame.grid()

        # Quiz heading (row 0)
        self.days_heading = Label(self.days_frame, bg=background,
                                     text="Numbers 1-10",
                                     font="Helvetica 16 bold")
        self.days_heading.grid()

    # function to enable buttons on main menu
    def close_days(self, partner):
        partner.colours_button.config(state=NORMAL)
        partner.numbers_button.config(state=NORMAL)
        partner.days_button.config(state=NORMAL)
        self.days_box.destroy()


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Māori Quiz")
    something = Main(root)
    root.mainloop()

