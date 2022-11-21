import pygame
size = width, height = 1020, 790
black = 0, 0, 0
class Wall:
     def __init__(self, x, y):
        self.image = pygame.image.load("images/wall3.png")
        self.geometry = self.image.get_rect()
        self.geometry.x=x
        self.geometry.y=y

class Wall2:
     def __init__(self, x, y):
        self.image = pygame.image.load("images/wall4.png")
        self.geometry = self.image.get_rect()
        self.geometry.x=x
        self.geometry.y=y
class lvl_1:
    def __init__(self):
        self.y=[Wall(790, 650),Wall(930, 640),Wall(930, 660),Wall(930, 720),Wall(910, 430),Wall(790, 440),Wall(790, 500),Wall(890, 60),Wall(890, 220),Wall(890, 180),Wall(790, 285),Wall(790, 130),Wall(790, 70),Wall(790, 70),Wall(790, 70),Wall(790, 10),Wall(590,235),Wall(590,290),Wall(680,290),Wall(680,250),Wall(680,190),Wall(680,130),Wall(680,70),Wall(680,10),Wall(600,60),Wall(340,0),Wall(500,-10),Wall(590,430),Wall(430,460),Wall(430,500),Wall(440,725),Wall(355,650),Wall(370,395),Wall(280,395),Wall(280,430),Wall(280,490),Wall(280,550),Wall(280,610),Wall(280,670),Wall(280,730),Wall(680,670),Wall(680,640),Wall(680,730),Wall(680,510),Wall(680,510),Wall(680,490),Wall(680,430),Wall(500,375),Wall(500,235),Wall(440,315),Wall(440,180),Wall(440,180),Wall(370,180),Wall(280,65),Wall(280,10),Wall(80, 720),Wall(80, 660),Wall(80, 260),Wall(170, 450),Wall(80, 480),Wall(80, 530),Wall(170, 400),Wall(70, 0), Wall(70, 6),Wall(70, 65),Wall(170, 65),Wall(170, 185),Wall(170, 245),Wall(170, 260)]
        self.x=[Wall2(1010, 780),Wall2(880, 780),Wall2(790, 640),Wall2(810, 640),Wall2(870, 640),Wall2(850, 430),Wall2(790, 430),Wall2(790, 560),Wall2(840, 560),Wall2(900, 560),Wall2(960, 560),Wall2(890, 110),Wall2(950, 110),Wall2(900, 180),Wall2(960, 180),Wall2(970, 345),Wall2(910, 345),Wall2(850, 345),Wall2(790, 345),Wall2(590, 340),Wall2(630, 340),Wall2(620, 115),Wall2(560, 115),Wall2(500, 115),Wall2(440, 115),Wall2(380, 560),Wall2(540, 715),Wall2(500, 715),Wall2(440, 715),Wall2(380, 640),Wall2(340, 640),Wall2(280, 640),Wall2(310, 395),Wall2(290, 395),Wall2(510, 640),Wall2(560, 640),Wall2(620, 640),Wall2(510, 560),Wall2(560, 560),Wall2(620, 560),Wall2(620, 430),Wall2(560, 430),Wall2(500, 430),Wall2(440, 375),Wall2(440, 235),Wall2(390, 310),Wall2(330, 310),Wall2(280, 310),Wall2(320, 180),Wall2(280, 180),Wall2(320, 115),Wall2(280, 115),Wall2(80, 650),Wall2(120, 650),Wall2(80, 580),Wall2(120, 580),Wall2(80, 310),Wall2(115, 310),Wall2(115, 115),Wall2(75, 115)]
        
        
    def return_of_x(self):
        return self.x
    def return_of_y(self):
        return self.y