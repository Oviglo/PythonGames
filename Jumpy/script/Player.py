from script.Entity import Entity
from script.Animation import Animation
from script.Hurdle import Hurdle
import pygame
from enum import Enum

class PlayerState(Enum):
    RUN = 0
    JUMP = 1
    FALL = 2

class Player(Entity):
    def __init__(self, pos: tuple):
        super().__init__(pos, (28, 34))
        self.state: PlayerState = PlayerState.RUN
        self.add_animation("run", Animation("player_run", 8, 0.08))
        self.add_animation("jump", Animation("player_jump", 3, 0.1, False))
        self.add_animation("fall", Animation("player_fall", 10, 0.08, False))
        self.set_current_animation("run")
        self.floor_x = self.rect.bottom
        self.can_jump = True
        self.velocity_y = 0.0
        self.gravity = 20.0

    def update(self):
        super().update()

        if (pygame.K_SPACE in self.scene.game.inputs):
            self.jump()

        # Gravité
        self.velocity_y = max(-self.gravity, min(self.gravity, self.velocity_y + 0.5))
        self.rect.bottom += self.velocity_y

        if self.rect.bottom >= self.floor_x and self.state:
            self.velocity_y = 0
            if self.state != PlayerState.FALL:
                self.state = PlayerState.RUN
                self.set_current_animation("run")

        if self.state == PlayerState.RUN and self.velocity_y == 0 and not self.can_jump and pygame.K_SPACE not in self.scene.game.inputs:
            self.can_jump = True
        

    def jump(self):
        if self.state != PlayerState.JUMP and self.state != PlayerState.FALL and self.can_jump:
            self.state = PlayerState.JUMP
            self.set_current_animation("jump")
            self.can_jump = False
            self.velocity_y = -8

    def process_collision(self) -> None:
        groups = self.groups()
        group = groups[0] if len(groups) > 0 else None

        if (group == None):
            return
        
        collided_sprites = pygame.sprite.spritecollide(self, group, False)
        if len(collided_sprites) > 2:
            for sp in collided_sprites:
                if isinstance(sp, Hurdle):
                    self.state = PlayerState.FALL
                    self.set_current_animation("fall")
                    self.stop_all_hurdles()

    def stop_all_hurdles(self):
        for en in self.scene.entities:
            if isinstance(en, Hurdle):
                en.stop()