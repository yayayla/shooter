from pygame import *
'''Необходимые классы'''
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
#класс-наследник для спрайта-врага (перемещается сам)
class Enemy1(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy2(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 85:
            self.direction = "right"
        if self.rect.x >= win_width - 490:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Enemy3(GameSprite):
    direction = "up"
    def update(self):
        if self.rect.y <= 85:
                self.direction = "up"
        if self.rect.y >= win_width - 300:
            self.direction = "down"
        if self.direction == "down":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1 
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height)) 
        self.image.fill((color_1, color_2, color_3)) 
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 6)
monster = Enemy1('cyborg.png', win_width - 80, 280, 4)
monster2 = Enemy2('cyborg.png', win_width - 700, 280, 4)
#monster3 = Enemy3('cyborg.png', win_width - 350, 50, 9)
w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 300, 120, 10 ,370)
w5 = Wall(154, 205, 50, 300, 110, 250, 10 )
w6 = Wall(154, 205, 50 ,400, 300, 250, 10)
#win = font.render('YOU WIN!', True, (255, 215, 0))
#lose = font.render('YOU LOSE!', True, (180, 0, 0))
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
final2 = GameSprite('treasure.png', win_width - 50, win_height - 50, 0)
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255,215,0))
lose = font.render('YOU LOSE!',True,(180,0,0))
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
while game:
    #font.init()
    #font = font.Font(None, 70)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True: 
        
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        monster2.update()
        #monster3.update()  
        player.reset()
        monster.reset()
        monster2.reset()
        #monster3.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        final.reset()
        final2.reset()
        if sprite.collide_rect(player,final) and sprite.collide_rect(player, final2):
            finish = True
            window.blit(win, (200, 200)) 
            #money.play()
        if sprite.collide_rect(player,monster) or sprite.collide_rect(player,monster2) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6):
            finish = True
            window.blit(lose,(200,200))
            #kick.play()

    
    display.update()
    clock.tick(FPS)