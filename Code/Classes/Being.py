import math



class Being():
    def __init__(self):
        self.health=3
        self.speed=2
        self.jumpHeight=4
        self.stunned=False
        self.maxHP = 3

    def isStunned(self):
        if self.stunned == True:
            return True
        else:
            return False

    def reduceSpeed(self, num):
        self.speed = self.speed * num
        return self.speed

    def returnToPreviousState():
        pass
      
class Scientist(Being):
    def __init__(self):
        super().__init__()
        self.aggroState=False

    def isCollided():
        pass
    
   
class JetpackScientist(Scientist):
    def __init__(self,jetpackFuel):
        self.jetpackFuel=jetpackFuel
        self.disabled=False

    def isinRadius():
        pass

    def desableElectricDevice():
        pass
class DartScientist(Scientist):
    def __init__(self,dartAmmo):
        self.dartAmmo=dartAmmo



class VacuumScientist(Scientist):
    def __init__(self):
        self.disabled=False

    def isinRadius():
        pass

    def disableElectricDevice():
        pass    
class Alien(Being):
    def __init__(self,stamina):
        super().__init__()
        self.stamina=stamina
        self.liquidForm=False

    def isDamaged(self,objectX,alienX):
        distance = math.sqrt((math.pow(objectX - alienX,2)))
        if distance < 30:
            return True
        else:
            return False

    def removeLives(self,num):
        self.health -= num
        return self.checkLife


    def areThereAnyLivesLeft(self):#--------------
        if self.health == 0 :
            return False
        else:
            return True    

    def setLifesToOne(self):
        self.health = 1
        return self.health

    def setLifesToMax(self):
        self.health = self.maxHP
        return self.health

    
    def checkLife(self):
        if self.health != 0 or self.health != -1:
            return self.health
        else: 
            return 0

