from script.utils import load_image
import pygame

class Animation:
    def __init__(self, image: str, frame_count: int = 1, frame_duration: float = 1, loop: bool = True):
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.init_time = 0
        self.current_time = 0
        self.current_frame = 0
        self.loop = loop
        self.frame_w = self.image.get_rect().w // frame_count
        print(self.frame_w)

    def update(self):
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.init_time) >= self.frame_duration * 1000:
            if (self.loop or self.current_frame != (self.frame_count -1 )):
                self.current_frame +=1
                self.current_frame = self.current_frame % self.frame_count
                self.init_time = pygame.time.get_ticks()
                self.current_time = 0
        
    def get_frame(self) -> pygame.surface.Surface:
        return self.image.subsurface(pygame.Rect(self.current_frame * self.frame_w, 0, self.frame_w, self.rect.h))
    
