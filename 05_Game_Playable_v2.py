from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # Set starting balance to amount entered by user at start of the game
        self.balance.set(starting_balance)

        # Get value of stakes (use it as a multiplier when calculating winnings
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open "
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back ="#b9ea96"
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text ="?\n", font=box_text,
                                 bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, columnn=0)

        self.prize2_label = Label(self.box_frame, text ="?\n", font=box_text,
                                 bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, columnn=1)

        self.prize3_label = Label(self.box_frame, text ="?\n", font=box_text,
                                 bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, columnn=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        # Balance label (row 4)

        start_text = "Game Cost: ${} \nHow Much " \
                     "will you win?".format(stakes * 5)

        self.balance_label(self.game_frame, font="Arial 12 bold",





    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_balance = self.balance.get()

        # Adjust the balance (subtract game cost and add pay out)
        # For testing purposes, just add 2
        current_balance += 2

        # set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit label so use can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))
