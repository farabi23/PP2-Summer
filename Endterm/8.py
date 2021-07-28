import pygame
import random
from pygame.math import Vector2
import os
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
bright_green = (0, 200, 0)
BLUE = (0, 0, 255)
orange = (255, 123, 7)
game_font = pygame.font.Font(None, 25)
yellow = ((255,255,0))
navy_blue = ((0,0,100))
sky_blue = ((0,255,255))
pink = ((255,100,180))

cell_size = 40
cell_number = 20
high = os.path.abspath("/Users/Farabi/Desktop/higher.txt")

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()

pygame.display.set_caption("My Anaconda don't")


class Walls:
    def __init__(self):
        self.body = [Vector2(5, 8), Vector2(4, 8), Vector2(3, 8), Vector2(2,8),Vector2(1,8)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)    
class Walls2:
    def __init__(self):
        self.body = [Vector2(18, 8), Vector2(17,8), Vector2(16, 8), Vector2(15, 8), Vector2(14 ,8)]   
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)
class Walls3:
    def __init__(self):
        self.body = [Vector2(11, 13), Vector2(10, 13), Vector2(9, 13), Vector2(8, 13)]     
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)    
class Walls4:
    def __init__(self):
        self.body = [Vector2(11, 4), Vector2(10, 4), Vector2(9, 4), Vector2(8,4)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)          
class Walls5:
    def __init__(self):
        self.body = [Vector2(1, 5), Vector2(1, 4), Vector2(1, 3), Vector2(1,2), Vector2(1, 1)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)
class Walls6:
    def __init__(self):
        self.body = [Vector2(1, 15), Vector2(1, 14), Vector2(1, 13), Vector2(1,12), Vector2(1, 11)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)    
class Walls7:
    def __init__(self):
        self.body = [Vector2(18, 15), Vector2(18, 14), Vector2(18, 13), Vector2(18,12), Vector2(18, 11)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)      
class Walls8:
    def __init__(self):
        self.body = [Vector2(18, 5), Vector2(18, 4), Vector2(18, 3), Vector2(18,2), Vector2(18, 1)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)

class Walls9:
    def __init__(self):
        self.body = [Vector2(14, 17), Vector2(14, 16), Vector2(14, 15), Vector2(14,14), Vector2(14, 13)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)
class Walls10:
    def __init__(self):
        self.body = [Vector2(5, 17), Vector2(5, 16), Vector2(5, 15), Vector2(5,14), Vector2(5, 13)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)
class Walls11:
    def __init__(self):
        self.body = [Vector2(5, 5), Vector2(5, 4), Vector2(5, 3), Vector2(5,2)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)                        
class Walls12:
    def __init__(self):
        self.body = [Vector2(14, 5), Vector2(14, 4), Vector2(14, 3), Vector2(14,2)]
    def draw_walls(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, block_rect)
class Fruit:
    def __init__(self):
        # x and y 
        self.randomize()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size) 
        pygame.draw.rect(screen, RED, fruit_rect)
    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x,self.y)

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10),Vector2(4, 10),Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, orange, block_rect)
    def move_snake(self):
        if self.new_block ==True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0]+self.direction)      
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0]+self.direction)      
            self.body = body_copy[:]  
    def add_block(self):
        self.new_block = True

class Snake_2:
    def __init__(self):
        self.body = [Vector2(5, 10),Vector2(4, 10),Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            x_pos = block.x * cell_size 
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, pink, block_rect)
    def move_snake(self):
        if self.new_block ==True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0]+self.direction)      
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0]+self.direction)      
            self.body = body_copy[:]  
    def add_block(self):
        self.new_block = True        

pygame.mixer.init()
class GAME():
    def __init__(self):
        self.snake = Snake()
        #self.snake_2 = Snake_2()
        self.fruit = Fruit()
        self.walls = Walls()
        self.walls2 = Walls2()
        self.walls3 = Walls3()
        self.walls4 = Walls4()
        self.backround()
        self.load_data()
    def update(self):
        #self.snake_2.move_snake()
        self.snake.move_snake()
        self.colliosions()
        self.check_fail()
    def draw_elements(self):
       # self.snake_2.draw_snake()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()
        self.walls.draw_walls()
        self.walls2.draw_walls()
        self.walls3.draw_walls()
        self.walls4.draw_walls()
        
    def colliosions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
           # self.snake_2.add_block()
        if self.fruit.pos == self.walls.body[0] or self.fruit.pos == self.walls.body[1] or self.fruit.pos == self.walls.body[2] or self.fruit.pos == self.walls.body[3] or self.fruit.pos == self.walls.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls2.body[0] or self.fruit.pos == self.walls2.body[1] or self.fruit.pos == self.walls2.body[2] or self.fruit.pos == self.walls2.body[3] or self.fruit.pos == self.walls2.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls3.body[0] or self.fruit.pos == self.walls3.body[1] or self.fruit.pos == self.walls3.body[2] or self.fruit.pos == self.walls3.body[3]:
            self.fruit.randomize()        
        if self.fruit.pos == self.walls4.body[0] or self.fruit.pos == self.walls4.body[1] or self.fruit.pos == self.walls4.body[2] or self.fruit.pos == self.walls4.body[3]:
            self.fruit.randomize()       
 
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.gameover()
        #if not 0 <= self.snake_2.body[0].x < cell_number or not 0 <= self.snake_2.body[0].y < cell_number:
           # self.gameover()    
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls.body[0] or block == self.walls.body[1] or block == self.walls.body[2] or block == self.walls.body[3] or block == self.walls.body[4]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls2.body[0] or block == self.walls2.body[1] or block == self.walls2.body[2] or block == self.walls2.body[3] or block == self.walls2.body[4]:
                self.gameover()               
        for block in self.snake.body[1:]:
            if block == self.walls3.body[0] or block == self.walls3.body[1] or block == self.walls3.body[2] or block == self.walls3.body[3]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls4.body[0] or block == self.walls4.body[1] or block == self.walls4.body[2] or block == self.walls4.body[3]:
                self.gameover()

       # for block in self.snake_2.body[1:]:
           # if block == self.snake_2.body[0]:
                #self.gameover()        
    def load_data(self):
        self.dir = os.path.abspath(__file__)
        with open(os.path.join(self.dir, high), 'w') as f:
            try:
                self.highscore = int(f.write(str(score_text)))
            except:
                self.highscore = 0    

    def gameover(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()

        pygame.mixer.music.stop()
        time.sleep(1)
        screen.fill(BLACK)
        
        end_text = pygame.font.Font(None, 75)
        end = end_text.render('You lost!', True, (RED))
        screen.blit(end, (300, 110))
        words_text = pygame.font. Font(None, 65)
        word = words_text.render('Your Score is '+ score_text, True, (RED))
        screen.blit(word, (250, 310))
       # prev_text = pygame.font.Font(None, 65)
        #prev = prev_text.render('Highscore is '+ str(self.highscore),True, (RED))
        #screen.blit(prev, (250, 610))

        if int(score_text) > self.highscore:
            self.highscore = int(score_text)
            hs = pygame.font.Font(None, 65)
            hs_text = hs.render('New high score is '+ str(self.highscore), True, (RED))
            screen.blit(hs_text, (250, 410))
            with open(os.path.join(self.dir, high), 'w') as f:
                f.write(str(score_text))
            pygame.display.flip()    
        else:
            prev_text = pygame.font.Font(None, 65)
            prev = prev_text.render('Highscore is '+ str(self.highscore),True, (RED))
            screen.blit(prev, (250, 610))

        
        pygame.display.flip()
        time.sleep(5)
        game_over = True
        pygame.quit()
     
        

    def draw_score(self):
        global score_text
        score_text = str(len(self.snake.body) - 3)
        score_surf = game_font.render(score_text, True, (RED))
        score_x = int((cell_size*cell_number) - 60)
        score_y = int((cell_number* cell_size)- 40)
        score_rect = score_surf.get_rect(center = (score_x, score_y))
        screen.blit(score_surf, score_rect)
        p1_text = game_font.render('P1', True, (RED))
        screen.blit(p1_text, (score_x-7, score_y-25))
        screen.blit(score_surf, score_rect)
    def backround(self):
        pygame.mixer.music.load("/Users/Farabi/Desktop/music.wav")
        pygame.mixer.music.play()

class GAME_2():

    def __init__(self):
        self.snake = Snake()
        self.snake_2 = Snake_2()
        self.fruit = Fruit()
        self.backround()
    def update(self):
        self.snake_2.move_snake()
       
        self.colliosions()
        self.check_fail()
    def draw_elements(self):
        self.snake_2.draw_snake()
        
        self.fruit.draw_fruit()
        self.draw_score()
        
    def colliosions(self):
        if self.fruit.pos == self.snake_2.body[0]:

            self.fruit.randomize()
            self.snake_2.add_block()
    def check_fail(self):
        if not 0 <= self.snake_2.body[0].x < cell_number or not 0 <= self.snake_2.body[0].y < cell_number and (not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number):
            self.gameover()
        for block in self.snake_2.body[1:]:
            if block == self.snake_2.body[0]:
                self.gameover()        

    def gameover(self):
        game_over = True
        #screen.fill(BLACK)
        #pygame.time.sleep(0.5)
        #game_over = True
        pygame.quit()

    def draw_score(self):
        #-------------------------------------------
        score_2_text = str(len(self.snake_2.body) - 3)
        score_2_surf = game_font.render(score_2_text, True, (BLUE))
        score_x_2 = int((cell_size*cell_number) - 40)
        score_y_2 = int((cell_number* cell_size)- 40)
        score_2_rect = score_2_surf.get_rect(center = (score_x_2, score_y_2))
        p2_text = game_font.render('P2', True, (BLUE))
        screen.blit(p2_text, (score_x_2-7, score_y_2-25))
        screen.blit(score_2_surf, score_2_rect)
    def backround(self):
        pygame.mixer.music.load("/Users/Farabi/Desktop/music.wav")
        pygame.mixer.music.play()    

# MEDIUM
class GAME_medium():
    def __init__(self):
        self.snake = Snake()
        #self.snake_2 = Snake_2()
        self.fruit = Fruit()
        self.walls = Walls()
        self.walls2 = Walls2()
        self.walls3 = Walls3()
        self.walls4 = Walls4()
        self.walls5 = Walls5()
        self.walls6 = Walls6()
        self.walls7 = Walls7()
        self.walls8 = Walls8()
        self.backround()
        self.load_data()
    def update(self):
        #self.snake_2.move_snake()
        self.snake.move_snake()
        self.colliosions()
        self.check_fail()
    def draw_elements(self):
       # self.snake_2.draw_snake()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()
        self.walls.draw_walls()
        self.walls2.draw_walls()
        self.walls3.draw_walls()
        self.walls4.draw_walls()
        self.walls5.draw_walls()
        self.walls6.draw_walls()
        self.walls7.draw_walls()
        self.walls8.draw_walls()
        
    def colliosions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
           # self.snake_2.add_block()
        if self.fruit.pos == self.walls.body[0] or self.fruit.pos == self.walls.body[1] or self.fruit.pos == self.walls.body[2] or self.fruit.pos == self.walls.body[3] or self.fruit.pos == self.walls.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls2.body[0] or self.fruit.pos == self.walls2.body[1] or self.fruit.pos == self.walls2.body[2] or self.fruit.pos == self.walls2.body[3] or self.fruit.pos == self.walls2.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls3.body[0] or self.fruit.pos == self.walls3.body[1] or self.fruit.pos == self.walls3.body[2] or self.fruit.pos == self.walls3.body[3]:
            self.fruit.randomize()        
        if self.fruit.pos == self.walls4.body[0] or self.fruit.pos == self.walls4.body[1] or self.fruit.pos == self.walls4.body[2] or self.fruit.pos == self.walls4.body[3]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls5.body[0] or self.fruit.pos == self.walls5.body[1] or self.fruit.pos == self.walls5.body[2] or self.fruit.pos == self.walls5.body[3] or self.fruit.pos == self.walls5.body[4]:
            self.fruit.randomize() 
        if self.fruit.pos == self.walls6.body[0] or self.fruit.pos == self.walls6.body[1] or self.fruit.pos == self.walls6.body[2] or self.fruit.pos == self.walls6.body[3] or self.fruit.pos == self.walls6.body[4]:
            self.fruit.randomize()          
        if self.fruit.pos == self.walls7.body[0] or self.fruit.pos == self.walls7.body[1] or self.fruit.pos == self.walls7.body[2] or self.fruit.pos == self.walls7.body[3] or self.fruit.pos == self.walls7.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls8.body[0] or self.fruit.pos == self.walls8.body[1] or self.fruit.pos == self.walls8.body[2] or self.fruit.pos == self.walls8.body[3] or self.fruit.pos == self.walls8.body[4]:
            self.fruit.randomize()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.gameover()
        #if not 0 <= self.snake_2.body[0].x < cell_number or not 0 <= self.snake_2.body[0].y < cell_number:
           # self.gameover()    
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls.body[0] or block == self.walls.body[1] or block == self.walls.body[2] or block == self.walls.body[3] or block == self.walls.body[4]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls2.body[0] or block == self.walls2.body[1] or block == self.walls2.body[2] or block == self.walls2.body[3] or block == self.walls2.body[4]:
                self.gameover()               
        for block in self.snake.body[1:]:
            if block == self.walls3.body[0] or block == self.walls3.body[1] or block == self.walls3.body[2] or block == self.walls3.body[3]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls4.body[0] or block == self.walls4.body[1] or block == self.walls4.body[2] or block == self.walls4.body[3]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls5.body[0] or block == self.walls5.body[1] or block == self.walls5.body[2] or block == self.walls5.body[3] or block == self.walls5.body[4]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls6.body[0] or block == self.walls6.body[1] or block == self.walls6.body[2] or block == self.walls6.body[3] or block == self.walls6.body[4]:
                self.gameover()         
        for block in self.snake.body[1:]:
            if block == self.walls7.body[0] or block == self.walls7.body[1] or block == self.walls7.body[2] or block == self.walls7.body[3] or block == self.walls7.body[4]:
                self.gameover() 
        for block in self.snake.body[1:]:
            if block == self.walls8.body[0] or block == self.walls8.body[1] or block == self.walls8.body[2] or block == self.walls8.body[3] or block == self.walls8.body[4]:
                self.gameover()                      

       # for block in self.snake_2.body[1:]:
           # if block == self.snake_2.body[0]:
                #self.gameover()        
    def load_data(self):
        self.dir = os.path.abspath(__file__)
        with open(os.path.join(self.dir, high), 'w') as f:
            try:
                self.highscore = int(f.write(str(score_text)))
            except:
                self.highscore = 0    

    def gameover(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()

        pygame.mixer.music.stop()
        time.sleep(1)
        screen.fill(BLACK)
        
        end_text = pygame.font.Font(None, 75)
        end = end_text.render('You lost!', True, (RED))
        screen.blit(end, (300, 110))
        words_text = pygame.font. Font(None, 65)
        word = words_text.render('Your Score is '+ score_text, True, (RED))
        screen.blit(word, (250, 310))
       # prev_text = pygame.font.Font(None, 65)
        #prev = prev_text.render('Highscore is '+ str(self.highscore),True, (RED))
        #screen.blit(prev, (250, 610))

        if int(score_text) > self.highscore:
            self.highscore = int(score_text)
            hs = pygame.font.Font(None, 65)
            hs_text = hs.render('New high score is '+ str(self.highscore), True, (RED))
            screen.blit(hs_text, (250, 410))
            with open(os.path.join(self.dir, high), 'w') as f:
                f.write(str(score_text))
            pygame.display.flip()    
        else:
            prev_text = pygame.font.Font(None, 65)
            prev = prev_text.render('Highscore is '+ str(self.highscore),True, (RED))
            screen.blit(prev, (250, 610))

        
        pygame.display.flip()
        time.sleep(5)
        game_over = True
        pygame.quit()
     
        

    def draw_score(self):
        global score_text
        score_text = str(len(self.snake.body) - 3)
        score_surf = game_font.render(score_text, True, (RED))
        score_x = int((cell_size*cell_number) - 60)
        score_y = int((cell_number* cell_size)- 40)
        score_rect = score_surf.get_rect(center = (score_x, score_y))
        screen.blit(score_surf, score_rect)
        p1_text = game_font.render('P1', True, (RED))
        screen.blit(p1_text, (score_x-7, score_y-25))
        screen.blit(score_surf, score_rect)
    def backround(self):
        pygame.mixer.music.load("/Users/Farabi/Desktop/music.wav")
        pygame.mixer.music.play()   

#HARd
class GAME_hard():
    def __init__(self):
        self.snake = Snake()
        #self.snake_2 = Snake_2()
        self.fruit = Fruit()
        self.walls = Walls()
        self.walls2 = Walls2()
        self.walls3 = Walls3()
        self.walls4 = Walls4()
        self.walls5 = Walls5()
        self.walls6 = Walls6()
        self.walls7 = Walls7()
        self.walls8 = Walls8()
        self.walls9 = Walls9()
        self.walls10 = Walls10()
        self.walls11 = Walls11()
        self.walls12 = Walls12()
        self.backround()
        self.load_data()
    def update(self):
        #self.snake_2.move_snake()
        self.snake.move_snake()
        self.colliosions()
        self.check_fail()
    def draw_elements(self):
       # self.snake_2.draw_snake()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()
        self.walls.draw_walls()
        self.walls2.draw_walls()
        self.walls3.draw_walls()
        self.walls4.draw_walls()
        self.walls5.draw_walls()
        self.walls6.draw_walls()
        self.walls7.draw_walls()
        self.walls8.draw_walls()
        self.walls9.draw_walls()
        self.walls10.draw_walls()
        self.walls11.draw_walls()
        self.walls12.draw_walls()
    def colliosions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
           # self.snake_2.add_block()
        if self.fruit.pos == self.walls.body[0] or self.fruit.pos == self.walls.body[1] or self.fruit.pos == self.walls.body[2] or self.fruit.pos == self.walls.body[3] or self.fruit.pos == self.walls.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls2.body[0] or self.fruit.pos == self.walls2.body[1] or self.fruit.pos == self.walls2.body[2] or self.fruit.pos == self.walls2.body[3] or self.fruit.pos == self.walls2.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls3.body[0] or self.fruit.pos == self.walls3.body[1] or self.fruit.pos == self.walls3.body[2] or self.fruit.pos == self.walls3.body[3]:
            self.fruit.randomize()        
        if self.fruit.pos == self.walls4.body[0] or self.fruit.pos == self.walls4.body[1] or self.fruit.pos == self.walls4.body[2] or self.fruit.pos == self.walls4.body[3]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls5.body[0] or self.fruit.pos == self.walls5.body[1] or self.fruit.pos == self.walls5.body[2] or self.fruit.pos == self.walls5.body[3] or self.fruit.pos == self.walls5.body[4]:
            self.fruit.randomize() 
        if self.fruit.pos == self.walls6.body[0] or self.fruit.pos == self.walls6.body[1] or self.fruit.pos == self.walls6.body[2] or self.fruit.pos == self.walls6.body[3] or self.fruit.pos == self.walls6.body[4]:
            self.fruit.randomize()          
        if self.fruit.pos == self.walls7.body[0] or self.fruit.pos == self.walls7.body[1] or self.fruit.pos == self.walls7.body[2] or self.fruit.pos == self.walls7.body[3] or self.fruit.pos == self.walls7.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls8.body[0] or self.fruit.pos == self.walls8.body[1] or self.fruit.pos == self.walls8.body[2] or self.fruit.pos == self.walls8.body[3] or self.fruit.pos == self.walls8.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls9.body[0] or self.fruit.pos == self.walls9.body[1] or self.fruit.pos == self.walls9.body[2] or self.fruit.pos == self.walls9.body[3] or self.fruit.pos == self.walls9.body[4]:
            self.fruit.randomize()    
        if self.fruit.pos == self.walls10.body[0] or self.fruit.pos == self.walls10.body[1] or self.fruit.pos == self.walls10.body[2] or self.fruit.pos == self.walls8.body[3] or self.fruit.pos == self.walls10.body[4]:
            self.fruit.randomize()
        if self.fruit.pos == self.walls11.body[0] or self.fruit.pos == self.walls11.body[1] or self.fruit.pos == self.walls11.body[2] or self.fruit.pos == self.walls11.body[3]:
            self.fruit.randomize() 
        if self.fruit.pos == self.walls12.body[0] or self.fruit.pos == self.walls12.body[1] or self.fruit.pos == self.walls12.body[2] or self.fruit.pos == self.walls12.body[3]:
            self.fruit.randomize()           
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.gameover()
        #if not 0 <= self.snake_2.body[0].x < cell_number or not 0 <= self.snake_2.body[0].y < cell_number:
           # self.gameover()    
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls.body[0] or block == self.walls.body[1] or block == self.walls.body[2] or block == self.walls.body[3] or block == self.walls.body[4]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls2.body[0] or block == self.walls2.body[1] or block == self.walls2.body[2] or block == self.walls2.body[3] or block == self.walls2.body[4]:
                self.gameover()               
        for block in self.snake.body[1:]:
            if block == self.walls3.body[0] or block == self.walls3.body[1] or block == self.walls3.body[2] or block == self.walls3.body[3]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls4.body[0] or block == self.walls4.body[1] or block == self.walls4.body[2] or block == self.walls4.body[3]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls5.body[0] or block == self.walls5.body[1] or block == self.walls5.body[2] or block == self.walls5.body[3] or block == self.walls5.body[4]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls6.body[0] or block == self.walls6.body[1] or block == self.walls6.body[2] or block == self.walls6.body[3] or block == self.walls6.body[4]:
                self.gameover()         
        for block in self.snake.body[1:]:
            if block == self.walls7.body[0] or block == self.walls7.body[1] or block == self.walls7.body[2] or block == self.walls7.body[3] or block == self.walls7.body[4]:
                self.gameover() 
        for block in self.snake.body[1:]:
            if block == self.walls8.body[0] or block == self.walls8.body[1] or block == self.walls8.body[2] or block == self.walls8.body[3] or block == self.walls8.body[4]:
                self.gameover() 
        for block in self.snake.body[1:]:
            if block == self.walls9.body[0] or block == self.walls9.body[1] or block == self.walls9.body[2] or block == self.walls9.body[3] or block == self.walls9.body[4]:
                self.gameover()
        for block in self.snake.body[1:]:
            if block == self.walls10.body[0] or block == self.walls10.body[1] or block == self.walls10.body[2] or block == self.walls10.body[3] or block == self.walls10.body[4]:
                self.gameover()        
        for block in self.snake.body[1:]:
            if block == self.walls11.body[0] or block == self.walls11.body[1] or block == self.walls11.body[2] or block == self.walls11.body[3]:
                self.gameover() 
        for block in self.snake.body[1:]:
            if block == self.walls12.body[0] or block == self.walls12.body[1] or block == self.walls12.body[2] or block == self.walls12.body[3]:
                self.gameover()                                           

       # for block in self.snake_2.body[1:]:
           # if block == self.snake_2.body[0]:
                #self.gameover()        
    def load_data(self):
        self.dir = os.path.abspath(__file__)
        with open(os.path.join(self.dir, high), 'w') as f:
            try:
                self.highscore = int(f.write(str(score_text)))
            except:
                self.highscore = 0    

    def gameover(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()

        pygame.mixer.music.stop()
        time.sleep(1)
        screen.fill(BLACK)
        
        end_text = pygame.font.Font(None, 75)
        end = end_text.render('You lost!', True, (RED))
        screen.blit(end, (300, 110))
        words_text = pygame.font. Font(None, 65)
        word = words_text.render('Your Score is '+ score_text, True, (RED))
        screen.blit(word, (250, 310))
       # prev_text = pygame.font.Font(None, 65)
        #prev = prev_text.render('Highscore is '+ str(self.highscore),True, (RED))
        #screen.blit(prev, (250, 610))

        if int(score_text) > self.highscore:
            self.highscore = int(score_text)
            hs = pygame.font.Font(None, 65)
            hs_text = hs.render('New high score is '+ str(self.highscore), True, (RED))
            screen.blit(hs_text, (250, 410))
            with open(os.path.join(self.dir, high), 'w') as f:
                f.write(str(score_text))
            pygame.display.flip()    
        else:
            prev_text = pygame.font.Font(None, 65)
            prev = prev_text.render('Highscore is '+ str(self.highscore),True, (RED))
            screen.blit(prev, (250, 610))

        
        pygame.display.flip()
        time.sleep(5)
        game_over = True
        pygame.quit()
     
        

    def draw_score(self):
        global score_text
        score_text = str(len(self.snake.body) - 3)
        score_surf = game_font.render(score_text, True, (RED))
        score_x = int((cell_size*cell_number) - 60)
        score_y = int((cell_number* cell_size)- 40)
        score_rect = score_surf.get_rect(center = (score_x, score_y))
        screen.blit(score_surf, score_rect)
        p1_text = game_font.render('P1', True, (RED))
        screen.blit(p1_text, (score_x-7, score_y-25))
        screen.blit(score_surf, score_rect)
    def backround(self):
        pygame.mixer.music.load("/Users/Farabi/Desktop/music.wav")
        pygame.mixer.music.play()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

logic = GAME()
logic_2 = GAME_2()
logic_med = GAME_medium()
logic_hard = GAME_hard()

def starting():
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)

    game_over = False
    while not game_over:
        screen.fill((175, 215, 70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == SCREEN_UPDATE:
                logic.update()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if logic.snake.direction.y != 1:
                        logic.snake.direction = Vector2(0, -1)    
                if event.key == pygame.K_DOWN:
                    if logic.snake.direction.y != -1:
                        logic.snake.direction = Vector2(0, 1)    
                if event.key == pygame.K_LEFT:
                    if logic.snake.direction.x != 1:
                        logic.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if logic.snake.direction.x != -1:
                        logic.snake.direction = Vector2(1, 0)     
                        
        
        logic.draw_elements() 
        #fruit.draw_fruit()
        #snake.draw_snake()
        pygame.display.update()    
        clock.tick(75)

    pygame.quit()


def starting_2():
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 100)

    game_over = False
    while not game_over:

        screen.fill((175, 215, 70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == SCREEN_UPDATE:
                logic_med.update()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if logic_med.snake.direction.y != 1:
                        logic_med.snake.direction = Vector2(0, -1)    
                if event.key == pygame.K_DOWN:
                    if logic_med.snake.direction.y != -1:
                        logic_med.snake.direction = Vector2(0, 1)    
                if event.key == pygame.K_LEFT:
                    if logic_med.snake.direction.x != 1:
                        logic_med.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if logic_med.snake.direction.x != -1:
                        logic_med.snake.direction = Vector2(1, 0)     
                        
        
        logic_med.draw_elements() 
        #fruit.draw_fruit()
        #snake.draw_snake()
        pygame.display.update()    
        clock.tick(75)

    pygame.quit()

def starting_3():
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    game_over = False
    while not game_over:

        screen.fill((175, 215, 70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == SCREEN_UPDATE:
                logic_hard.update()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if logic_hard.snake.direction.y != 1:
                        logic_hard.snake.direction = Vector2(0, -1)    
                if event.key == pygame.K_DOWN:
                    if logic_hard.snake.direction.y != -1:
                        logic_hard.snake.direction = Vector2(0, 1)    
                if event.key == pygame.K_LEFT:
                    if logic_hard.snake.direction.x != 1:
                        logic_hard.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if logic_hard.snake.direction.x != -1:
                        logic_hard.snake.direction = Vector2(1, 0)     
                        
        
        logic_hard.draw_elements() 
        #fruit.draw_fruit()
        #snake.draw_snake()
        pygame.display.update()    
        clock.tick(100)

    pygame.quit()
    
def starting_4():
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    game_over = False
    while not game_over:
        
        screen.fill((175, 215, 70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == SCREEN_UPDATE:
                logic.update()
                logic_2.update()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if logic.snake.direction.y != 1:
                        logic.snake.direction = Vector2(0, -1)    
                if event.key == pygame.K_DOWN:
                    if logic.snake.direction.y != -1:
                        logic.snake.direction = Vector2(0, 1)    
                if event.key == pygame.K_LEFT:
                    if logic.snake.direction.x != 1:
                        logic.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if logic.snake.direction.x != -1:
                        logic.snake.direction = Vector2(1, 0)   
                # THE AWSD KEYS FOR THE SECOND SNAKE !!!! ________________________
                if event.key == pygame.K_w:
                    if logic_2.snake_2.direction.y != 1:
                        logic_2.snake_2.direction = Vector2(0, -1)    
                if event.key == pygame.K_s:
                    if logic_2.snake_2.direction.y != -1:
                        logic_2.snake_2.direction = Vector2(0, 1)    
                if event.key == pygame.K_a:
                    if logic_2.snake_2.direction.x != 1:
                        logic_2.snake_2.direction = Vector2(-1, 0)
                if event.key == pygame.K_d:
                    if logic_2.snake_2.direction.x != -1:
                        logic_2.snake_2.direction = Vector2(1, 0)  

                        
                             
        screen.fill((175, 215, 70))
        logic.draw_elements()
        logic_2.draw_elements() 
        #fruit.draw_fruit()
        #snake.draw_snake()
        pygame.display.update()    
        clock.tick(75)

    pygame.quit()
        

def game_intro():

    intro = True
    while intro:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
        screen.fill(WHITE)
        large_text = pygame.font.Font(None, 115)
        text = large_text.render('Welcome', True, BLACK)
        screen.blit(text, (220, 200))
         
        # the buttons
        pygame.draw.rect(screen, GREEN, (200, 300 , 400 , 100))
        pygame.draw.rect(screen, BLACK, (200, 300 , 400 , 100),4)
        
        pygame.draw.rect(screen, yellow, (200, 410 , 400 , 100))
        pygame.draw.rect(screen, BLACK, (200, 410 , 400 , 100),4)

        pygame.draw.rect(screen, RED, (200, 520 , 400 , 100))
        pygame.draw.rect(screen, BLACK, (200, 520 , 400 , 100), 4)

        pygame.draw.rect(screen, sky_blue, (200, 630, 400, 100))
        pygame.draw.rect(screen, BLACK, (200, 630, 400, 100), 4)

        # pressing the buttons
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        #easy        
        if 200 + 400 > mouse[0] > 200 and 300 + 100 > mouse[1] > 300:
            easy_text = pygame.font.Font(None, 85)
            easy = easy_text.render('Easy', True, BLACK)
            screen.blit(easy, (330, 325))
            if click[0] == 1:
                starting()                
        else:
            pygame.draw.rect(screen, GREEN, (200, 300 , 400 , 100))
            pygame.draw.rect(screen, BLACK, (200, 300 , 400 , 100),4)
        #medium    
        if 200 + 400 > mouse[0] > 200 and 410 + 100 > mouse[1] > 410:
            medium_text = pygame.font.Font(None, 85)
            medium = medium_text.render('Medium', True, BLACK)
            screen.blit(medium, (295, 435))
            if click[0] == 1:
                starting_2()
        else:
            pygame.draw.rect(screen, yellow, (200, 410 , 400 , 100))
            pygame.draw.rect(screen, BLACK, (200, 410 , 400 , 100),4)
        #hard
        if 200 + 400 > mouse[0] > 200 and 520 + 100 > mouse[1] > 520:
            hard_text = pygame.font.Font(None, 85)
            hard = hard_text.render('Hard', True, BLACK)
            screen.blit(hard, (330, 545))
            if click[0] == 1:
                starting_3()
        else:
            pygame.draw.rect(screen, RED, (200, 520 , 400 , 100))
            pygame.draw.rect(screen, BLACK, (200, 520 , 400 , 100), 4)
        #2player
        if 200 + 400 > mouse[0] > 200 and 630 + 100 > mouse[1] > 630:
            player_text = pygame.font.Font(None, 85)
            player = player_text.render('2 Players', True, BLACK)
            screen.blit(player, (275, 655))
            if click[0] == 1:
                starting_4()
        else:
            pygame.draw.rect(screen, sky_blue, (200, 630, 400, 100))
            pygame.draw.rect(screen, BLACK, (200, 630, 400, 100), 4)


        pygame.display.update()
        clock.tick(15)

                      
#fruit = Fruit()
#snake = Snake()
game_intro()


