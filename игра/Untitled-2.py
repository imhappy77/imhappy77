from pygame import *

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры

    def update_l(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.x > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.x <  500 - 80:
           self.rect.y += self.speed
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.x > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.x <  500 - 80:
           self.rect.y += self.speed   

back = (200, 255, 255)
window = display.set_mode((600, 500))
window.fill(back)
game = True
finish = False
clock =  time.Clock()
FPS = 60
racket1 = Player ('racket.png', 30, 200, 4, 50, 150)
racket2 = Player ('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER1 LOSE', True,(180,0,0))
lose2 = font.render('PLAYER2 LOSE', True,(180,0,0))
speed_x = 3
speed_y = 3

while game:
    for e in event.get ():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if  sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y >450 or ball.rect.y <0:
            speed_y *= -1
        if ball.rect.x<0:
            finish = True
            window.blit(lose1,(200,200))
            game_over = True
        if ball.rect.x >600:
            finish = True
            window.blit(lose2,(200,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
