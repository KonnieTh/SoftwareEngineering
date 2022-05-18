from constructableItem import ConstructableItem


class GumGun(ConstructableItem):
    def __init__(self,weightOfAmmo):
        self.weightOfAmmo = weightOfAmmo
        self.ammo = 1