from app.items.armor import Armor
from app.items.weapon import Weapon


def get_light_weapon():
    return Weapon(name='Нож', value=10, stamina_per_turn=2)


def get_heavy_weapon():
    return Weapon(name='Топор', value=12, stamina_per_turn=6)


def get_light_armor():
    return Armor(name='Кожанка', value=1, stamina_per_turn=1)


def get_middle_armor():
    return Armor(name='Ведьмачий доспех', value=3, stamina_per_turn=3)


def get_heavy_armor():
    return Armor(name='Латы', value=4, stamina_per_turn=4)
