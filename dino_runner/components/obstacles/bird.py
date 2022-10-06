# import random
# from .obstacle import Obstacles
# from dino_runner.utils.constants import BIRD

# class Bird(Obstacles):
#     def __init__(self,images):
#         type = 0
#         super().__init__(images, type)
#         self.rect.y = 325
        
#     def fly(self):
#         if self.step_index >= 9:
#             self.step_index = 0
#         self.images = BIRD[self.step_index//5] 
#         self.step_index += 1

#     def draw(self, screen):
#         screen.blit(self.images,(self.rect))