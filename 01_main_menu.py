"""Component 1 of Te Reo Māori Quiz
Main menu GUI
Created by Janna Lei Eugenio
5/05/2022
"""

from tkinter import *
import random


# Main menu
class Main:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "white"

        # Main menu Screen GUI
        self.main_frame = Frame(width=300, height=300,
                                     bg=background_colour, pady=10)
        self.main_frame.grid()

        # Te Reo Māori Quiz Heading (row 0)
        self.temp_converter_label = Label(self.main_frame,
                                          text="Te Reo Māori Quiz",
                                          font="Helvetica 16 bold",
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Introduction (row 1)
        self.main_intro_label = Label(self.main_frame, text="",
                                      font="Helvetica 10",
                                      bg=background_colour)

        # Colours quiz button (row 2, column 0)
        self.colours_button = Button(self.main_frame, text="Colours",
                                     font="Helvetica 14", bg="#DAE8FC",
                                     padx=5, pady=1, command=print("colours"))
        self.colours_button.grid(row=1)

        # Numbers quiz button (row 2, column 1)
        self.numbers_button = Button(self.main_frame, text="Numbers 1-10",
                                     font="Helvetica 14", bg="#DAE8FC",
                                     padx=5, pady=1, command=print("numbers"))
        self.numbers_button.grid(row=1)

        # Days of the Week quiz button (row 2, column 2)
        self.days_button = Button(self.main_frame, text="Days of the Week",
                                  font="Helvetica 14", bg="#DAE8FC",
                                  padx=5, pady=1, command=print("days"))
        self.days_button.grid(row=1)


# MAIN ROUTINE
if __name__ == "__main__":
    root = Tk()
    root.title("Te Reo Māori Quiz")
    something = Main(root)
    root.mainloop()

