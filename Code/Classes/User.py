from Hint import Hint 
from inventory import Inventory
from ServerConnection import ServerConnection

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
            server = ServerConnection()
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

    
    def updateHintsAndCoinsOfUser(self,penalty):
        server = ServerConnection()
        if server.percentOfPosReviews()==True:
            self.numOfHints += 1
        else:
            if penalty == "coins":
                self.inventory.coins += 10
            elif penalty == "hint":
                self.numOfHints =- 1
            else: 
                print("ERROR")

    def createHint(self,hintName,hintDesc,username):
        self.numOfHints -= 1
        self.hint = Hint(hintName,None,hintDesc,username)


    def getHint(self,hint): #return the given hint:string
        return "Title:" + hint.hintTitle + "Description:" + hint.hintDescription


    def sendGift(self,item):
         if item not in self.inventory.itemDict:
            print("ERROR")
         elif self.inventory.itemDict.get(item)==0:
            print("ERROR")
         else:
            x = self.inventory.itemDict.get(item)
            x -= 1
            return item
    def reciprocateGift(self):
        pass

    def reqFriendsList(self):
        return self.FriendsList

    def sendFriendRequest(self):
        pass

    def updateFriendsList(self,user):
        if user not in self.FriendsList:
            self.FriendsList.append(user)
        else:
            print("User already exists in friends list")

    def returnSample(self,friends = None, all = None):
        pass

    #def setStatRequested(characteristics: list,timeLim = None):
    #    formQuery(characteristics, timeLim)