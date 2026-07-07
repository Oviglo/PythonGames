from script.Entity import Entity
from script.utils import load_image
import pygame

class Hurdle(Entity):
    def __init__(self, pos: tuple):
        super().__init__(pos)
        self.image = load_image("hurdle")
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.is_stop = False
        self.speed = 3.0

    def update(self):
        super().update()

        self.rect.right -= self.speed

        if self.rect.right < 0:
            self.kill()

        if self.is_stop and self.speed >= 0:
            self.speed = pygame.math.lerp(self.speed, 0, 0.04)
        if self.speed < 0.5:
            self.speed = 0.0

    def stop(self):
        self.is_stop = True
