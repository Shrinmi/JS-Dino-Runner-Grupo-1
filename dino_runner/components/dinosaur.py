import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_HAMMER, HAMMER_TYPE, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE, DUCKING_SHIELD, JUMPING, RUNNING, DUCKING


DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER} 
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 350
    JUMP_VELOCITY= 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY
        
        self.has_power_up = False
        self.power_up_time_up = 0

    def update(self,user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        if not self.dino_jump:
            if user_input[pygame.K_UP]:
                self.dino_jump = True
                self.dino_run = False
                self.dino_duck = False
            elif user_input[pygame.K_DOWN]:
                self.dino_duck = True
                self.dino_run = False
                self.dino_jump = False
            elif not self.dino_jump:
                self.dino_jump = False
                self.dino_run = True
                self.dino_duck = False
        
        if self.step_index >= 9:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1 #self.step_index=self.step_index+1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_velocity *4
        self.jump_velocity -= 0.8
        print("Jump velocity:", self.jump_velocity)
        print("Y position:", self.dino_rect.y)
        if self.jump_velocity<-self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_POS
            self.jump_velocity=self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index//5] # if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))

    def on_pick_power_up(self, start_time, duration, type):
        self.has_power_up = True
        self.power_up_time_up = start_time + (duration*1000)
        self.type = type