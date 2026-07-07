import pygame
from script.Entity import Entity
from script.utils import load_image
from math import ceil

class Floor(Entity):
    def __init__(self, pos: tuple, width: int):
        super().__init__(pos, (64, 64))
        self.image = pygame.surface.Surface((width, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.single_image = load_image("floor")
        self.width = width
        self.delta = 0
        self.is_stop = False
        self.speed = 3.0

    def update(self):
        count = ceil(self.width / 64) + 1
        for i in range(count):
            self.image.blit(self.single_image, ((i * 64) - self.delta, 0))

        self.delta += self.speed

        self.delta = self.delta % 64

        if self.is_stop and self.speed >= 0:
            self.speed = pygame.math.lerp(self.speed, 0, 0.04)

    def stop(self):
        self.is_stop = True

    
