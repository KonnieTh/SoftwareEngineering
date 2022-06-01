
class Achievement:
    def __init__(self,title,description,progression,rating):
        self.title = title
        self.description = description
        self.progression = progression
        self.rating = rating

    def showAch(self): 
        return self.title, self.description, self.progression, self.rating

