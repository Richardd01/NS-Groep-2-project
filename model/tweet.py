class Tweet():
    def __init__(self, id, datetime, text):
        self.id = id
        self.datetime = datetime
        self.text = text


    def getId(self):
        return self.id


    def getDatetime(self):
        return self.datetime

    
    def getText(self):
        return self.text
    