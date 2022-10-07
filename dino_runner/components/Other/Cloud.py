# import random
# from pygame.sprite import Sprite

# from dino_runner.utils.constants import CLOUD


# class Cloud(Sprite):
#     def __init__(self):
#         self.cloud = []
#         self.when_appears = 0

#     def generate_clouds(self, score):
#         if len(self.cloud)==0 and self.when_appears == score:
#             self.when_appears+=random.randint(0, 30)
#             self.cloud.append(CLOUD)

#     def update(self, game_speed, score):
#         self. generate_clouds(score)
#         for clouds in self.cloud:
#             clouds.update(game_speed, self.cloud)

#     def draw(self, screen):
#         for c in self.cloud:
#             self.cloud.draw(screen)