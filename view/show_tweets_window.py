import tkinter as tk
import sys
sys.path.append('../')
from twitter import Twitter

class ShowTweetsWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.screenTitleLabel = tk.Label(self, text="Latest tweets", pady=40, font=("Arial", 36))
        self.latestTweets = self.formatTweets(self.getLatestTweets())
        self.latestTweetsLabel = tk.Label(self, text="{}".format(self.latestTweets), font=("Arial", 28))

        self.screenTitleLabel.grid(column=0, row=0)
        self.latestTweetsLabel.grid(column=0, row=1)

        self.updateTweets()
    
    def updateTweets(self):
        latestTweets = self.formatTweets(self.getLatestTweets())
        self.latestTweetsLabel.configure(text="{}".format(latestTweets))
        self.after(10000, self.updateTweets)

    def getLatestTweets(self):
        twitter = Twitter()
        return twitter.get_tweets_from_timeline(5)

    def formatTweets(self, unformattedTweets):
        return "\n".join(unformattedTweets)