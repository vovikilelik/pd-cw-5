from abc import abstractmethod, ABC

from app.actors.actor import Actor


class Unit(ABC):
    owner: Actor

    def __init__(self, owner):
        self.owner = owner

    def start_turn(self):
        self.owner.add_stamina_points(3)

    def attack(self, target: 'Unit'):
        if self.owner.use_item(self.owner.weapon):
            target.owner.set_damage(self.owner.weapon.value)

    def super_attack(self, target: 'Unit'):
        if self.owner.use_item(self.owner.skill):
            target.owner.set_damage(self.owner.skill.value)

    def wait(self):
        self.owner.add_stamina_points(max(6 - self.owner.armor.value, 0) * 2 + 3)

    def surrender(self):
        pass

    @abstractmethod
    def action(self, *units: 'Unit') -> dict:
        pass

    def __str__(self):
        return self.owner.__str__()
