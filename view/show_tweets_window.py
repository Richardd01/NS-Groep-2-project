import tkinter as tk
from tkinter.messagebox import showinfo
import sys
import json
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
        """
        Update tweets elke 2 minuten
        """
        latestTweets = self.formatTweets(self.getLatestTweets())
        self.latestTweetsLabel.configure(text="{}".format(latestTweets))
        self.after(120000, self.updateTweets) # Elke 2 minuten ververst pagina zich. API Limit: 15 / 15 minuten

    def getLatestTweets(self):
        """
        Haalt laatste 5 tweets van timeline
        :return: List(text)
        """
        #twitter = Twitter()
        data = Twitter().get_tweets_from_timeline(5)
        if data.status_code != 200:
            error_message = json.loads(data.text)['errors'][0]['message']
            showinfo(title='Error', message=error_message)
        tweets = []
        for tweet in data:
            tweets.append(tweet['text'])
        return tweets

    def formatTweets(self, unformattedTweets):
        """
        Maakt van list met strings één lange string met \n als seperator
        :return: str
        """
        return "\n".join(unformattedTweets)