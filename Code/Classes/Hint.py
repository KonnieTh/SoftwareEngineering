class Hint:
    def __init__(self,hintTitle,tags,hintDescription,creator):
        self.hintTitle = hintTitle
        self.tags = tags
        self.hintDescription = hintDescription
        self.likes = 0
        self.dislikes = 0
        self.creator = creator # creator must be of type User


    def getHint(self):
        return self.hintTitle, self.tags, self.hintDescription


