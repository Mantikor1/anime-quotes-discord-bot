import os
import json
import os

dir = os.path.dirname(__file__)
file = open(dir + "\\quotes.json")
quotes = json.load(file)

class Question():
    def __init__(self):
        questions = self.drawQuote()
        self.quote = questions["quote"]
        self.title = questions["title"]
        self.character = questions["character"]
        self.titleFound = False
        self.characterFound = False

    def drawQuote(self):
        return quotes[1]