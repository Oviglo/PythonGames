import pygame
from script.Scene import Scene

class Game:
    def __init__(self, caption: str,  window_sizes: pygame.Vector2, frame_sizes: pygame.Vector2 = None):
        pygame.init()
        self.running: bool = True
        
        pygame.display.set_caption(caption)
        self.win_surf = pygame.display.set_mode(window_sizes)
        frame_sizes = frame_sizes if frame_sizes != None else window_sizes
        self.frame_surf = pygame.surface.Surface(frame_sizes)
        self.clock = pygame.time.Clock()
        self.scene = None
        self.inputs = set()
        self.on_update_callback = None

    def on_update(self, callback: function):
        self.on_update_callback = callback

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.inputs.add(event.key)
                elif event.type == pygame.KEYUP:
                    self.inputs.discard(event.key)

            self.frame_surf.fill(pygame.Color(90, 90, 200))
            # Rendu de la scene
            if self.scene != None:
                self.scene.update()
                self.scene.render(self.frame_surf)

            if self.on_update_callback != None:
                self.on_update_callback()

            pygame.display.flip()
            self.clock.tick(60)

            self.win_surf.blit(pygame.transform.scale(self.frame_surf, self.win_surf.get_rect().size))

    def set_scene(self, scene: Scene):
        self.scene = scene
        self.scene.set_game(self)

    