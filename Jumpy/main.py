from script.Game import Game
from script.Scene import Scene
from script.Player import Player, PlayerState
from script.Floor import Floor
from script.Hurdle import Hurdle
import pygame
import random

def create_hurdle():
    hurdle = Hurdle((320, 122))
    scene.add_entity(hurdle)

game = Game("Jumpy", (1280, 720), (320, 180))
scene = Scene()
game.set_scene(scene)

# Sol
floor = Floor((0, 180 - 44), 320)
scene.add_entity(floor)

# Joueur
player = Player((80, 110))
scene.add_entity(player)

init_time: int = 0
random_limit = 80
score: int = 0

def draw_score(surf: pygame.surface.Surface) -> None:
    global score
    font = pygame.font.Font("assets/font/Jersey10-Regular.ttf", 16)
    
    score_text = font.render(str(score), False, pygame.Color(200, 200, 100))
    score_text_rect = score_text.get_rect()
    score_text_rect.topright = ((surf.get_rect().centerx), 4)
    surf.blit(score_text, score_text_rect)

def loop():
    global init_time
    global score
    global random_limit
    current_time = pygame.time.get_ticks()
    if (current_time - init_time) >= 500  and player.state != PlayerState.FALL:
        random_val = random.randint(0, 100)
        score += 1
        if (random_val > random_limit):
            create_hurdle()
        init_time = current_time

    random_limit = max(0, 80 - (score * 0.2))


    player.process_collision()
    if player.state == PlayerState.FALL:
        floor.stop()

    # Affiche le score
    draw_score(game.scene.game.frame_surf)

game.on_update(loop)

def __main__(): 
    game.run()


__main__()