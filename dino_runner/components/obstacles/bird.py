import random

from .obstacle import Obstacles


class Bird(Obstacles):
    def __init__(self, images):
        type = 0
        super().__init__(images, type)
        self.rect.y = random.choice([200, 270, 325])
        self.step_index = 0

    def draw(self,screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.images[self.step_index//5], self.rect)
        self.step_index += 1 
