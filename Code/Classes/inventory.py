from Blueprint import Blueprint
import random as rd

class Inventory:
    def __init__(self):
        self.coins = 20
        self.size = 6
        self.pos={'1':'','2':'','3':'','4':''} #positions to place blueprints
        self.materialDict = {'cables':0,'gears':0,'metalScraps':0,'oil':0,'springs':0,'mystery_fluid':0}
        self.itemDict = {'gum_gun':0,'stun_gun':0,'EMP_grenade':0,'time_travel_grenade':0,'time_freeze_grenade':0,'life_potion':0,'speed_potion':0,'stamina_potion':0}
        self.mystery_items={'mystery1':0,'mystery2':0,'mystery3':0,'mystery4':0,'mystery5':0,'mystery6':0,'mystery7':0,'mystery8':0,'mystery9':0,'mystery10':0,'mystery11':0,'mystery12':0}
        self.reviveToken=0


    def addBlueprint(self,item,position): #adds blueprint to a position and deactivates it
        blueprint=Blueprint(item)
        if(blueprint.isActive==True):
            self.pos[position]=item
            blueprint.deactivateBlueprint()
        else:
            print('Blueprint is inactive')

    def isItemsBlueprintActive(self,item): #returns True if blueprint is active
        blueprint=Blueprint(item)
        if(blueprint.isActive==True):
            return True
        else:
            return False

    def getBlueprints(self): #show blueprints
        for i in self.itemDict:
            blueprint=Blueprint(i)
            recipe=blueprint.getBlueprint()
            print("Recipe for ", i, " is: ", end=" ")
            for j in range(len(recipe)):
                print(recipe[j],end=" ")
            print()

    def registeredBlueprints(self): #shows blueprints in pos
        for i in self.pos:
            blueprint=Blueprint(i)
            recipe=blueprint.getBlueprint()
            print("Recipe for ", i, " is: ", end=" ")
            for j in range(len(recipe)):
                print(recipe[j],end=" ")
            print()

    def addInactiveBlueprint(self,blueprint): #activates inactive blueprint
        if(self.doesPlayerHaveEnoughCoins(10)):
            self.coins-=10
            blueprint.activateBlueprint()

    def addRandItem(self): #adds a random quantity
        entry_list = list(self.itemDict.items())
        random_entry = rd.choice(entry_list)
        item=random_entry[0]
        quantity = rd.randint(1, 5)
        for i in range(quantity):
            self.addItem(item)
    
    def changeItem(self,item): #possibly changes the item to a mystery
        num=rd.randint(0,10)
        if(num<3):
            return self.getRandomMystery()
        return item
    
    def crafting(self,item): #crafts an item
        if(self.enoughSpaceForCrafting(item) and self.checkIfMaterialsAreMissing(item)):
            self.removeMaterials(item)
            self.addItem(item)
            print("\nCrafting Done!")
            return True
        else:
            print("Not enough space or missing materials")
            return False

    def removeReviveToken(self): #removes one revive token
        if(self.reviveToken>0):
            self.reviveToken-=1
        else:
            print("Error")
    
    def getRandomMystery(self): #returns random mystery item
        entry_list = list(self.mystery_items.items())
        random_entry = rd.choice(entry_list)
        return random_entry[0]

    def destroyItems(self):
        for i in self.itemDict:
            self.clearPosition(i)
    
    def checkMystery(self,mystery): #checks if mystery item will be returned or it will clear all the items
        shot=rd.randint(0,99)
        if(shot<20):
            self.destroyItems()
            return 'RIP'
        else:
            return mystery

    def doesPlayerHaveEnoughCoins(self,num): #returns True if player has enough coins
        if(self.coins>=num):
            return True
        else:
            return False
    
    def isThereAnotherItemInPos(self,position): #returns True if there is another item in the chosen position
        if(self.pos[position]!=''):
            return True
        else:
            return False

    def removeItem(self,item): #removes 1 of the given item
        if(self.itemDict[item]>0):
            self.itemDict[item]-=1
        else:
            print("ERROR")
    
    def clearPosition(self,obj): #opens up a position
        try:
            if(self.materialDict[obj]):
                self.materialDict[obj]=0
                return "DONE"
        except:
            try:
                if(self.itemDict[obj]):
                    self.itemDict[obj]=0
                    return "DONE"
            except:
                return "FAIL"
        

    def areThereEnoughMaterials(self,material,num): #Trade-returns True if there are at least num materias in the inventory
        if(self.materialDict[material]>=num):
            return True
        else:
            return False

    def checkIfMaterialsAreMissing(self,item): #returns True if there are enough materials for the item to be made
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            if self.materialDict[i]==0:
                return False
        return True

    def addItem(self,item): #adds 1 of the given item
        self.itemDict[item]+=1

    def removeMaterials(self,item): #removes the materials the item consists of
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            self.materialDict[i]-=1

    def addMaterialsItem(self,item): #adds the materials the item consists of
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            self.materialDict[i]+=1

    def dismantle(self,item): #dismantles an item
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            self.materialDict[i]+=1
        self.removeItem(item)

    def enoughSpace(self): #returns True if there is enough space in the inventory
        spaces=0
        for i in self.materialDict:
            if self.materialDict[i]>0:
                spaces+=1
        for j in self.itemDict:
            if self.itemDict[j]>0:
                spaces+=1
        for k in self.mystery_items:
            if self.mystery_items[k]>0:
                spaces+=1
        if self.size>spaces:
            return True
        else:
            return False

    def enoughSpaceForCrafting(self,item): #returns True if there is enough space for crafting
        self.removeMaterials(item)
        if(self.enoughSpace()):
            self.addMaterialsItem(item)
            return True
        else:
            self.addMaterialsItem(item)
            return False

    def canPlayerCraftNewItem(self): #returns True if after the addition of some materials the player can craft a new item
        for item in self.itemDict:
            if self.checkIfMaterialsAreMissing(item):
                return True
        return False

    def addMaterials(self,material,num): #adds a specific amount of a material
        self.materialDict[material]+=num
    
    def removeMaterial(self,material,num):#removes a specific amount of a material
        self.materialDict[material]-=num

    def addItemToPos(self,item,position): #adds blueprint in a specific spot in crafting page
        self.pos[position]=item

    def tradeItems(self,item1,item2,quantity): #trades item 1 for item 2 (2-1)
        if(self.areThereEnoughMaterials(item1,quantity)):
            self.removeMaterial(item1,quantity)
            self.addMaterials(item2,quantity/2)
        else:
            print("Not enough materials")