import json
import sys
from model.tweet import Tweet

class TwitterIO():

    @staticmethod
    def read_file(file_location):
        """
        Leest bestand en returned in json formaat
        :param file_location: str
        :return: dict
        """
        try:
            with open(file_location) as file:
                return json.loads(file.read())
        except IOError:
            print('Bestand niet gevonden')
        except Exception as e:
            print('Er is iets fout gegaan bij het lezen van een bestand')
            print(e)
    
    @staticmethod
    def get_tweets_from_file(file_location):
        """
        Haalt tweets op uit bestand en geeft terug als json
        :param file_location: str
        :return: List(Tweet)
        """
        try:
            tweets = []
            data = TwitterIO.read_file(file_location)
            for tweet in data:
                tweets.append(Tweet(tweet['id'], tweet['datetime'], tweet['message']))
            return tweets
        except IOError:
            print('Bestand niet gevonden.')
        except Exception as e:
            print('Er is iets fout gegaan bij het ophalen van alle tweets uit een bestand')
            print(e)
    
    @staticmethod
    def add_tweet_to_file(file_location, tweet):
        """
        Voegt tweet to aan bestand file_location
        :param file_location: str
        :param tweet: Tweet object
        """
        try:
            tweetlist = TwitterIO.read_file(file_location)
            tweetlist.append({'id': tweet.getId(),'datetime': tweet.getDatetime(), 'message': tweet.getText()})
            with open(file_location, 'w') as file:
                json.dump(tweetlist, file, indent=4)
        except IOError:
            print('Bestand niet gevonden.')
        except Exception as e:
            print('Er is iets fout gegaan bij het toevoegen van een tweet aan een bestand')
            print(e)

    @staticmethod
    def remove_tweet_from_file(file_location, id):
        """
        Verwijdert tweet uit bestand met een bepaald ID
        :param file_location: str
        :param id: str
        """
        try:
            tweetlist = TwitterIO.read_file(file_location)
            result = [tweet for tweet in tweetlist if not (tweet['id'] == id)]
            with open(file_location, 'w') as file:
                json.dump(result, file, indent=4)
        except IOError:
            print('Bestand niet gevonden.')
        except Exception as e:
            print('Er is iets fout gegaan bij het verwijderen van een tweet uit een bestand')
            print(e)