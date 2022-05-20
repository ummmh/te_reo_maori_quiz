"""Component 2 of Te Reo Māori Quiz
Version 5 of the Quiz GUI - trialling component so that instead of generating a
new quiz window, it changes the main page
Created by Janna Lei Eugenio
11/05/2022
"""

import tkinter as tk
from tkinter import *


# Main window
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # main frame where all the pages are stored
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        # stores the pages
        self.pages = {}

        for p in (MainMenu, Quiz):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0)
            self.pages[page_name] = frame

        self.show_page('MainMenu')

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
        self.main_frame.grid()

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
                                        command=self.select_colours)
        self.colours_button.grid(row=0, column=0)

        # Numbers quiz button (row 2, column 1)
        self.numbers_button = tk.Button(self.quiz_select_buttons_frame,
                                        text="Numbers 1-10",  # off white
                                        font="Helvetica 14", bg="#F5F5F5",
                                        command=self.select_numbers)
        self.numbers_button.grid(row=0, column=1)

        # Days of the Week quiz button (row 2, column 2)
        self.days_button = tk.Button(self.quiz_select_buttons_frame,
                                     text="Days of the Week",  # light grey
                                     font="Helvetica 14", bg="#BAC8D3",
                                     command=self.select_days)
        self.days_button.grid(row=0, column=2)

    def select_colours(self):
        open_quiz = self.controller.show_page(Quiz)
        # Changes heading and background to match button
        open_quiz.quiz_box.configure(bg="#F8CECC")  # background = light red
        open_quiz.quiz_heading.configure(bg="#F8CECC", text="Colours")

    def select_numbers(self):
        open_quiz = self.controller.show_page(Quiz)
        # Changes heading and background to match button
        open_quiz.quiz_box.configure(bg="#F5F5F5")  # background = off white
        open_quiz.quiz_heading.configure(bg="#F5F5F5", text="Numbers 1-10")

    def select_days(self):
        open_quiz = self.controller.show_page(Quiz)
        # Changes heading and background to match button
        open_quiz.quiz_frame.configure(bg="#BAC8D3")  # background = light grey
        open_quiz.quiz_heading.configure(bg="#BAC8D3", text="Days of the Week")


# Quiz GUI
class Quiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Quiz frame
        self.quiz_frame = tk.Frame(width=500, height=500)

        # Quiz heading (row 0)
        self.quiz_heading = tk.Label(self, font="Helvetica 16 bold")
        self.quiz_heading.grid(row=0)


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Māori Quiz")
    root.mainloop()
