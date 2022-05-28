class Inventory:
    def __init__(self):
        self.__coins = 0
        self.__size = 10
        self.revival_token=0
        self.__materialDict = {'cables':0,'gears':0,'metalScraps':0,'oil':0,'springs':0}
        self.__itemDict = {'gum_gun':0,'stun_gun':0,'EMP_grenade':0,'time_travel_grenade':0,'time_freeze_grenade':0,'life_potion':0,'speed_potion':0,'stamina_potion':0}
    
    def craft(self,item): #craft item by calling craft(item_name)
        pass

    def checkIfMaterialsAreMissing(self,material,num):
        if(self.__materialDict[material]>=num):
            return True
        else:
            return False

    def addItem(self,item): #add a specific amount of a material
        self.__itemDict[item]+=1

    def removeMaterials(self,material,num): #remove a specific amount of a material
        if(self.__materialDict[material]>=num):
            self.__materialDict[material]-=num
        else:
            print('Error')

    def dismantle(self,item):
        if(self.__itemDict[item]==0):
            return False
        else:
            self.__itemDict[item]-=1

    def enoughSpace(self):
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

    def canPlayerCraftNewItem(self):
        pass

    def chooseMateriaslForTrade(self):
        pass#?????

    def enoughMateriaslForTrade(self,material,num):
        pass #idio me check if materials are missing

    def addMaterials(self,material,num): #add a specific amount of a material
        self.__materialDict[material]+=num

    def doesPlayerHaveRevivalToken(self):
        if self.revival_token>0:
            return True
        else:
            return False

    def removeTokenFromInventory(self):
        pass

    def tradeItems(self):
        pass

    def addValuableItem(self):
        pass

    def destroyItems(self):
        pass

    def tradeMaterials(self):
        pass

    def addBlueprint(self):
        pass

    

