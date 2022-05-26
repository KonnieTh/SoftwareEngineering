from turtle import speed


class Being():
    def __init__(self,health,speed,jumpHeight):
        self.health=health
        self.speed=speed
        self.jumpHeight=jumpHeight
        self.stunned=False
        self.maxHP = 3

    def isStunned(self):
        if self.stunned == True:
            return True
        else:
            return False
            
class Scientist(Being):
    def __init__(self):
        self.aggroState=False

    def reduceSpeed(self):
        self.speed = self.speed * 0.5
        return speed
    
    
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

    def removeOneLife(self):
        self.health -= 1
        return self.checkLife

    def removeTwoLife(self):
        self.health -= 2
        return self.checkLife

    def reduceSpeed(self):
        self.speed = self.speed * 0.8
        return speed

    def areThereAnyLivesLeft(self):
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

   # def isDamaged(self):
