class ActorClass:
    name: str
    max_hit_points: int = 100
    max_stamina_points: int = 100

    def __init__(self, name, max_hit_points, max_stamina_points):
        self.name = name
        self.max_hit_points = max_hit_points
        self.max_stamina_points = max_stamina_points

    @classmethod
    def from_dict(cls, data):
        return ActorClass(**data)
