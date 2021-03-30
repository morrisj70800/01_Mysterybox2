class History:
    def __init__(self, partner, game_history, game_stats):

        # disable history button
        partner.start_statistics_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Game Statistics",
                                 font=("Arial", "19", "bold",)
                                 )
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your Game Statistics. "
                                                           "Please use the export button to access the result",
                                  justify=LEFT, width=40, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Stating Balance (row 2)
        self.detail_frame = Frame(self.history_frame)
        self.detail_frame.grid(row=2)


        #Starting Balance row 2.0

        self.start_balance_label = Label(self.detail_frame,
                                         text="Starting Balance:",
                                         font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.detail_frame,
                                               font=content, text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0,column=1,padx=0)

        # Current Balance (row2.2)
        self.current_balance_label = Label (self.detail_frame,
                                            text="Current Balance:", font=heading,
                                            anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label= Label(self.detail_frame, font=content,text="${}".format(game_stats[1]),
                                                anchor="w")
        self.current_balance_value_label.grid(row=1,column=1,padx=0)

        if game_stats[1] >= game_stats[0]:
            win_loss = "Amount won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "red"

        # Amount won/ lost (row 2.3)
        self.wind_loss_label = Label(self.detail_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.detail_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2 ,column=1 ,padx=0)

        # Rounds Played (row2.4)
        self.games_played_label = Label(self.detail_frame,
                                        text="Rounds Played:", font=heading,
                                        anchor="e")
        self.games_played_label.grid(row=4,column=0,padx=0)

        self.games_played_value_label = Label(self.detail_frame, font=content,
                                              text=len(game_history), anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Export / Dismiss Buttons Frame (Row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 15 bold", bg="darkblue",fg="white",
                                    command=partial(lambda: self.export(game_history,game_stats)))
        self.export_button.grid(row=0, column=0,padx=5)

        if len(game_history) == 0:
            self.export_button.config(state=DISABLED)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 15 bold",bg="maroon",fg="white",
                                    command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.start_statistics_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, game_history, all_game_stats):
        Export(self, game_history, all_game_stats)