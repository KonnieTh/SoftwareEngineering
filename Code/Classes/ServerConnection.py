from User import *
import datetime
import random

class ServerConnection:
    def __init__(self, itemsList, achievementList, availLevels) -> None:
        self.itemsList = itemsList
        self.offerList = []
        self.achievementList = achievementList
        self.pastPurchases = []
        self.bidList = []
        self.usersList = []
        self.roomsList = []
        self.availLevels = availLevels
        self.hintsList = []

    def checkRoom(self, roomID):
        for i in self.roomList:
            if i.roomID == roomID:
                return True
        return False


    def userSingedUp(self, user):
        currentTime = datetime.datetime.now()
        self.usersList.append([user, currentTime])

    def publishPurchase(self, offer, buyerUser, sellerUser, price):
        if offer in self.offerList:
            self.offerList.remove(offer)
            currentTime = datetime.datetime.now()
            self.pastPurchases.append([offer, buyerUser, sellerUser, price, currentTime])
            self.updateInventory(self, offer, buyerUser, sellerUser, price)
        else:
            print("Error")

    def publishOffer(self, offer):
        self.offerList.append(offer)

    def updateInventory(self, offer, buyerUser, sellerUser):
        sellerUser.inventory.itemDict[offer] -= offer.quantity
        sellerUser.inventory.coins += offer.priceOfPurchase
        buyerUser.inventory.itemDict[offer] += offer.quantity
        buyerUser.inventory.coins -= offer.priceOfPurchase

    def addRandItem(self, user):
        x = random.randint(0, len(list(self.itemsList)))
        quantity = random.randint(1, 5)
        x = self.itemslist[x]
        if x in user.inventory:
            user.inventory[list(self.itemsList)[x]] += quantity
        else:
            user.inventory[x] = quantity

    def setMiniGame(self, user):
        x = random.randint(1, 100)
        if x <= 20:
            self.addRandItem(user)

    def banUser(self, user, date):
        pass

    def setAndDisplayMiniGame(self, user):
        x = random.randint(1, 20)
        y = int(input('Chooose a num between 1 and 20: '))
        if x == y:
            self.addRandItem(user)

    def removeOfferFromList(self, offer):
        self.offerList.remove(offer)

    def returnFunds(self, price, user):
        user.inventory.coins += int(0.05 * price)
        

    def sendFriendRequest(self, senderUser, receiverUser):
        x = int(input(f"{senderUser.username} has sent you a friend request: (type: 0 to decline, 1 to accept, 2 to answer later)"))
        if(x>2 or x<0):
            print('Valid answers are: 0, 1 or 2')
            print('Please try again')
            self.sendFriendRequest(self, senderUser, receiverUser)

        elif(x == 1):
            senderUser.listOfFriends.append(receiverUser)
            receiverUser.listOfFriends.append(senderUser)
        elif(x == 2):
            print('Showing previous screen')
        else:
            senderUser.notifications.append(f"User: {receiverUser.username} has declined your request")

    def percentOfPosReviews(self, hint):
        if hint.likes+hint.dislikes >= 10:
            h = hint.likes / (hint.likes + hint.dislikes)
            if h >= 0.7:
                hint.author.numOfHints += 1

            elif hint.author.numOfHints > 1:
                hint.author.numOfHints -= 1

            elif hint.author.inventory.coins >= 10:
                hint.author.inventory.coins -= 10
            
            elif hint.author.inventory.coins < 10:
                hint.author.inventory.coins = 0


    def updateHintReviews(self, hint, liked):
        if liked:
            hint.likes += 1
        else:
            hint.dislikes += 1


    def checkUser(self, user):
        if user in self.usersList:
            return True
        else:
            return False

    def storeHint(self, hint):
        self.hintsList.append(hint)


    def retrieveOffers(self,seller):
        playerOffers = []
        for i in range(len(self.offerList)):
            if self.offerList[i].seller == seller:
                playerOffers.append(self.offerList[i])

        return playerOffers  