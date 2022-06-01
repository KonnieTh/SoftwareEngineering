from Blueprint import Blueprint

class Inventory:
    def __init__(self):
        self.coins = 0
        self.__size = 10
        self.pos={1:'',2:'',3:'',4:''} #positions to place blueprints
        self.__materialDict = {'cables':0,'gears':0,'metalScraps':0,'oil':0,'springs':0}
        self.itemDict = {'gum_gun':0,'stun_gun':0,'EMP_grenade':0,'time_travel_grenade':0,'time_freeze_grenade':0,'life_potion':0,'speed_potion':0,'stamina_potion':0}
    
    def doesPlayerHaveEnoughCoins(self,num): #returns True if player has enough coins
        if(self.__coins>=num):
            return True
        else:
            return False
    
    def isThereAnotherItemInPos(self,position): #returns True if there is another item in the chosen position
        if(self.pos[position]!=''):
            return True
        else:
            return False

    def removeItem(self,item): #removes 1 of the given item
        if(self.__itemDict[item]>0):
            self.__itemDict[item]-=1
        else:
            print("ERROR")
    
    def areThereEnoughMaterials(self,material,num): #Trade-returns True if there are at least num materias in the inventory
        if(self.__materialDict[material]>=num):
            return True
        else:
            return False

    def checkIfMaterialsAreMissing(self,item): #returns True if there are enough materials for the item to be made
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            if self.__materialDict[i]==0:
                return False
        return True

    def addItem(self,item): #adds 1 of the given item
        self.__itemDict[item]+=1

    def removeMaterials(self,item): #removes the materials the item consists of
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            self.__materialDict[i]-=1

    def dismantle(self,item): #dismantles an item
        blueprint=Blueprint(item)
        lis=blueprint.getBlueprint() #list of materials the item consists of
        for i in lis:
            self.__materialDict[i]+=1
        self.removeItem(item)

    def enoughSpace(self): #returns True if there is enough space in the inventory
        spaces=0
        for i in self.__materialDict:
            if self.__materialDict[i]>0:
                spaces+=1
        for j in self.__itemDict:
            if self.__itemDict[j]>0:
                spaces+=1
        if self.__size>spaces:
            return True
        else:
            return False

    def canPlayerCraftNewItem(self): #returns True if after the addition of some materials the player can craft a new item
        for item in self.__itemDict:
            if self.checkIfMaterialsAreMissing(item):
                return True
        return False

    def addMaterials(self,material,num): #adds a specific amount of a material
        self.__materialDict[material]+=num

    def addItemToPos(self,item,position): #adds blueprint in a specific spot in crafting page
        self.pos[position]=item
