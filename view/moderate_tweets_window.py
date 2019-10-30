import tkinter as tk
import sys
sys.path.append('../')
from twitterio import TwitterIO
from twitter import Twitter
import test as Test

class ModerateTweetsWindow(tk.Frame):    
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.moderatedTweetsListbox = tk.Listbox(self, selectmode="single", width=150, height=20)
        self.moderatedTweets = self.getModeratedTweets()

        if self.moderatedTweets:
            self.instructionLabel = tk.Label(self, 
                                             text="Select a tweet, then click \"Accept\" or \"Reject\" depending on the content.", 
                                             pady=20)
            
            self.acceptButton = tk.Button(self, text="Accept", command=self.clickAcceptTweet)
            self.rejectButton = tk.Button(self, text="Reject", command=self.clickRejectTweet)
            
            for tweet in self.moderatedTweets:
                self.moderatedTweetsListbox.insert(self.moderatedTweets.index(tweet), tweet.getText())

            self.instructionLabel.grid(column=0, row=0)
            self.moderatedTweetsListbox.grid(column=0, row=1)
            self.acceptButton.grid(column=0, row=2, pady=10)
            self.rejectButton.grid(column=0, row=3)
        else:
            self.noTweetAvailableLabel = tk.Label(self, text="There are no tweets to moderate.", pady=40, font=("Arial", 18))
            self.noTweetAvailableLabel.grid(column=0, row=0)

    def getModeratedTweets(self):
        self.moderatedTweetsListbox.delete(0, 'end') # Haalt alle items uit listbox
        tweets = TwitterIO.get_tweets_from_file('tweets/tweets.json') # Haalt tweets uit bestand tweets.json
        return tweets

    def clickAcceptTweet(self):
        if len(self.moderatedTweetsListbox.curselection()) > 0: # Voert alleen uit als er daadwerkelijk een tweet is geselecteerd
            index = self.moderatedTweetsListbox.curselection()[0] # index van geselecteerde tweet
            twitter = Twitter()
            twitter.tweet(self.moderatedTweetsListbox.get(index)) # Tweet de tweet op twitter
            TwitterIO.remove_tweet_from_file('tweets/tweets.json', self.moderatedTweets[index].getId()) # Verwijder tweet uit tweets.json
            self.moderatedTweetsListbox.delete(index) #Verwijder tweet uit listbox
            self.moderatedTweets.pop(index) # Verwijderd tweet uit de moderatedTweets lijst
            
        

    def clickRejectTweet(self):
        if len(self.moderatedTweetsListbox.curselection()) > 0: # Voert alleen uit als er daadwerkelijk een tweet is geselecteerd
            index = self.moderatedTweetsListbox.curselection()[0] # index van geselecteerde tweet
            self.moderatedTweetsListbox.delete(index) # Verwijderd tweet uit listbox
            tweet = self.moderatedTweets[index]
            TwitterIO.add_tweet_to_file('log/log.json', tweet) # Voegt tweet toe aan log bestand
            TwitterIO.remove_tweet_from_file('tweets/tweets.json', self.moderatedTweets[index].getId()) # Verwijderd tweet uit tweets.json
            self.moderatedTweets.pop(index) # Verwijderd tweet uit de moderatedTweets lijst
    

