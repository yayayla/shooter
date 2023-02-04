from pygame import *


back = (20, 0, 145) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('Pin-Pong')


game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False





    clock.tick(FPS)
    display.update()