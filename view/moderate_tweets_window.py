import tkinter as tk
from tkinter.messagebox import showinfo
import sys
import json
sys.path.append('../')
from twitterio import TwitterIO
from twitter import Twitter

class ModerateTweetsWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.tweets = []
        self.moderatedTweetsListbox = tk.Listbox(self, selectmode="single", width=150, height=20)
        self.moderatedTweets = self.getModeratedTweets()
        self.getTweetButton = tk.Button(self, text='Get tweets', command=self.getModeratedTweets)  # voeg juist command toe
        if self.moderatedTweets:
            self.instructionLabel = tk.Label(self, 
                                             text="Select a tweet, then click \"Accept\" or \"Reject\" depending on the content.", 
                                             pady=20)
            self.acceptButton = tk.Button(self, text="Accept", command=self.clickAcceptTweet)
            self.rejectButton = tk.Button(self, text="Reject", command=self.clickRejectTweet)

            """
            for tweet in self.moderatedTweets:
                self.moderatedTweetsListbox.insert(self.moderatedTweets.index(tweet), tweet.getText())
            """

            self.instructionLabel.grid(column=0, row=0)
            self.moderatedTweetsListbox.grid(column=0, row=1)
            self.acceptButton.grid(column=0, row=2, pady=10)
            self.rejectButton.grid(column=0, row=3)
            self.getTweetButton.grid(column=0, row=4, pady=10)
        else:
            self.noTweetAvailableLabel = tk.Label(self, text="There are no tweets to moderate.", pady=40, font=("Arial", 18))
            self.noTweetAvailableLabel.grid(column=0, row=0)
            self.getTweetButton.grid(column=0, row=1, pady=10)

    def getModeratedTweets(self):
        self.moderatedTweetsListbox.delete(0, 'end') # Haalt alle items uit listbox
        tweets = TwitterIO.get_tweets_from_file('tweets/tweets.json') # Haalt tweets uit bestand tweets.json
        print('Get moderated tweets')
        if(len(tweets) > 0):
            for tweet in tweets:
                self.moderatedTweetsListbox.insert(tweets.index(tweet), tweet.getText())
                self.tweets.append(tweet)
            return True
        else:
            return False

        return tweets

    def clickAcceptTweet(self):
        if len(self.moderatedTweetsListbox.curselection()) > 0: # Voert alleen uit als er daadwerkelijk een tweet is geselecteerd
            index = self.moderatedTweetsListbox.curselection()[0] # index van geselecteerde tweet
            twitter = Twitter()
            request = twitter.tweet(self.moderatedTweetsListbox.get(index)) # Tweet de tweet op twitter
            if request.status_code != 200:
                error_message = json.loads(request.text)['errors'][0]['message']
                showinfo(title='Error', message=error_message)
            print(self.tweets[index].getId())
            TwitterIO.remove_tweet_from_file('tweets/tweets.json', self.tweets[index].getId()) # Verwijder tweet uit tweets.json
            self.moderatedTweetsListbox.delete(index) #Verwijder tweet uit listbox
            self.tweets.pop(index) # Verwijderd tweet uit de moderatedTweets lijst
            
        

    def clickRejectTweet(self):
        if len(self.moderatedTweetsListbox.curselection()) > 0: # Voert alleen uit als er daadwerkelijk een tweet is geselecteerd
            index = self.moderatedTweetsListbox.curselection()[0] # index van geselecteerde tweet
            self.moderatedTweetsListbox.delete(index) # Verwijderd tweet uit listbox
            tweet = self.tweets[index]
            TwitterIO.add_tweet_to_file('log/log.json', tweet) # Voegt tweet toe aan log bestand
            TwitterIO.remove_tweet_from_file('tweets/tweets.json', self.tweets[index].getId()) # Verwijderd tweet uit tweets.json
            self.tweets.pop(index) # Verwijderd tweet uit de moderatedTweets lijst
    

