import pygame
from Racquet import Racquet
from Ball import Ball
from utils import draw_middle_line, show_ready_text, print_score
from enum import Enum

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()

sound_win = pygame.mixer.Sound("sound/win.wav")
sound_loose = pygame.mixer.Sound("sound/loose.wav")

pygame.display.set_caption("Pypong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run: bool = True

# Requette du joueur
player_rac = Racquet(40, pygame.Color(44, 44, 200), pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT))
player_rac.set_pos_y((SCREEN_HEIGHT / 2) - (player_rac.rect.h / 2))
opponent_rac = Racquet(SCREEN_WIDTH - 70, pygame.Color(200, 200, 44), pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT))
opponent_rac.set_pos_y((SCREEN_HEIGHT / 2) - (player_rac.rect.h / 2))

ball = Ball(pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT))

sprites = pygame.sprite.Group()
sprites.add(player_rac)
sprites.add(opponent_rac)
sprites.add(ball)
player_inputs = set()

player_score = 0
opponent_score = 0

class GameStat(Enum):
    READY = 0
    PLAY = 1
    PAUSE = 2

game_stat: GameStat = GameStat.READY

ready_time = 0
current_time = 0   

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            player_inputs.add(event.key)
        if event.type == pygame.KEYUP:
            player_inputs.discard(event.key)

    screen.fill(pygame.Color(10, 10, 10))

    # Affiche le score
    print_score(screen, player_score, opponent_score)

    # Dessine la ligne du milieu
    draw_middle_line(screen)

    # Dessine les éléments
    sprites.draw(screen)

    # Etat READY
    if game_stat == GameStat.READY:
        show_ready_text(screen)
    elif game_stat == GameStat.PLAY:
        if pygame.K_UP in player_inputs:
            player_rac.move_up()
        elif pygame.K_DOWN in player_inputs:
            player_rac.move_down()
        
        # Collision entre la balle et une raquette
        ball.process_collision()

        # Mouvement le l'opposant
        opponent_rac.ai_process(ball)

        # Met à jour les éléments
        sprites.update()

        # le joueur perd
        if ball.out_left() or ball.out_right():
            opponent_rac.generate_distance_reaction()
            game_stat = GameStat.READY
            ready_time = pygame.time.get_ticks()
            if ball.out_left():
                opponent_score += 1
                sound_loose.play()
            # le joueur gagne
            if ball.out_right():
                player_score += 1
                sound_win.play()

            ball.reset()


    # Rafraichi l'écran
    pygame.display.flip()
    # Attendre pour la prochaine frame
    clock.tick(60)
    current_time = pygame.time.get_ticks()

    # Mance la partie au bout de 2 secondes
    if (current_time - ready_time >= 2000) and game_stat == GameStat.READY:
        game_stat = GameStat.PLAY
