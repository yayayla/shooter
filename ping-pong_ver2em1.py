from pygame import *

back = (50, 50, 255) #цвет фона (background)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
window.fill(back)
speed_x = 1
speed_y = 1
FPS = 60
game = True
finish = False
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < win_height - 120: 
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 120: 
            self.rect.y += self.speed
ball = GameSprite('tennis_ball.jpg', 200, 200, 4, 50, 50)
racket1 = Player('racket.png',10,100,5,10,100)
racket2 = Player('racket.png',500,100,5,10,100)
while game:
    if finish != True: 
        ball.rect.x += speed_x 
        ball.rect.y += speed_y
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball): 
        speed_x *= -1.3
    if ball.rect.y <= 0:
        speed_y *= -1.1
    if ball.rect.y >= 450:
        speed_y *= -1.1
    for e in event.get(): 
        if e.type == QUIT: 
            game = False
    window.fill(back)
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    ball.reset()
    racket1.reset()
    racket2.reset()
    racket1.update_l()
    racket2.update_r()
    
    clock.tick(FPS)
    display.update()