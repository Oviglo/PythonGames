import pygame
import typing
from script.Animation import Animation

if typing.TYPE_CHECKING:
    from script.Scene import Scene

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple = (1, 1)):
        super().__init__()
        self.image = pygame.surface.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.animations = {}
        self.current_animation = None
        self.scene = None

    def set_scene(self, scene: Scene) -> None:
        self.scene = scene

    def update(self):
        if self.current_animation != None:
            self.current_animation.update()
            self.image = self.current_animation.get_frame()

    def add_animation(self, name: str, animation: Animation):
        self.animations[name] = animation

    def set_current_animation(self, name: str) -> None:
        if name in self.animations:
            self.current_animation = self.animations[name]
