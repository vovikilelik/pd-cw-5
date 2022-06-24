from app.items.item import Item


class Weapon(Item):

    def __init__(self, **props):
        Item.__init__(self, **props)
