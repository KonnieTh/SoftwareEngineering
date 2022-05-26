
from item import Item


class ConstructableItem(Item):
    def __init__(self,blueprint):
        self.blueprint = blueprint