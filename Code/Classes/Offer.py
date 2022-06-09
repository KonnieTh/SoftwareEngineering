from datetime import datetime
import datetime

class Offer:
    def __init__(self,seller,itemToSell,quantity,buyOutPrice,startingBid):
        self.seller = seller #seller must be of type User
        self.itemToSell = itemToSell #itemToSell must be of type Item
        self.buyOutPrice = buyOutPrice
        self.startingBid = startingBid
        self.timeOfCreation = datetime.datetime.now()
        self.quantity = quantity