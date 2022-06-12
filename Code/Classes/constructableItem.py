from item import *


class ConstructableItem(Item):
    def __init__(self,blueprint):
        self.blueprint = blueprint

class ConsumableItem(ConstructableItem):
    def __init__(self):
        self.inInventory = 0

class LifePotion(ConsumableItem):
    def __init__(self,capacity):
        self.capacity = capacity

class SpeedPotion(ConsumableItem):
    def __init__(self,timesSpeed):
        self.timesSpeed = timesSpeed

class StaminaPotion(ConsumableItem):
    def __init__(self,timeStaminaRecovery):
        self.timeStaminaRecovery = timeStaminaRecovery

class EMPGrenade(ConstructableItem):
    def __init__(self,weight,blastRadius):
        self.weight = weight
        self.blastRadius = blastRadius

class TimeTravelGrenade(ConstructableItem):
    def __init__(self,weight,blastRadius):
        self.weight = weight
        self.blastRadius = blastRadius

class TimeFreezeGrenade(ConstructableItem):
    pass
    #nothing for now

class StunGun(ConstructableItem):
    pass
    #nothing for now

class GumGun(ConstructableItem):
    def __init__(self,weightOfAmmo):
        self.weightOfAmmo = weightOfAmmo
        self.ammo = 1

