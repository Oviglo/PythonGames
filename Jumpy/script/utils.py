import pygame

def load_image(name: str) -> pygame.surface.Surface:
    return pygame.image.load("assets/image/"+ name + ".png")
