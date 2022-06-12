from User import User
from ServerConnection import *

user4 = User("john12","pswrd","john@gmail.com")
user5 = User("jane23","kff","jane@gmail.com")
user6 = User("mary340","233","mary@gmail.com")
user4.inventory.addItem('EMP_grenade')
user4.inventory.addItem('life_potion')

server.usersList.append(user4)
server.usersList.append(user5)
server.usersList.append(user6)

FriendName = input("Enter a player's username: \n")

relativeNames = server.checkUser(FriendName)
for i in range(len(relativeNames)):   
    print(relativeNames[i].username)

receiver = input('Select a player to add to your friends: ')
server.sendFriendRequest(user4,user5) #για λόγους ευκολίας μεσο αυτής της μεθόδου στέλνουμε και δεχόμαστε το friedn request

print('Send a gift to your new friend.')
print(user4.inventory.itemDict) #showItems, createList()
choice = input('Choose an item to give: ') #chooseGift
user4.sendGift(choice,receiver) #για να δουλευει χρειάζεται η changeItem()

#για λογους ευκολίας απλα θα δεχόμαστε gift αυθαίρετα το ίδιο item που στείλαμε
choice2 = input('You got a gift, do you accept it(yes/no)?')
if choice2 == 'yes':
    user4.acceptGift(choice)
elif choice2 == 'no':
    user4.rejectGift(choice,receiver)





