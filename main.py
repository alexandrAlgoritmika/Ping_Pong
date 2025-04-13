import pygame as pg 
pg.init() 

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, w, h, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

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