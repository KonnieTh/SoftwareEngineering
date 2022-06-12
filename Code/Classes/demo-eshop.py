from ServerConnection import *
from User import User
from Offer import Offer

#Αυτο το demο είναι μόνο η βασική ροή του eshop use-case
user7 = User("marios","pswrd","marios@gmail.com")
user8 = User("manos","kff","manos@gmail.com")
shop = User('shop','shop','shop')
shop.inventory.coins= 9999
shop.inventory.itemDict['gum_gun']= 99
shop.inventory.itemDict['stun_gun']= 99
shop.inventory.itemDict['EMP_grenade']= 99
shopOffer1 = Offer(shop,'gum_gun',5,20,0)
shopOffer2 = Offer(shop,'stun_gun',1,32,0)
shopOffer3 = Offer(shop,'EMP_grenade',7,24,0)
server.offerList.append(shopOffer1)
server.offerList.append(shopOffer2)
server.offerList.append(shopOffer3)

choice = input('1.Buy from shop. \n2.Buy from player.\nChoose: ')

todayOffers = server.makeListOfTodaysOffers()
for i in range(len(todayOffers)): #display()
    print(todayOffers[i].itemToSell + ': ' + str(todayOffers[i].buyOutPrice)+ ' coins')

choice2 = input('Type the item you want to buy: ')

for i in range(len(todayOffers)):
    if todayOffers[i].itemToSell == choice2:
        tempItem = todayOffers[i]
        if (user7.inventory.doesPlayerHaveEnoughCoins(todayOffers[i].buyOutPrice) and user7.inventory.enoughSpace()):
            server.publishPurchase(todayOffers[i],user7,shop,todayOffers[i].buyOutPrice)
            print("Transaction complete!")
            break
        else:
            print('ERROR not enough coins or space!')

choice3 = input('1.Want a 5 percent return \n2.A lott for the Minigame?\n(1/2): ')
if choice3 == '1':
    server.returnFunds(tempItem.BuyOutPrice,user7)
elif choice == '2':
    server.setAndDisplayMiniGame(user7)