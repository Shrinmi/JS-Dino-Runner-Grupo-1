import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, DEFAULT_TYPE, DIE_IMG, HAMMER_TYPE, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS
from .score import Score
from dino_runner.utils.constants import FONT_STYLE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player= Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = PlayerHeartManager()

        self.death_count=0
        self.score = Score()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        self.game_speed = 15
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.score.reset_score()
        self.power_up_manager.reset_power_ups()
        self.heart_manager.reset_hearts()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.score.score)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_active(self.screen)
        self.heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.screen.fill((127,255,212))#pintar mi ventana
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        
        font = pygame.font.SysFont(FONT_STYLE, 30)
        if self.death_count == 0:#mostrar mensaje bienvenida
            self.screen.blit(RUNNING[0],(half_screen_width -35, half_screen_height -140))#mostrar icono
            text_component = font.render("Press any key to start", True, (20,51,51))
        else:
            self.screen.blit(DIE_IMG,(half_screen_width -35, half_screen_height -140))
            text_component = font.render(f"Number of deaths : {self.death_count}", True, (20,51,51))#mostrar el numero de muertes actuales
            self.screen.blit(text_component, (half_screen_width -300 , half_screen_height +30))
            text_component = font.render(f"You die, press any key to restart", True, (20,51,51)) #mostrar mensaje de volver a jugar
            self.score.show_score(self.screen) # mostrar el puntaje
        text_rect = text_component.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text_component, text_rect)
        
        pygame.display.update()#actualizar ventana
        self.handle_key_events_on_menu() #escuchar eventos

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE 
        is_invencible = has_shield or self.heart_manager.heart_count > 0
        has_hammer = self.player.type == HAMMER_TYPE 
        is_revitalizing = has_hammer or self.heart_manager.heart_count > 0

        if has_hammer:
            if self.heart_manager.heart_count < 6 :
                self.heart_manager.increase_heart()

        if not has_shield and not has_hammer:
            self.heart_manager.reduce_heart()

        if not is_invencible and not is_revitalizing:
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1
        return is_invencible and is_revitalizing 

    def draw_power_up_active(self, screen):
        if self.player.has_power_up:
            time_to_show = round ((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                font = pygame.font.SysFont(FONT_STYLE, 18)
                text_component = font.render(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", True, (0,0,0))
                text_rect = text_component.get_rect()
                text_rect.center = (500, 40)
                screen.blit(text_component, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
                