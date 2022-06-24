from random import random

from app.scene.unit import Unit


def has_skill():
    return random() > 0.8


class Ai(Unit):

    def action(self, *units: Unit) -> dict:

        if self.owner.stamina_points < 6:
            self.wait()
            return {'target': 'enemy', 'name': 'wait'}

        for u in units:

            # skip ownself
            if u.owner is self.owner:
                continue

            if has_skill():
                self.attack(u)
            else:
                self.super_attack(u)

            return {'target': 'actor', 'name': 'bit'}

