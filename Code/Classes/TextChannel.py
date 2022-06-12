from cgitb import text
from pydoc import doc
from User import User
from Offer import Offer


class TextChannel:
    def __init__(self,channelName,playerList):
        self.channelName = channelName
        self.playerList = playerList
        self.messageList = []
        self.commandList = ['/rankings','/offers<username>','/achievements<username>']


    def getPlayerList(self): #returns all players
        return self.playerList
        
    def retrieveMessages(self): #returns all messages
        for i in self.messageList:
            print(i)


    def showToList(self,searchedName): #returns all players that start with searchedName
        listOfPlayers = []
        for i in range(len(self.playerList)):
            if self.playerList[i].username.startswith(searchedName):
                listOfPlayers.append(self.playerList[i])
        return listOfPlayers


    def checkViability(self,message, receiver,choice): # bans message if message contains bannedWords and sends it if otherwise
        bannedWords = ['fuck']
        for i in range(len(bannedWords)):
            if bannedWords[i] in message: 
                self.banMessage()
                break
            else:
                self.sendMessage(message,receiver,choice)

    def sendMessage(self,message,receiver,choice):
        option = self.messageOptions(choice)
        if option == 'regular':
            print(receiver+' <- '+message)
        else:
             print(receiver+' <- '+option+message)   


    def banMessage(self):
        print("The message was banned. You have been restricted from the chat for 24 hours.")
       # server.banUser()
        
    def openCommands(self): #returs list of commands
        return self.commandList


    def submitTeam(self,teamName,players):
        locals()[teamName]= TextChannel(teamName,players)
        print('Successfully created new team chat!')

    def messageOptions(self,choice): #για λογους απλοποίησης απλα θα εμφανίζουμε δίπλα στο μήνυμα το option αντι να τροποποιούμε την γραμμτοσείρα
        if choice == "yell":
            #make string in bold, and different color
            return 'YELLS! '
        elif choice == 'whisper':
            #make string's oppacity low and diffrent color
            return 'whispers...'
        else:
            return 'regular'


