import pygame as pg 
pg.init() 

win = pg.display.set_mode((850,500))
pg.display.set_caption('PingPong')

win.fill((30,89,69))

run = True
clock = pg.time.Clock()

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    win.fill((30,89,69))
    pg.display.update()
    clock.tick(40)