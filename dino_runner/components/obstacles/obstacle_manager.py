import random
from dino_runner.utils.constants import BIRD, SMALL_CACTUS, LARGE_CACTUS
from .cactus import SmallCactus, LargeCactus
from .bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles=[]

    def update(self, game_speed, player, on_death):
        if len(self.obstacles)==0:
            n = random.randint(0, 3)
            if n == 0 or n == 3:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif n == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif n == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                if on_death():
                    self.obstacles.remove(obstacle)
                else:
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles=[]
