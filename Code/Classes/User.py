from Hint import Hint 
from Offer import Offer
from inventory import Inventory

class User:
    def __init__(self,username,password,email,profilePicture):
        self.username = username
        self.password = password
        self.email = email
        self.listOfFriends = []
        self.listOfAchievements = []
        self.profilePicture = profilePicture
        self.rank = 0
        self.live = False 
        self.inventory = Inventory()
        self.numOfHints = 1

    def isLive(self): #return True if User is Live
        if self.live == True:
            return True
        else:
            return False

    def retrieveRank(self): #return User's rank
        return self.rank

    def makeBid(self,ammount,offer):
        if self.inventory.coins < ammount:
            print("ERROR")
        else:
            self.inventory.coins -= ammount
            #server.bidList.append([self,ammount,offer])


    def makeOffer(self,item,price):
        if not item in self.inventory.itemDict:
            print("ERROR")
        elif self.inventory.itemDict.get(item)==0:
            print("ERROR")
        else:
            x = self.inventory.itemDict.get(item)
            x -= 1
            return item,price

    def checkNumOfHints(self): #return True if User has at least one hint
        if(len(self.numOfHints)>=1):
            return True
        else:
            return False

    def updateHintsOfUser(self,num):
        self.numOfHints += num

    def showUser(self):
        pass

    def updateHintsAndCoinsOfUser(self,coins):
        self.inventory.coins += coins

    def createHint(self,hintName,hintDesc):
        self.numOfHints -= 1
        self.hint = Hint(hintName,hintDesc)


    def getHint(self,hint): #return the given hint:string
        return "Title:" + hint.hintTitle + "Description:" + hint.hintDescription

    def sendGift(self,item):
         if not item in self.inventory.itemDict:
            print("ERROR")
         elif self.inventory.itemDict.get(item)==0:
            print("ERROR")
         else:
            x = self.inventory.itemDict.get(item)
            x -= 1
            return item
        

    def reqFriendsList(self):
        return self.listOfFriends

    def sendFriendRequest(self,user):
        pass