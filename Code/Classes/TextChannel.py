#from server import Server

from pickle import NONE


class TextChannel:
    def __init__(self,channelName,playerList):
        self.channelName = channelName
        self.playerList = playerList
        self.messageList = []
        self.commandList = []


    def getPlayerList(self): #returns all players
        return self.playerList
        
    def retrieveMessages(self): #returns all messages
        return self.messageList


    def showToList(self,searchedName): #returns all players that start with searchedName
        listOfPlayers = []
        for i in self.playerList:
            if self.playerList[i].startwith(searchedName):
                listOfPlayers.append(self.playerList[i])
        return listOfPlayers


    def checkViability(self,message,textChannel): # bans message if message contains bannedWords and sends it if otherwise
        bannedWords = []
        for i in bannedWords:
            if bannedWords[i] in message:
                self.banMessage()
                break
            else:
                self.sendMessage(self,message,textChannel)

    def sendMessage(self,message,user=None,channel=None):
        print(message)


    def banMessage(self):
        print("The message was banned. You have been restricted from the chat for 24 hours.")
       # server.banUser()
        
    def openCommands(self): #returs list of commands
        return self.commandList


    def submitTeam(self,teamName,players):
        locals()[teamName]= TextChannel(teamName,players)


