class Blueprint():
    def __init__(self,itemTag):
        self.__list_of_materials = []
        self.itemTag=itemTag
        self.isActive=True
    
        if(self.itemTag=="gum_gun"):
           self.__list_of_materials.append("")
        if(self.itemTag=="stun_gun"):
            self.__list_of_materials.append("")
        if(self.itemTag=="EMP_grenade"):
            self.__list_of_materials.append("")
        if(self.itemTag=="time_travel_grenade"):
            self.__list_of_materials.append("")
        if(self.itemTag=="time_freeze_grenade"):
            self.__list_of_materials.append("")
        if(self.itemTag=="life_potion"):
            self.__list_of_materials.append("")
        if(self.itemTag=="speed_potion"):
            self.__list_of_materials.append("")
        if(self.itemTag=="stamina_potion"):
            self.__list_of_materials.append("")
    
    def getBlueprint(self):
        return  self.__list_of_materials

    def activateBlueprint(self):
        self.isActive=True

    def deactivateBlueprint(self):
        self.isActive=False