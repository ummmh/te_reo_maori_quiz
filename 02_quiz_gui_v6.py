"""Component 2 of Te Reo Māori Quiz
Version 6 of the Quiz GUI - improved version of version 5
Created by Janna Lei Eugenio
12/05/2022
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

        # adds all the classes to pages so can be shown
        for p in (MainMenu, Colours, Numbers, Days):
            page_name = p.__name__
            frame = p(parent=container, controller=self)
            frame.grid(row=0, column=0)
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
        self.colours_frame = tk.Frame(bg=background)
        self.colours_frame.grid(row=0, column=0, sticky="nsew")

        # Quiz heading (row 0)
        self.colours_heading = tk.Label(self.colours_frame,
                                        font="Helvetica 16 bold",
                                        bg=background, text="Colours")
        self.colours_heading.grid(row=0)

        # Quiz instructions (row 1)
        self.colours_text = tk.Label(self.colours_frame, font="Helvetica 10",
                                     bg=background, text="(intro)")
        self.colours_text.grid(row=1)

        # Back button (row 2)
        self.back_bttn = tk.Button(self.colours_frame, font="Helvetica 14",
                                   bg="white", text="Back to Main Menu",
                                   command=controller.show_page("MainMenu"))
        self.back_bttn.grid(row=2)


class Numbers(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#F5F5F5"  # background = off white

        # Quiz frame
        self.numbers_frame = tk.Frame(bg=background)
        self.numbers_frame.grid(row=0, column=0, sticky="nsew")

        # Quiz heading (row 0)
        self.numbers_heading = tk.Label(self.numbers_frame,
                                        font="Helvetica 16 bold",
                                        bg=background, text="Colours")
        self.numbers_heading.grid(row=0)

        # Quiz instructions (row 1)
        self.numbers_text = tk.Label(self.numbers_frame, font="Helvetica 10",
                                     bg=background, text="(intro)")
        self.numbers_text.grid(row=1)

        # Back button (row 2)
        self.back_bttn = tk.Button(self.numbers_frame, font="Helvetica 14",
                                   bg="white", text="Back to Main Menu",
                                   command=controller.show_page("MainMenu"))
        self.back_bttn.grid(row=2)


class Days(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background = "#BAC8D3"  # background = light grey

        # Quiz frame
        self.days_frame = tk.Frame(bg=background)
        self.days_frame.grid(row=0, column=0, sticky="nsew")

        # Quiz heading (row 0)
        self.days_heading = tk.Label(self.days_frame, font="Helvetica 16 bold",
                                     bg=background, text="Colours")
        self.days_heading.grid(row=0)

        # Quiz instructions (row 1)
        self.days_text = tk.Label(self.days_frame, font="Helvetica 10",
                                  bg=background, text="(intro)")
        self.days_text.grid(row=1)

        # Back button (row 2)
        self.back_bttn = tk.Button(self.days_frame, font="Helvetica 14",
                                   bg="white", text="Back to Main Menu",
                                   command=self.controller.show_page("MainMenu"))
        self.back_bttn.grid(row=2)


# MAIN ROUTINE
if __name__ == "__main__":
    root = MainWindow()
    root.title("Te Reo Māori Quiz")
    root.mainloop()
