from app.actors.actor import Actor
from app.scene.unit import Unit


def is_lose(unit: Unit):
    return unit.owner.hit_points <= 0


class Scene:
    units: list[Unit]

    def __init__(self, *units):
        self.units = list(units)

    def compile(self, action):
        actor = self.units[0]
        enemy = self.units[1]

        if action['type'] == 'weapon':
            actor.attack(enemy)
        elif action['type'] == 'armor':
            actor.wait()
        elif action['type'] == 'skill':
            actor.super_attack(enemy)

        return enemy.action(actor)

    def is_enough(self):
        for u in self.units:
            if u.owner.hit_points <= 0:
                return True

        return False

    def __str__(self):
        return ' '.join([u.__str__() for u in self.units])
