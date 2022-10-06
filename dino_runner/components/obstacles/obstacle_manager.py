import pygame
import random
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from .cactus import SmallCactus, LargeCactus



class ObstacleManager:
    def __init__(self):
        self.obstacles=[]

    def update(self, game_speed, player, on_death):
        if len(self.obstacles)==0:
            n = random.randint(0, 2)
            if n == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif n == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                on_death()
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles=[]
