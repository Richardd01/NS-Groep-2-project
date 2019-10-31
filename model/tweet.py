class Tweet():
    def __init__(self, id, datetime, text):
        self.id = id
        self.datetime = datetime
        self.text = text


    def getId(self):
        """
        Geeft uuid van tweet terug
        :return: str
        """
        return self.id


    def getDatetime(self):
        """
        Geeft datum en tijd terug
        :return: str
        """
        return self.datetime

    
    def getText(self):
        """
        Geeft bericht terug
        :return: str
        """
        return self.text
    