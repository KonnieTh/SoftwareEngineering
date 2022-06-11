class Hint:
    def __init__(self,hintTitle,tags,hintDescription):
        self.hintTitle = hintTitle
        self.tags = tags
        self.hintDescription = hintDescription
        self.likes = 0
        self.dislikes = 0


    def getHint(self):
        return self.hintTitle, self.tags, self.hintDescription
