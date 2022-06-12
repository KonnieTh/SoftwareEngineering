
#from User import *
from Hint import Hint
from inventory import Inventory
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
            offer.priceOfPurchase = price
            self.offerList.remove(offer)
            currentTime = datetime.datetime.now()
            self.pastPurchases.append([offer, buyerUser, sellerUser, price, currentTime])
            self.updateInventory(offer, buyerUser, sellerUser)
        else:
            print("Error")

    def publishOffer(self, offer):
        self.offerList.append(offer)

    def updateInventory(self, offer, buyerUser, sellerUser):
        sellerUser.inventory.itemDict[offer.itemToSell] -= offer.quantity
        sellerUser.inventory.coins += offer.priceOfPurchase
        buyerUser.inventory.itemDict[offer.itemToSell] += offer.quantity
        buyerUser.inventory.coins -= offer.priceOfPurchase

    def addRandItem(self, user):
        x = random.randint(0, len(list(self.itemsList)))
        quantity = random.randint(1, 5)
        x = self.itemslist[x]
        if x in user.inventory:
            user.inventory[list(self.itemsList)[x]] += quantity
        else:
            user.inventory[x] = quantity

    def banUser(self, user, date):
        pass

    def setAndDisplayMiniGame(self, user):
        x = random.randint(1, 4)
        if x == 1:
            self.addRandItem(user)
            print('Congratz you won!!')
        else:
            print('Oops you lost :(')    

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
            senderUser.updateFriendsList(receiverUser)
            receiverUser.updateFriendsList(senderUser)
        elif(x == 2):
            print('Showing previous screen')
        else:
            senderUser.notifications.append(f"User: {receiverUser.username} has declined your request")
            print('Friend request declined')

    def checkpercentOfPosReviews(self, hint):
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

        print('Thanks for rating this hint!')


    def checkUser(self, username):
        temp = []
        for i in range(len(self.usersList)):
            if self.usersList[i].username.startswith(username):
                temp.append(self.usersList[i])

        return temp        


    def storeHint(self, hint):
        self.hintsList.append(hint)


    def retrieveOffers(self,seller):
        playerOffers = []
        for i in range(len(self.offerList)):
            if self.offerList[i].seller == seller:
                playerOffers.append(self.offerList[i])

        return playerOffers  

    def findHint(self,tag,user):
        for i in range(len(self.hintsList)):
            if tag in self.hintsList[i].tags:
                #print(self.hintsList[i].tags)
                return self.hintsList[i]

    def createHint(self,title,tags,desc,user):
        locals()[title] = Hint(title,tags,desc,user)
        self.storeHint(title)
        user.numOfHints -= 1
        print('Successfully created new hint!')


    def checkText(self,text):
        bannedWords = ['fuck']
        for i in range(len(bannedWords)):
            if bannedWords[i] in text: 
                print('Found forbbiden works in text: '+ bannedWords[i])
                return 'error'
            else:
                print('Text is ok, proceeding to uploading.')
                return 'ok'

    def reviewHint(self,input,hint):
        if input == 'yes':
            self.updateHintReviews(hint, 1)

        elif input == "no":
            self.updateHintReviews(hint, 0)

    def makeListOfTodaysOffers(self):
        temp = []
        for i in range(len(self.offerList)):
            if self.offerList[i].seller.username == 'shop':
                temp.append(self.offerList[i])
        return temp        


server = ServerConnection(None,None,None)







        
