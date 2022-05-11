class User:
    def __init__(self,username,password,email,listOfFriends,listOfAchievements,profilePicture,rank):
        self.username = username
        self.password = password
        self.email = email
        self.listOfFriends = listOfFriends
        self.listOfAchievements = listOfAchievements
        self.profilePicture = profilePicture
        self.rank = rank


class ServerRoom:
    def __init__(self,numOfPlayers,creator,level,roomID,roomPassword,isPrivate,isAvailable):
        self.numOfPlayers = numOfPlayers
        self.creator = creator  #creator must be of type User
        self.level = level
        self.roomID = roomID
        self.roomPassword = roomPassword
        self.isPrivate = isPrivate
        self.isAvailable = isAvailable


class Achievement:
    def __init__(self,title,description,progression,rating):
        self.title = title
        self.description = description
        self.progression = progression
        self.rating = rating


class textChannel:
    def __init__(self,channelName,playerList):
        self.channelName = channelName
        self.playerList = playerList


class Offer:
    def __init__(self,seller,buyer,itemToSell,buyOutPrice,bidPrice,timeOfCreation):
        self.seller = seller #seller must be of type User
        self.buyer = buyer #buyer must be of type User
        self.itemToSell = itemToSell #itemToSell must be of type Item
        self.buyOutPrice = buyOutPrice
        self.bidPrice = bidPrice
        self.timeOfCreation = timeOfCreation


class Hint:
    def __init__(self,hintTitle,tags,hintDescription,likes,dislikes):
        self.hintTitle = hintTitle
        self.tags = tags
        self.hintDescription = hintDescription
        self.likes = likes
        self.dislikes = dislikes


