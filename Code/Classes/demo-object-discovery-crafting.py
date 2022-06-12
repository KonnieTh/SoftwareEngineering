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
        print(inv.materialDict[i],i)
    print("\nand these items in your inventory:")
    for i in inv.itemDict:
        print(inv.itemDict[i],i)


def foundMysteryItem(inv): #in case player finds mystery item
    print("\nYou just found a mystery item! Your items may get erased!")
    take_it = input("Would you like to take it? Type yes or no.\n")

    flag=0
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
        print("That's unfortunate!")
    else:
        print("OOPS")

    #player has enough space in the inventory to add the mystery item
    if(flag==0):
        myster=inv.checkMystery(inv.getRandomMystery())
        if(myster!="RIP"):
            inv.mystery_items[myster]+=1

def foundMaterial(inv,material): #in case player finds a material
    print("\nYou just found a material!")
    take_it = input("Would you like to take it? Type yes or no.\n")

    flag=0
    if(take_it.lower()=="yes"):
        if(inv.materialDict[material]==0):
            while(not inv.enoughSpace()):
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
        print("That's unfortunate!")
    else:
        print("OOPS")
    #player has enough space in the inventory to add the material
    if(flag==0):
        inv.addMaterials(material,1)
    if(inv.canPlayerCraftNewItem()):
        print("\nLooks like you can craft an item!")

def crafting(inv,item): #crafts an item
    if(inv.enoughSpaceForCrafting(item) and not inv.checkIfMaterialsAreMissing(item)):
        inv.removeMaterials(item)
        inv.addItem(item)
        print("\nCrafting Done!")


player_inv=initInv()
showInv(player_inv)
foundMaterial(player_inv,"cables")
print(player_inv.itemDict)
print(player_inv.materialDict)
print(player_inv.mystery_items)
print("Would you like to craft an item?")
