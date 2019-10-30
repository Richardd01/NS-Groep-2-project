import tkinter as tk
from view.moderate_tweets_window import ModerateTweetsWindow
from view.show_tweets_window import ShowTweetsWindow


class StartWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.screenTitleLabel = tk.Label(self, text="NS Tweets: management", pady=40, font=("Arial", 18))
        self.displayTweetsButton = tk.Button(self, text="Display latest tweets",
                                        command=lambda: master.switchFrame(ShowTweetsWindow))
        self.moderateTweetsButton = tk.Button(self, text="Moderate tweets",
                                         command=lambda: master.switchFrame(ModerateTweetsWindow))

        self.screenTitleLabel.grid(column=0, row=1)
        self.displayTweetsButton.grid(column=0, row=2)
        self.moderateTweetsButton.grid(column=0, row=3)     