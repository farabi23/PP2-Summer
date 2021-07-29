import pygame
from pygame.locals import *
import random, time
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
clock = pygame.time.Clock()
 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
speed = 6
 

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

 

pygame.display.set_caption("Hungry Lion")

fonts = pygame.font.Font(None, 20)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.key.get_pressed()
        if pos[pygame.K_a]:
            self.rect.x -= speed
        elif pos[pygame.K_d]:
            self.rect.x += speed
        elif pos[pygame.K_w]:
            self.rect.y -= speed
        elif pos[pygame.K_s]:
            self.rect.y += speed

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def re_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.re_pos()   

class BLock_gr(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
    def eating(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)
    def update(self):
        self.rect.y += random.randint(-1, 2)
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.eating()


class Game():

    def __init__(self):
        self.score = 0
        self.game_over = False

        self.block_list = pygame.sprite.Group()
        self.block_list_eat = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(50):
            block = Block()
            block_eat = BLock_gr()

            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            block_eat.rect.x = random.randrange(SCREEN_WIDTH)
            block_eat.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

            self.block_list_eat.add(block_eat)
            self.all_sprites_list.add(block_eat)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                    

        return False

    def logic(self):

        if not self.game_over:
            self.all_sprites_list.update()

            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            blocks_hit_list_eat = pygame.sprite.spritecollide(self.player, self.block_list_eat, True)

            for block in blocks_hit_list:
                self.score -= 1
                
            for block in blocks_hit_list_eat:
                self.score += 1
                

            if len(self.block_list_eat) == 0:
                self.game_over = True
                
            elif self.score <= -5:
                self.game_over = True
                
    def drawing(self):
        DISPLAYSURF.fill(WHITE)
        score = fonts.render(str(self.score), True, BLACK)
        DISPLAYSURF.blit(score, (6, 6))

        if self.game_over:
            gameoverfont = pygame.font.Font(None, 60)
            gameover = gameoverfont.render('Game Over', True, RED)
            DISPLAYSURF.blit(gameover, (250, 200))

        if not self.game_over:
            self.all_sprites_list.draw(DISPLAYSURF)



game = Game()

DISPLAYSURF = pygame.display.set_mode((700,500))

while True:
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    game.drawing()        
    game.process_events()    
    game.logic()
    pygame.display.update()
    clock.tick(60)

    pygame.QUIT




