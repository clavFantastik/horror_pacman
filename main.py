from classes import Classes
import pygame
import sys
from settings import screen, width, height, BUTTON_STYLE
import math




def main():
    pygame.init()
    game_over = False
    menu = Classes.Menu()
    game = Classes.Game()
    death = Classes.Death()
    sceene = 'menu'

    while game_over == False:
        for event in pygame.event.get():
            print(game.active, menu.active, sep = " ")
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sceene = 'death'
                    game.active = False
                    menu.active = False
                    death.active = True
                elif event.key == pygame.K_ESCAPE and menu.active == False:
                    menu.active = True
                    game.active = False
                    sceene = 'menu'

                elif event.key == pygame.K_ESCAPE and menu.active == True:
                    menu.active = False
                    game.active = True
                    sceene = 'game'

            if sceene == "game":
                game.player.process_event(event)
            if sceene == 'menu':
                menu.print_menu()
                menu.button_clicked(event)
                if menu.active == False:
                    game.new_game()
                    sceene = 'game'

            if sceene == 'death':
                death.print_death()
                death.button_clicked(event)
                if death.active == False:
                    game.new_game()
                    sceene = 'game'


        if sceene == 'game':
            keys = pygame.key.get_pressed()
            game.check_collision()
            game.player.move()
            game.enemy.move()
            game.print_labyrinth()
            pygame.display.flip()
            pygame.time.wait(10)

        if sceene == 'menu':
            pygame.display.flip()
        if sceene == 'death':
            pygame.display.flip()

    sys.exit()


if __name__ == '__main__':
    main()

