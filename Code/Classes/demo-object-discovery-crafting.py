from Blueprint import Blueprint
from inventory import Inventory

def initInv():#initializing inventory
    player_inventory=Inventory()
    player_inventory.addMaterials("metalScraps",2)
    player_inventory.addMaterials("gears",1)
    player_inventory.addMaterials("oil",1)
    player_inventory.addMaterials("springs",2)
    player_inventory.addMaterials("mystery_fluid",1)
    player_inventory.addItem("gum_gun")
    return player_inventory

def showInv(inv):#showing what's inside the inventory 
    print("You currently have these materials:")
    for i in inv.materialDict:
        if(inv.materialDict[i]):
            print(inv.materialDict[i],i)
    print("\nand these items in your inventory:")
    for i in inv.itemDict:
        if(inv.itemDict[i]):
            print(inv.itemDict[i],i)


def foundMysteryItem(inv): #in case player finds mystery item
    print("\nYou just found a mystery item! Your items may get erased!")
    take_it = input("Would you like to take it? Type yes or no.\n")

    flag=1
    if(take_it.lower()=="yes"):
        while(not inv.enoughSpace()):
            print("\nYour inventory appears to be full! Would you like to get rid of an item or some materials from the inventory?")
            take_it = input("Type yes or no.\n")
            if(take_it.lower()=="yes"):
                print("\nChoose one of the items or materials below:")
                for i in inv.itemDict:
                    if(inv.itemDict[i]!=0):
                        print(i,end=" ")
                for i in inv.materialDict:
                    if(inv.materialDict[i]!=0):
                        print(i,end=" ")
                item=input("Type the item or material you want removed or type stop to exit.\n")
                if(item.lower()=="stop"):
                    flag=1
                    break
                else:
                    is_ok=inv.clearPosition(item.lower())
                    if(is_ok=="FAIL"):
                        flag=1
                        break
            else:
                flag=1
                break
    elif(take_it.lower()=="no"):
        flag=1
        print("That's unfortunate!")
    else:
        flag=1
        print("OOPS")

    #player has enough space in the inventory to add the mystery item
    if(flag==0):
        myster=inv.checkMystery(inv.getRandomMystery())
        if(myster!="RIP"):
            inv.mystery_items[myster]+=1
        print("Would you like to sell the new mystery item?")
        answer=input("Type yes or no.")
        if(answer=='yes'):
            print("We are preparing your offer... (hasn't been completed)")
        elif(answer=='no'):
            print('Too bad!')

def foundMaterial(inv,material): #in case player finds a material
    print("\nYou just found a material!")
    take_it = input("Would you like to take it? Type yes or no.\n")

    flag=0
    if(take_it.lower()=="yes"):
        if(inv.materialDict[material]==0):
            while(not inv.enoughSpace()):
                clearInv(inv)
    elif(take_it.lower()=="no"):
        print("That's unfortunate!")
    else:
        print("OOPS")
    #player has enough space in the inventory to add the material
    if(flag==0):
        inv.addMaterials(material,1)
    if(inv.canPlayerCraftNewItem()):
        print("\nLooks like you can craft an item!")

def clearInv(inv):
    print("\nYour inventory appears to be full! Would you like to get rid of an item or some materials from the inventory?")
    take_it2 = input("Type yes or no.\n")
    if(take_it2.lower()=="yes"):
        print("\nChoose one of the items or materials below:")
        for i in inv.itemDict:
            if(inv.itemDict[i]!=0):
                print(i,end=" ")
        for i in inv.materialDict:
            if(inv.materialDict[i]!=0):
                print(i,end=" ")
        item=input("Type the item or material you want removed or type stop to exit.\n")
        if(item.lower()=="stop"):
            flag=1
            return False
        else:
            is_ok=inv.clearPosition(item.lower())
            if(is_ok=="FAIL"):
                flag=1
                return False
    else:
        flag=1
        return False

player_inv=initInv()
# player_inv.getBlueprints()
showInv(player_inv)
#player finds a material
foundMaterial(player_inv,"cables")
showInv(player_inv)
#player finds a mystery item
foundMysteryItem(player_inv)
showInv(player_inv)

print("Would you like to craft an item?")
answer=input("Type yes or no: ")
if(answer=='yes'):
    if(not player_inv.enoughSpace()):
        while(clearInv(player_inv)):
            pass
    print("You have these blueprints:")
    player_inv.getBlueprints()
    print("\nChoose the item you want to craft")
    print("You currently have these materials:")
    for i in player_inv.materialDict:
        if(player_inv.materialDict[i]):
            print(player_inv.materialDict[i],i)
    item=input("Type item name:\n(gum_gun, stun_gun, EMP_grenade, time_travel_grenade, time_freeze_grenade, life_potion, speed_potion, stamina_potion) \n")
    done=player_inv.crafting(item)
    if(not done):
        print("OOPS. Something went wrong")
    showInv(player_inv)
else:
    print("Bye bye")
