from ServerConnection import *

class Hint:
    def __init__(self,hintTitle,tags,hintDescription,author):
        self.hintTitle = hintTitle
        self.tags = tags
        self.hintDescription = hintDescription
        self.likes = 0
        self.dislikes = 0
        self.author = author #user


    def getHint(self):
        return self


   