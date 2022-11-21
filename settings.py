import pygame

size = width, height = 1020, 790
screen = pygame.display.set_mode(size)

BUTTON_STYLE = {
        "hover_color": pygame.Color('green'),
        "clicked_color": pygame.Color('orange'),
        "clicked_font_color": pygame.Color('black'),
        "hover_font_color": pygame.Color('orange'),
    }

BUTTON_STYLE2 = {
        "hover_color": pygame.Color('red'),
        "clicked_color": pygame.Color('black'),
        "clicked_font_color": pygame.Color('red'),
        "hover_font_color": pygame.Color('white'),
    }

black = 0, 0, 0
white = 255, 255, 255