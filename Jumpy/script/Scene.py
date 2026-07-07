import pygame
import typing
from script.Entity import Entity

if typing.TYPE_CHECKING:
    from script.Game import Game

class Scene:
    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.game = None

    def set_game(self, game: Game) -> None:
        self.game = game

    def add_entity(self, entity: Entity) -> None:
        entity.set_scene(self)
        self.entities.add(entity)

    def update(self) -> None:
        self.entities.update()

    def render(self, surf: pygame.surface.Surface) -> None:
        self.entities.draw(surf)
    