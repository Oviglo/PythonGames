import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, terrain_size: pygame.Vector2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30)).convert_alpha()
        self.image.fill(pygame.Color(0, 0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color(200, 200, 200), (15, 15), 15)
        self.terrain_size = terrain_size
        self.speed = 6
        self.x_dir = 1
        self.y_dir = 1
        self.rect = self.image.get_rect()
        self.rect.center = (terrain_size.x // 2, terrain_size.y // 2)
        self.bounce_count = 0

        # Son de rebond
        self.sound_bip = pygame.mixer.Sound("sound/bip.wav")

    def update(self):
        self.rect.y += (self.speed * self.y_dir)
        self.rect.x += (self.speed * self.x_dir)

        if (self.rect.y > (self.terrain_size.y - self.rect.h)):
            self.y_dir = -1
            self.sound_bip.play()
        elif ( self.rect.y < 0):
            self.y_dir = 1
            self.sound_bip.play()

        if self.bounce_count >= 10:
            self.speed += 1
            self.bounce_count = 0

    def process_collision(self) -> None:
        groups = self.groups()
        group = groups[0] if len(groups) > 0 else None

        if (group == None):
            return
        
        collided_sprites = pygame.sprite.spritecollide(self, group, False)
        if len(collided_sprites) > 1:
            racquet = collided_sprites[1] if collided_sprites[1] != self else collided_sprites[0]
            racquet_rect = racquet.rect
            if (racquet_rect.left <= self.rect.left):
                self.x_dir = 1
            elif (racquet_rect.right >= self.rect.right):
                self.x_dir = -1
            self.bounce_count += 1
            self.sound_bip.play()

    def out_left(self) -> bool:
        return self.rect.left < 0
    
    def out_right(self) -> bool:
        return self.rect.right > self.terrain_size.x
    
    def reset(self):
        self.rect.center = (self.terrain_size.x // 2, self.terrain_size.y // 2)