from consumableItem import ConsumableItem 

class StaminaPotion(ConsumableItem):
    def __init__(self,timeStaminaRecovery):
        self.timeStaminaRecovery = timeStaminaRecovery