from app.actors.actor_class import ActorClass
from app.items.weapon import Weapon


def get_thief_actor_class():
    return ActorClass('thief', 80, 30)


def get_thief_skill():
    return Weapon(name='Коварный удар', value=15, stamina_per_turn=3)
