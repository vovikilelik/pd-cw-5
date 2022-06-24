from app.actors.actor_class import ActorClass
from app.items.weapon import Weapon


def get_warrior_actor_class():
    return ActorClass('warrior', 100, 20)


def get_warrior_skill():
    return Weapon(name='Сильный пинок', value=20, stamina_per_turn=6)
