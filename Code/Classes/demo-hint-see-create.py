#from Hint import *
from ServerConnection import *
from User import *
 
 
#create a user and a server instance
user3 = User("user3","jejw","usr@gmail.com")
user3.numOfHints = 2
hint1 = Hint("someHint",['boss','exploit'],"someDescription",user3.username)
server.storeHint(hint1)

input1 = input('To read a hint type r, to write one type w. \n')

if input1=="r":
    if (user3.checkNumOfHints()==True):
        tag = input('Type a tag for your hint:  \n')

        correct_hint = server.findHint(tag,user3)
        print(correct_hint.hintTitle + ':' + correct_hint.hintDescription)       
        review_input = input("Please rate this hint. Type yes for a positive review or no for a negative review: \n")
                
        server.reviewHint(review_input,correct_hint)
        server.checkpercentOfPosReviews(correct_hint)

    else: 
        print("You cannot see a hint. \n")


elif input1 =="w":

            #writeHint()
            new_title = input('Type the title of new hint: ')
            new_desc = input('Type a description for the new hint: ')
            new_tag = input("Type a tag for the new hint: ")

            checker = server.checkText(new_desc)
            if checker == 'error':
                print('Error posting hint! ')
            elif checker == 'ok':
                server.createHint(new_title,new_tag,new_desc,user3)





