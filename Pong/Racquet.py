import pygame
from Ball import Ball
from random import randint

class Racquet(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, color: pygame.Color, terrain_size: pygame.Vector2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 120))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, terrain_size.y // 2)
        self.speed = 6
        self.terrain_size = terrain_size
        self.distance_reaction = 400

    def generate_distance_reaction(self) -> None:
        self.distance_reaction = randint(200, 650)
        self.speed = randint( 3, 15)

    def set_pos_y(self, pos: int):
        self.rect.y = pos

    def move_up(self):
        if (self.rect.y > 0):
            self.rect.y -= self.speed

    def move_down(self):
        if (self.rect.y < (self.terrain_size.y - self.rect.h)):
            self.rect.y += self.speed

    def ai_process(self, ball: Ball):
        dist = pygame.Vector2(ball.rect.center).distance_to(pygame.Vector2(self.rect.center)) // 1
        if dist < self.distance_reaction:
            self.move_to(ball.rect.centery)

    def move_to(self, pos: int):
        y = pygame.math.lerp(self.rect.centery, pos, self.speed * 0.01)
        self.rect.centery = y
        

