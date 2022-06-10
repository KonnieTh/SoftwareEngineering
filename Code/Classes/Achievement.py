
class Achievement:
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.progression = []
        self.rating = 0
  
    def showAch(self): 
        return self.title, self.description, self.progression, self.rating

