from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Game:
    def __init__(self):

        # Formatting variables...
        self.game_stats_list =[50, 6]

        # In Actual program this is blank and is populated with user calculations
        self.round_stats_list =['silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'lead ($0) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'lead ($0) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10'
                                'silver ($4) | silver ($4) | lead ($0) - Cost: $10']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # History button (row 1)
        self.stats_button = Button(self.game_frame,
                                   text="Game Stats",
                                   font="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats))
        self.stats_button.grid(row=1)

        def to_stats(self, game_history, game_stats):
            GameStats(self, game_history, game_stats)


class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12 bold"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                            partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="game Statistic",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are you Game Statistics."
                                              "Please use the Export Button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justicfy=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid (row=1)

        # Starting balance (row 2)
        self.detalis_frame = Frame(self.stats_frame)
        self.detalis_frame.grid (row=2)

        # Starting balance (row 2.0)

        self.start_balance_label = Label(self.detalis_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.detalis_frame, font=content,
                                               text="${}".format(game_stats[0])
