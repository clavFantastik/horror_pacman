import pygame
from classes import Lab_lvl
from settings import screen, width, height, BUTTON_STYLE, BUTTON_STYLE2
from button import Button
class Player:
    def __init__(self):
        self.image = pygame.image.load("images/pc3.png")
        self.geometry = self.image.get_rect()
        self.geometry.x=10
        self.geometry.y=15
        self.shift = 0
        self.shift2=0

    def check_edges(self):
        if self.geometry.top <= 0 or self.geometry.bottom >= height:
            self.shift = 0
            self.shift2 = 0
        if self.geometry.left <= 0 or self.geometry.right >= width:
            self.shift = 0
            self.shift2 = 0

    def move(self):
        self.geometry.y += self.shift
        self.geometry.x += self.shift2
        self.check_edges()

    def move_to_start(self):
        self.geometry.x = 10
        self.geometry.y = 15

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.shift = -2
                self.shift2 = 0
            elif event.key == pygame.K_s:
                self.shift = 2
                self.shift2 = 0
            elif event.key == pygame.K_a:
                self.shift2 = -2
                self.shift = 0
            elif event.key == pygame.K_d:
                self.shift2 = 2
                self.shift = 0
        elif event.type == pygame.KEYUP:
            self.shift = 0
            self.shift2=0
                



class Enemy:
    def __init__(self):
        self.image = pygame.image.load("images/pac.png")
        self.geometry = self.image.get_rect()
        self.geometry.x=10
        self.geometry.y=15
        self.shift = 0
        self.shift2= 1

    def check_edges(self):
        if self.geometry.top <= 0 or self.geometry.bottom >= height:
            self.shift = 0
            self.shift2 = 0
        if self.geometry.left <= 0 or self.geometry.right >= width:
            self.shift = 0
            self.shift2 = 0

    def move(self):
        self.geometry.y += self.shift
        self.geometry.x += self.shift2
        self.check_edges()

    def move_to_start(self):
        self.geometry.x = 110
        self.geometry.y = 265







class Labyrinth:
    def __init__(self):
        self.walls = []
        self.walls2 = []
        wallx=0
        wally=0
        wallx2=0
        w_all=Lab_lvl.lvl_1()
        self.walls=w_all.return_of_y()
        self.walls2=w_all.return_of_x()
        for i in range(13):
            self.walls.append(Lab_lvl.Wall(wallx, wally))
            wally+=60
        for i in range(3):
            self.walls2.append(Lab_lvl.Wall2(wallx, 180))
            wallx+=60
        for i in range(15):
            self.walls2.append(Lab_lvl.Wall2(wallx2, wally))
            wallx2+=60
        wallx=1010
        wally=0
        for i in range(13):
            self.walls.append(Lab_lvl.Wall(wallx, wally))
            wally+=60
        wallx2=80
        for i in range(17):
            self.walls2.append(Lab_lvl.Wall2(wallx2, 0))
            wallx2+=60
        wallx=0
        for i in range(3):
            self.walls2.append(Lab_lvl.Wall2(wallx, 395))
            wallx+=60


    def get_walls(self):
        return self.walls
    def get_walls2(self):
        return self.walls2

class Menu:
    def __init__(self):
        pygame.font.init()
        self.active = True
        self.bg = pygame.image.load("images/menu_pict.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, screen.get_size())
        self.font = pygame.font.Font(None, width * height * 3 // 20000)
        self.text = self.font.render("PACMAN", True, pygame.Color('yellow'))
        self.text_rect = self.text.get_rect(center=(width / 2, height / 10))
        button_NewGame = pygame.Rect(250, height / 1.5 + height / 10, 200, 150)
        button_Exit = pygame.Rect(550, height / 1.5 + height / 10, 200, 150)
        self.new_game_button = Button(button_NewGame, pygame.Color('gray'), self.change_sceene, text='New game', **BUTTON_STYLE)
        self.exit_button = Button(button_Exit, pygame.Color('gray'), exit, text='Exit', **BUTTON_STYLE)
    def print_menu(self):
        screen.blit(self.bg, (0, 0))
        screen.blit(self.text, self.text_rect)
        self.new_game_button.update(screen)
        self.exit_button.update(screen)

    def button_clicked(self, event):
        self.new_game_button.check_event(event)
        self.exit_button.check_event(event)


    def change_sceene(self):
        self.active = False


class Game:
    def __init__(self):
        self.walls = Labyrinth().get_walls()
        self.walls2 = Labyrinth().get_walls2()
        self.player = Player()
        self.enemy = Enemy()
        self.active = False

    def print_labyrinth(self):
        screen.fill(pygame.Color('black'))
        screen.blit(self.enemy.image, self.enemy.geometry)
        screen.blit(self.player.image, self.player.geometry)
        for i in self.walls:
            screen.blit(i.image, i.geometry)
        for i in self.walls2:
            screen.blit(i.image, i.geometry)

    def check_collision(self):
        for i in self.walls:
            if self.player.geometry.colliderect(i.geometry):
                self.player.geometry.x += -self.player.shift2
                self.player.shift2 = 0
                self.player.geometry.y += -self.player.shift
                self.player.shift = 0
        for i in self.walls:
            if self.enemy.geometry.colliderect(i.geometry):
                self.enemy.shift=-self.enemy.shift
                

        for i in self.walls2:
            if self.player.geometry.colliderect(i.geometry):
                self.player.geometry.y += -self.player.shift
                self.player.shift = 0
                self.player.geometry.x += -self.player.shift2
                self.player.shift2 = 0
        for i in self.walls2:
            if self.enemy.geometry.colliderect(i.geometry):
                
                self.enemy.shift2=-self.enemy.shift2
    def new_game(self):
        self.active = True
        self.enemy.move_to_start()
        self.player.move_to_start()
        self.print_labyrinth()
        pygame.display.flip()
        self.player.shift = 0
        self.player.shift2 = 0

class Death:
    def __init__(self):
        self.active = False
        self.bg = pygame.image.load("images/game_over.jpg").convert()
        self.bg = pygame.transform.smoothscale(self.bg, screen.get_size())
        button_NewGame = pygame.Rect(250, height / 1.5 + height / 10, 200, 150)
        button_Exit = pygame.Rect(550, height / 1.5 + height / 10, 200, 150)
        self.new_game_button = Button(button_NewGame, pygame.Color('gray'), self.change_sceene, text='New game', **BUTTON_STYLE2)
        self.exit_button = Button(button_Exit, pygame.Color('gray'), exit, text='Exit', **BUTTON_STYLE2)

    def print_death(self):
        screen.blit(self.bg, (0, 0))
        self.new_game_button.update(screen)
        self.exit_button.update(screen)

    def button_clicked(self, event):
        self.new_game_button.check_event(event)
        self.exit_button.check_event(event)

    def change_sceene(self):
        self.active = False