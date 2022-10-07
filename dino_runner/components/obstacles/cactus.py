import random
from .obstacle import Obstacles


class SmallCactus(Obstacles):
    def __init__(self, images):
        type = random.randint(0, 2)
        super().__init__(images, type)
        self.rect.y = 325

class LargeCactus(Obstacles):
    def __init__(self, images):
        type = random.randint(0, 2)
        super().__init__(images, type)
        self.rect.y = 300