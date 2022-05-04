from src.entity import Entity


class Link:
    def __init__(self, entity_a=None, entity_b=None):
        self.entity_a: Entity = entity_a
        self.entity_b: Entity = entity_b

    def __repr__(self):
        return f"<Link {self.entity_a} {self.entity_b}>"