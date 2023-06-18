import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((500,500))

RED = (255,0,0)
YELLOW = (255,255,0)
LIGHT_BLUE = (200,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK =(0,0,0)
WHITE = (255,255,255)
clock = pygame.time.Clock()
class Area():
    def __init__(self,x,y,w,h,color):
        self.fill_color = color
        self.rect = pygame.Rect(x,y,w,h)
    def set_color(self,color):
        self.fill_color = color
    def draw(self):
        pygame.draw.rect(window,self.fill_color,self.rect)        
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)  
    def collide(self,x,y):
        return self.rect.collidepoint(x,y)

class Card(Area):
    def __init__(self,x,y,w,h,color,text,size):
        super().__init__(x, y, w, h, color)
        self.font = pygame.font.SysFont('Verdana', size)
        self.label = self.font.render(text, True, WHITE)
    def fdraw(self,color,shift_x,shift_y):
        self.draw()
        self.outline(color,7)
        window.blit(self.label,(self.rect.x+shift_x,self.rect.y+shift_y))

cards = []
cards.append(Card(20,150,90,135,YELLOW,"Click!",20))
cards.append(Card(140,150,90,135,YELLOW,"Click!",20))
cards.append(Card(260,150,90,135,YELLOW,"Click!",20))
cards.append(Card(380,150,90,135,YELLOW,"Click!",20))

btn_restart = Card(200,350,120,50,BLACK,"restart",30) 


finish = True
T = 20
count = T -1
score = 0
font = pygame.font.SysFont('Consolas', 35)
label_score = font.render("Score:", True, WHITE)
label_time = font.render("Time:", True, WHITE)
time_count = 0
#------------------
total_time = 5
total_score = 5
#-----------------
while(finish):
    time_count +=1
    timer = total_time - time_count//30
    _score = font.render(str(score), True, RED)
    _time = font.render(str(timer), True, WHITE)
    count +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for i in range(len(cards)):
                if cards[i].collide(x,y):
                    if i == rand_num:
                        cards[i].set_color(GREEN)
                        score +=1
                    else:
                        cards[i].set_color(RED)    
                        score = max(0,score-1)  
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if btn_restart.collide(x,y):
                time_count = 0
                score = 0   
                count = T -1             
    if timer >= 0:                    
        if count == T:  
            for i in range(len(cards)):
                cards[i].set_color(BLUE)   
            rand_num = randint(0,3)    
            count = 0    
        window.fill(BLACK)
        window.blit(label_score,(20,20))
        window.blit(_score,(140,20))

        window.blit(label_time,(340,20))
        window.blit(_time,(440,20))
        for i in range(len(cards)):
            if i == rand_num:
                cards[i].fdraw(BLUE,15,50)  
                cards[i].outline(RED,7)
            else:    
                cards[i].draw()
                cards[i].outline(WHITE,7)
    else:
        if score >= total_score:
            window.fill(BLACK) 
            label = font.render("YOU WIN!", True, GREEN)  
        else:
            window.fill(BLACK)  
            label = font.render("YOU LOSE!", True, RED) 

        font1 = pygame.font.SysFont('Consolas', 20)    
        total = font1.render("Total: " +str(score), True, WHITE)     
        window.blit(label,(180,220))   
        window.blit(total,(215,275)) 

        btn_restart.fdraw(WHITE,6,2)



    pygame.display.update()
    
    clock.tick(30)





  