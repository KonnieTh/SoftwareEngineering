from constructableItem import ConstructableItem

class EMPGrenade(ConstructableItem):
    def __init__(self,weight,blastRadius):
        self.weight = weight
        self.blastRadius = blastRadius