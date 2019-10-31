from TwitterAPI import TwitterAPI
from model.tweet import Tweet
import json
import uuid

class Twitter():
    def __init__(self):
        self.api = TwitterAPI(self.__get_credentials()['CONSUMER_KEY'],
                              self.__get_credentials()['CONSUMER_SECRET'],
                              self.__get_credentials()['ACCESS_TOKEN'],
                              self.__get_credentials()['ACCESS_SECRET'])

    def __get_credentials(self):
        """
        Haalt api gegevens uit bestand
        :return: dict
        """
        with open('twitter_credentials.json') as infile:
            text = infile.read()  
            return json.loads(text)

    def tweet(self, text):
        """
        Plaatst tweet op twitter pagina (https://twitter.com/ngroep2)
        :param text: str
        :return: request
        """
        r = self.api.request('statuses/update', {'status': text})
        return r


    def get_tweets_from_timeline(self, count):
        """
        Haalt 'count' tweets van onze timeline
        :param count: int
        :return: request
        """
        data = self.api.request('statuses/home_timeline', {'count':count})
        return data
        




