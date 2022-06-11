from collections import UserList
from User import User
from ServerConnection import ServerConnection

user1 = User("john12","pswrd","john@gmail.com")
user2 = User("jane23","kff","jane@gmail.com")
user3 = User("mary340","233","mary@gmail.com")

server = ServerConnection(None,None, None)
server.usersList.append(user1.username)
server.usersList.append(user2.username)
server.usersList.append(user3.username)

input1 = input("Please enter a player's username: \n")

for i in range(len(server.usersList)):
    if (server.usersList[i] == input1):
        print(server.usersList)
    elif(server.usersList[i].find(input1) != -1 ):
        print(server.usersList)

input_friend = input("Enter the username of the player you want to add as friend: \n")

server.sendFriendRequest(user1.username,input_friend)

