class Blueprint():
    def __init__(self,itemTag):
        self.list_of_materials = []
        self.itemTag=itemTag
        self.isActive=True
    
        if(self.itemTag=="gum_gun"):
            self.list_of_materials=["oil","gears","metalScraps"]
        if(self.itemTag=="stun_gun"):
            self.list_of_materials=["oil","springs","metalScraps"]
        if(self.itemTag=="EMP_grenade"):
            self.list_of_materials=["cables","gears"]
        if(self.itemTag=="time_travel_grenade"):
            self.list_of_materials=["cables","metalScraps"]
        if(self.itemTag=="time_freeze_grenade"):
            self.list_of_materials=["cables","springs"]
        if(self.itemTag=="life_potion"):
            self.list_of_materials=["mystery_fluid","oil"]
        if(self.itemTag=="speed_potion"):
            self.list_of_materials=["mystery_fluid","springs"]
        if(self.itemTag=="stamina_potion"):
            self.list_of_materials=["mystery_fluid","gears"]
    
    def getBlueprint(self):
        return  self.list_of_materials

    def activateBlueprint(self):
        self.isActive=True

    def deactivateBlueprint(self):
        self.isActive=False