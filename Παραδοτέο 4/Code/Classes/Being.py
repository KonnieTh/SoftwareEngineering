class Being():
    def __init__(self,health,speed,jumpHeight):
        self.health=health
        self.speed=speed
        self.jumpHeight=jumpHeight
        self.stunned=False

class Scientist(Being):
    def __init__(self):
        self.aggroState=False

class JetpackScientist(Scientist):
    def __init__(self,jetpackFuel):
        self.jetpackFuel=jetpackFuel
        self.disabled=False

class DartScientist(Scientist):
    def __init__(self,dartAmmo):
        self.dartAmmo=dartAmmo

class VacuumScientist(Scientist):
    def __init__(self):
        self.disabled=False

class Alien(Being):
    def __init__(self,stamina):
        self.stamina=stamina
        self.liquidForm=False