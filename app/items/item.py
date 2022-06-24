class Item:
    name: str = None
    value: int = 0
    stamina_per_turn: int = 0

    def __init__(self, name, value, stamina_per_turn):
        self.name = name
        self.value = value
        self.stamina_per_turn = stamina_per_turn

    @classmethod
    def from_dict(cls, data) -> 'Item':
        return Item(data['name'], data['value'], data['stamina_per_turn'])
