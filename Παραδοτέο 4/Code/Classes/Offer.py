
class Offer:
    def __init__(self,seller,buyer,itemToSell,buyOutPrice,bidPrice,timeOfCreation):
        self.seller = seller #seller must be of type User
        self.buyer = buyer #buyer must be of type User
        self.itemToSell = itemToSell #itemToSell must be of type Item
        self.buyOutPrice = buyOutPrice
        self.bidPrice = bidPrice
        self.timeOfCreation = timeOfCreation
