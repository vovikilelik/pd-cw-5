from app.actors.actor_class import ActorClass
from app.items.armor import Armor
from app.items.item import Item
from app.items.weapon import Weapon


class Actor:
    name = None

    actor_class: ActorClass

    armor: Armor
    weapon: Weapon
    skill: Weapon

    hit_points: int
    stamina_points: int

    def __init__(self, name, actor_class: ActorClass, armor: Armor, weapon: Weapon, skill: Weapon, hit_points: int = None, stamina_points: int = None):
        self.name = name

        self.actor_class = actor_class

        self.armor = armor
        self.weapon = weapon
        self.skill = skill

        self.hit_points = actor_class.max_hit_points if hit_points is None else hit_points
        self.stamina_points = actor_class.max_stamina_points if stamina_points is None else stamina_points

    @property
    def max_hit_points(self):
        return self.actor_class.max_hit_points

    def set_hit_points(self, value):
        self.hit_points = min(max(value, 0), self.max_hit_points)

    @property
    def max_stamina_points(self):
        return self.actor_class.max_stamina_points

    def set_stamina_points(self, value):
        self.stamina_points = min(max(value, 0), self.max_stamina_points)

    def add_hit_points(self, value):
        self.set_hit_points(self.hit_points + value)

    def add_stamina_points(self, value):
        self.set_stamina_points(self.stamina_points + value)

    def has_use(self, item: Item):
        return 0 <= self.stamina_points - item.stamina_per_turn

    def use_item(self, item: Item):
        if self.has_use(item):
            self.add_stamina_points(-item.stamina_per_turn)
            return True

        return False

    @property
    def durability(self):
        if self.has_use(self.armor):
            return self.armor.value
        else:
            return 0

    def set_damage(self, value):
        value = max(value - self.durability, 0)
        self.add_hit_points(-value)
        self.add_stamina_points(-self.armor.stamina_per_turn)

    def __str__(self):
        return f'{self.name}: {self.hit_points}/{self.stamina_points}'

    @classmethod
    def from_dict(cls, data):
        actor_class = ActorClass.from_dict(data['actor_class'])

        armor = Armor.from_dict(data['armor'])
        weapon = Weapon.from_dict(data['weapon'])
        skill = Weapon.from_dict(data['skill'])

        return Actor(
            name=data['name'],
            armor=armor,
            weapon=weapon,
            skill=skill,
            actor_class=actor_class,
            hit_points=data['hit_points'],
            stamina_points=data['stamina_points']
        )
