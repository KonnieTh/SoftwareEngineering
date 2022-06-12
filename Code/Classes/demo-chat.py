from ServerConnection import ServerConnection
from User import User
from Offer import Offer
from TextChannel import TextChannel

server = ServerConnection(None,None,None)#να σβηστεί αργότερα

user1 = User('user1','123456','user1@gmail.com')
user1.listOfAchievements = ['1','2'] #must be of type Achievement, in this case its just a string for demo purposes
user1.live = True
user1.rank = 34
user2 = User('user2','123456','user2@gmail.com')
user2.listOfAchievements = ['1','2','3']  
user2.live = True
user2.rank = 344

offer1 = Offer(user1,'stun gun',1,52,1) #stun gun must be of type Item, in this case its just a string for demo purposes
offer2 = Offer(user1,'gum gun',1,64,2)
server.offerList.append(offer1)
server.offerList.append(offer2)
server.usersList.append(user1)
server.usersList.append(user2)

globalChat = TextChannel('globalChat',[user1,user2])
globalChat.messageList = ['user1:hey how its going?', 'user2: all good man, how about you?']

globalChat.retrieveMessages()

inputText  = input('type @ or / or (space) OR type create to create a team chat: ')

if inputText == '@':

    players = globalChat.showToList('us')
    #print(players[1].username)
    for i in range(len(players)):
        if players[i].live == True:
            print('@'+players[i].username)

    sendTo = input('select a user: ')
    message = input('send message: ')
    choice = input('choose message option(yell,whisper,regular): ')
    globalChat.checkViability(message, sendTo, choice)

elif inputText == '/':

    commandlist = globalChat.openCommands()
    print(commandlist)
    command = str(input('type command: '))

    if command == '/rankings':
        for i in range(len(globalChat.playerList)):
            print(globalChat.playerList[i].username + ': ' + str(globalChat.playerList[i].retrieveRank()))

    elif command.startswith('/achievements'):
        #print(command[:13])
        player = command[14:len(command)-1]
        #print(player)
        for i in range(len(globalChat.playerList)):
            if globalChat.playerList[i].username == player:
                print(globalChat.playerList[i].username + ':' + str(globalChat.playerList[i].listOfAchievements))
    
    elif command.startswith('/offers'):
        player = command[8:len(command)-1]
        print(player)
        offers = server.retrieveOffers(player)
        for i in range(len(offers)):
            print(offers[i].itemToSell+': '+offers[i].buyOutPrice)+' coins' #για λογους απλοποίηση απλα θα εμφανίζει τις προσφορες, κανονικά θα πρέπει να σε πηγαίνει στην σελίδασ του eshop




elif inputText == 'create': #quick and easy demo on how to create a new team chat(create new TextChannel)

    teamName = input('Type a name for your team chat: ')
    team = []
    while len(team) < len(server.usersList):
        temp = input('Select a team member: ')
        for i in range(len(server.usersList)):
            if temp == server.usersList[i].username:
                team.append(server.usersList[i])

        flag = input('want to add more members?(y/n)')
        if flag == 'n':
            break
    
    globalChat.submitTeam(teamName, team)

else:

    message = input('send message: ')
    choice = input('choose message option(yell,whisper,regular): ')
    globalChat.checkViability(message,'global', choice)