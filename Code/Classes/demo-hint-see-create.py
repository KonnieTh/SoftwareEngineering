from Hint import Hint
from ServerConnection import *
 
 
#create a user and a server instance
user1 = User("user1","jejw","usr@gmail.com")
user1.numOfHints = 2
server = ServerConnection(None,None, None)
hint1 = Hint("someHint",None,"someDescription",user1.username)

input1 = input('Do you want to see a hint? Type yes or no. \n')

if input1=="yes":
    if (user1.checkNumOfHints()==True):
        hint_input = input('Please type the title of the hint you want to see: \n')

        for i in server.hintsList:
            if hint_input in server.hintsList:
                user1.getHint(server.hintList[i])
                
                review_input = input("Please rate this hint. Type yes for a positive review or no for a negative review: \n")
                
                if review_input == "yes":
                    server.hintList[i].likes += 1
                    server.updateHintReviews()
                    server.percentOfPosReviews()

                elif review_input == "no":
                    server.hintList[i].likes -= 1
                    server.updateHintReviews()
                    server.percentOfPosReviews()


            else:
                print("The hint you typed is not available. \n")

    else: 
        print("You cannot see a hint. \n")

elif input1 =="no":
    input2 = input("Do you want to create a hint? Type yes or no. \n")
    if input2 == "yes":
            hint_title, hint_description = input("Please type the title and the description of the new hint: ").split()
            server.hintDict.update({hint_title,hint_description})
            user1.createHint(hint_title,hint_description,user1.username)
            print(hint_title)
    else:
        print("ERROR")

else:
    print("ERROR")


