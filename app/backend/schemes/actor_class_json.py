from app.actors.actor_class import ActorClass
from app.lib.serialization.json_bundle import JsonBundle


class ActorClassJson(JsonBundle[ActorClass]):
    name: str
    max_hit_points: int
    max_stamina_points: int
