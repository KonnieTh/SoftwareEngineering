from inventory import Inventory
from ServerConnection import *

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        self.FriendsList = []
        self.listOfAchievements = []
        self.rank = 0
        self.live = False 
        self.inventory = Inventory()
        self.numOfHints = 1
        self.notifications = []

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
            server.bidList.append([self,ammount,offer])


    def makeOffer(self,item,price):
        if item not in self.inventory.itemDict:
            print("ERROR")
        elif self.inventory.itemDict.get(item)==0:
            print("ERROR")
        else:
            x = self.inventory.itemDict.get(item)
            x -= 1
            return item,price

    def checkNumOfHints(self): #return True if User has at least one hint
        if(self.numOfHints>=1):
            return True
        else:
            return False

    def updateHintsOfUser(self,num):
        self.numOfHints += num


    def sendGift(self,item, receiver):
       self.inventory.removeItem(item)
       changedItem = receiver.inventory.changeItem(item) #inventory
       receiver.inventory.addItem(changedItem)
       print("gift sent!")

    def reciprocateGift(self):
        pass

    def reqFriendsList(self):
        return self.FriendsList

    def sendFriendRequest(self):
        pass

    def updateFriendsList(self,user):
        if user not in self.FriendsList:
            self.FriendsList.append(user)
            print('Friend request accepted!')
        else:
            print("User already exists in friends list.")

    def returnSample(self,friends = None, all = None):
        pass

    def findActiveFriends(self):
        pass

    def sendInvite(self):
        pass

    def acceptGift(self,item):
        self.inventory.addItem(item)

    def rejectGift(self,item,sender):
        sender.inventory.addItem(item)
    #def setStatRequested(characteristics: list,timeLim = None):
    #    formQuery(characteristics, timeLim)