import pygame

from dino_runner.utils.constants import FONT_STYLE



class Score:
    def __init__(self):
        self.score = 0
    
    def update(self,game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
            font = pygame.font.SysFont(FONT_STYLE, 30)
            text_component = font.render(f"Points:{self.score}", True, (0,0,0))
            text_rect = text_component.get_rect()
            text_rect.center = (1000, 50)
            screen.blit(text_component, text_rect)
    
    def show_score(self,screen):
            font = pygame.font.SysFont(FONT_STYLE, 30)
            text_component = font.render(f"Score:{self.score}", True, (20,51,51))
            text_rect = text_component.get_rect()
            text_rect.center = (750, 350)
            screen.blit(text_component, text_rect)


    def reset_score(self):
        self.score=0
