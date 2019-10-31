import tkinter as tk
from tkinter.messagebox import showinfo
import sys
import uuid
import time
sys.path.append('../')
from twitterio import TwitterIO
from model.tweet import Tweet

class ConsumentenWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, text='Wat wil je tweeten?', height=2, width=30)
        self.tekst = tk.Text(self, width=100, height=4)
        self.button = tk.Button(self,  text='Tweet', command=self.clicked)

        self.label.pack()
        self.tekst.pack(padx=10, pady=10)
        self.button.pack(pady=10)

    def clicked(self):
        tweet = self.tekst.get("1.0", tk.END).rstrip()
        if len(tweet) > 140:
            text = "Tweet is te lang"
            self.label['text'] = text
        elif len(tweet) == 0:
            text = 'Tweet is leeg'
            self.label['text'] = text
        else:
            text = "Wat wil je tweeten?"
            self.label['text'] = text
            self.tekst.delete('1.0', tk.END)
            showinfo(title='Verzonden', message='Tweet is verzonden')
            TwitterIO.add_tweet_to_file('tweets/tweets.json', Tweet(str(uuid.uuid4()), time.strftime('%m/%d/%Y,%H:%M:%S'), tweet))
