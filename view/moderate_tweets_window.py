import tkinter as tk
from tkinter.messagebox import showinfo
import sys
import json
sys.path.append('../')
from twitterio import TwitterIO
from controller.twitter import Twitter

class ModerateTweetsWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.tweets = []
        self.moderatedTweetsListbox = tk.Listbox(self, selectmode="single", width=150, height=20)
        self.getModeratedTweets()
   
        self.instructionLabel = tk.Label(self, 
                                        text="Select a tweet, then click \"Accept\" or \"Reject\" depending on the content.", 
                                        pady=20)
        self.acceptButton = tk.Button(self, text="Accept", command=self.clickAcceptTweet)
        self.rejectButton = tk.Button(self, text="Reject", command=self.clickRejectTweet)
        self.getTweetButton = tk.Button(self, text='Get tweets', command=self.getModeratedTweets)

        self.instructionLabel.grid(column=0, row=0)
        self.moderatedTweetsListbox.grid(column=0, row=1)
        self.acceptButton.grid(column=0, row=2, pady=10)
        self.rejectButton.grid(column=0, row=3)
        self.getTweetButton.grid(column=0, row=4, pady=10)


    def getModeratedTweets(self):
        """
        Haalt tweets uit bestand en zet deze in de listbox. Ook worden de tweets in de list tweets gezet.
        """
        self.moderatedTweetsListbox.delete(0, 'end') # Haalt alle items uit listbox
        tweets = TwitterIO.get_tweets_from_file('tweets/tweets.json') # Haalt tweets uit bestand tweets.json
        if(len(tweets) > 0):
            self.tweets = []
            for tweet in tweets:
                self.moderatedTweetsListbox.insert(tweets.index(tweet), tweet.getText())
                self.tweets.append(tweet)


    def clickAcceptTweet(self):
        """
        Haalt geselecteerde tweet uit bestand en plaatst het bericht op twitter. 
        Tweet word uit tweets list gehaald en word ook verwijderd uit de listbox
        """
        if len(self.moderatedTweetsListbox.curselection()) > 0: # Voert alleen uit als er daadwerkelijk een tweet is geselecteerd
            index = self.moderatedTweetsListbox.curselection()[0] # index van geselecteerde tweet
            #twitter = Twitter()
            request = Twitter().tweet(self.tweets[index].getText()) # Tweet de tweet op twitter
            if request.status_code != 200:
                error_message = json.loads(request.text)['errors'][0]['message']
                showinfo(title='Error', message=error_message)
            TwitterIO.remove_tweet_from_file('tweets/tweets.json', self.tweets[index].getId()) # Verwijder tweet uit tweets.json
            self.moderatedTweetsListbox.delete(index) #Verwijder tweet uit listbox
            self.tweets.pop(index) # Verwijderd tweet uit de moderatedTweets lijst
            showinfo('Tweeted', 'Tweet has been sent')
        else:
            showinfo('Error', 'Please select a message')
            
        

    def clickRejectTweet(self):
        """
        Haalt geselecteerde tweet uit tweets.json bestand en voegt deze toe aan log.json
        Tweet word uit tweets list gehaald en word ook verwijderd uit listbox
        """
        if len(self.moderatedTweetsListbox.curselection()) > 0: # Voert alleen uit als er daadwerkelijk een tweet is geselecteerd
            index = self.moderatedTweetsListbox.curselection()[0] # index van geselecteerde tweet
            self.moderatedTweetsListbox.delete(index) # Verwijderd tweet uit listbox
            tweet = self.tweets[index]
            TwitterIO.add_tweet_to_file('log/log.json', tweet) # Voegt tweet toe aan log bestand
            TwitterIO.remove_tweet_from_file('tweets/tweets.json', self.tweets[index].getId()) # Verwijderd tweet uit tweets.json
            self.tweets.pop(index) # Verwijderd tweet uit de moderatedTweets lijst
            showinfo('Rejected', 'Tweet is rejected')
        else:
            showinfo('Error', 'Please select a message')