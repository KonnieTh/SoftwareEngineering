
class ServerRoom:
    def __init__(self,numOfPlayers,creator,level,roomID,roomPassword,isPrivate,isAvailable):
        self.numOfPlayers = numOfPlayers
        self.creator = creator  #creator must be of type User
        self.level = level
        self.roomID = roomID
        self.roomPassword = roomPassword
        self.isPrivate = isPrivate
        self.isAvailable = isAvailable
