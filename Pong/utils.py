import pygame

def draw_middle_line(surf: pygame.surface.Surface) -> None:
    line_count = 10
    middle_x = surf.width / 2
    space_size = 20
    for line in range(line_count):
        line_size = (surf.height // line_count) - space_size
        line_y = line * (line_size + space_size)
        pygame.draw.line(surf, pygame.Color(255, 255, 255), (middle_x, line_y), (middle_x, line_y + line_size))

def show_ready_text(surf: pygame.surface.Surface) -> None:
    font = pygame.font.Font("font/PixelifySans-VariableFont_wght.ttf", 40)
    text = font.render("Ready !", False, pygame.Color(180, 40, 180))
    text_rect = text.get_rect()
    text_rect.center = (surf.width // 2, surf.height // 2)
    surf.blit(text, text_rect)

def print_score(surf: pygame.surface.Surface, score1: int, score2: int) -> None:
    font = pygame.font.Font("font/PixelifySans-VariableFont_wght.ttf", 40)
    
    score_text_1 = font.render(str(score1), False, pygame.Color(180, 180, 255))
    score_text_1_rect = score_text_1.get_rect()
    score_text_1_rect.topright = ((surf.get_rect().centerx - 50), 40)
    surf.blit(score_text_1, score_text_1_rect)

    score_text_2 = font.render(str(score2), False, pygame.Color(255, 255, 180))
    score_text_2_rect = score_text_2.get_rect()
    score_text_2_rect.topleft = ((surf.get_rect().centerx + 50), 40)
    surf.blit(score_text_2, score_text_2_rect)