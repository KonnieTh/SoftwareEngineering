#from server import Server


from cgitb import text

from User import User


class TextChannel:
    def __init__(self,channelName,playerList):
        self.channelName = channelName
        self.playerList = playerList
        self.messageList = []
        self.commandList = ['/rankings','/offers <username>','/achievements <username>']


    def getPlayerList(self): #returns all players
        return self.playerList
        
    def retrieveMessages(self): #returns all messages
        for i in self.messageList:
            print(i)


    def showToList(self,searchedName): #returns all players that start with searchedName
        listOfPlayers = []
        for i in len(self.playerList):
            if self.playerList[i].startwith(searchedName):
                listOfPlayers.append(self.playerList[i])
        return listOfPlayers


    def checkViability(self,message): # bans message if message contains bannedWords and sends it if otherwise
        bannedWords = ['fuck']
        for i in len(bannedWords):
            if bannedWords[i] in message:
                self.banMessage()
                break
            else:
                self.sendMessage(self,message)

    def sendMessage(self,message,user=None,channel=None):
        print(message)


    def banMessage(self):
        print("The message was banned. You have been restricted from the chat for 24 hours.")
       # server.banUser()
        
    def openCommands(self): #returs list of commands
        return self.commandList


    def submitTeam(self,teamName,players):
        locals()[teamName]= TextChannel(teamName,players)


#--------chat demo
user1 = User('user1','123456','user1@gmail.com')
user1.listOfAchievements = ['1','2']
user1.live = True
user1.rank = 34
user2 = User('user2','123456','user2@gmail.com')
user2.listOfAchievements = ['1','2']
user2.live = True
user2.rank = 344
globalChat = TextChannel('globalChat',[user1,user2])

globalChat.messageList = ['user1:hey how its going?', 'user2: all good man, how about you?']
globalChat.retrieveMessages()

inputText  = input('type @ or / or (space): ')

if inputText == '@':
    players = globalChat.showToList('us')
    for i in len(players):
        if players[i].isLive == True:
            print('@'+players[i]+'\n')

    message = input('send message: ')
    globalChat.checkViability(message)

elif inputText == '/':
    commandlist = globalChat.openCommands()
    print(commandlist)
    command = input('type command: ')

    if command == '/rankings':
        for i in range(len(globalChat.playerList)):
            print(globalChat.playerList[i].username + ': ' + str(globalChat.playerList[i].retrieveRank()))

    elif command[:12] == '/achievements':
        print(command[:12])
        player = command[14:-1]
        print(player)
        for i in len(globalChat.playerList):
            if globalChat.playerList == player:
                print(globalChat.playerList[i] + ':' + globalChat.playerList[i].listOfAchievements)
else:

    message = input('send message: ')
    globalChat.checkViability(message)

