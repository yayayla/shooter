from pygame import *


back = (20, 0, 145) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('Pin-Pong')
speed_x = 3 
speed_y = 3

game = True
finish = False
clock = time.Clock()
FPS = 60

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(Gamesprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


ball = Gamesprite('pngwing.png', 200, 200, 4, 50, 50)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




    ball.reset()
    ball.update()
    clock.tick(FPS)
    display.update()