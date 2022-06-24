from app.actors.actor import Actor
from app.backend.schemes.actor_class_json import ActorClassJson
from app.backend.schemes.item_json import ItemJson
from app.lib.serialization.json_bundle import JsonBundle


class ActorJson(JsonBundle[Actor]):
    name: str

    armor = ItemJson()
    weapon = ItemJson()
    skill = ItemJson()

    hit_points: int
    stamina_points: int

    actor_class = ActorClassJson()
