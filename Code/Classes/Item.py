import math

class Item:
    def __init__(self, value, itemName, description, x_pos, y_pos, pic):
        self.value = value
        self.itemName = itemName
        self.description = description
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.inInv = False
        self.pic = pic

    def collided(self, alienX):
        distance = math.sqrt((math.pow(abs(self.x_pos - alienX),2)))
        if distance < 70:
            return True
        else:
            return False

class MysteryItem(Item):
    #nothing for now
    pass