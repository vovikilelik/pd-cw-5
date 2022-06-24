from app.items.item import Item
from app.lib.serialization.json_bundle import JsonBundle


class ItemJson(JsonBundle[Item]):
    name: str
    value = ''
    stamina_per_turn = ''
