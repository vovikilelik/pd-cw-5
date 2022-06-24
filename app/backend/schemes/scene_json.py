from app.backend.schemes.actor_json import ActorJson
from app.lib.serialization.json_bundle import JsonBundle
from app.scene.scene import Scene


class SceneJson(JsonBundle[Scene]):

    @classmethod
    def actor(cls, scene: Scene):
        __actor_bundle = ActorJson()
        return __actor_bundle.to_dict(scene.units[0].owner)

    @classmethod
    def enemy(cls, scene: Scene):
        __actor_bundle = ActorJson()
        return __actor_bundle.to_dict(scene.units[1].owner)
