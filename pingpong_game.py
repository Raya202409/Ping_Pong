#Создай собственный Шутер!

from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hight-205:
            self.rect.y += self.speed

    def updateR(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_hight-205:
            self.rect.y += self.speed

'''class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_hight:
            self.rect.x = randint(80,win_wight - 80)
            self.rect.y = 0
            lost += 1

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_hight:
            self.rect.x = randint(80,win_wight - 80)
            self.rect.y = 0'''

#создай окно игры
lost = 0
cost = 0
win_wight = 700
win_hight = 500
window = display.set_mode((win_wight,win_hight))
display.set_caption('Пинг Понг')
background = transform.scale(image.load('TRAVKA.jpg'),(700,500))
#задай фон сцены

clock = time.Clock()
FPS = 60
# TODO привет,мир

player1 = Player('Снимок.PNG',30,win_hight - 205,60,200,4)

player2 = Player('Снимок.PNG',605,win_hight - 205,60,200,4)


ball = GameSprite('Ballik.png',275,150,75,75,3)

finish = False
game = True
speed_x = 3
speed_y = 3
font.init()
shrift = font.SysFont('verdana',20)
loze1 = font.SysFont('impact',35).render('Игрок 1 пропустил желе!', 1,(250, 40, 240))
loze2 = font.SysFont('impact',35).render('Игрок 2 пропустил желе!', 1,(100, 25, 215))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            pass
    
    if finish != True:
        window.blit(background,(0,0))
        text_lose = shrift.render('Пропущено: '+ str(lost), 1,(255,255,255))
        text_cost = shrift.render('Съедено:'+ str(cost),1, (255,255,255))
        player1.updateL()
        player2.updateR()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if ball.rect.y > win_hight - 75 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1

        if ball.rect.x < -15:
            finish = True
            window.blit(loze1,(200,200))
        
        if ball.rect.x > win_wight-65:
            finish = True
            window.blit(loze2,(200,200))

        player1.reset()
        player2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)