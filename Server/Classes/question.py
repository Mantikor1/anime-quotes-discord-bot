import os
import json
import os
import random

dir = os.path.dirname(__file__)
path = os.path.join(dir, "quotes.json")
file = open(path)
quotes = json.load(file)

class Question():
    def __init__(self):
        questions = self.drawQuote()
        self.quote = questions["quote"]
        self.title = questions["title"]
        self.character = questions["character"]
        self.titleFound = False
        self.characterFound = False

    # Draw a random quote from the file
    def drawQuote(self):
        return random.choice(quotes)