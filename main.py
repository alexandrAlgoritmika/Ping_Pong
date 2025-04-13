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

class Player1(GameSprite):
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 5
    def move_down(self):
        if self.rect.y < 375:
            self.rect.y += 5

win = pg.display.set_mode((850,500))
pg.display.set_caption('PingPong')

win.fill((30,89,69))

run = True
clock = pg.time.Clock()
ball = GameSprite('ball.png', 50, 50, 400, 225)
player_1 = Player1('player_1.png', 125, 125, 10, 175)
player_2 = GameSprite('player_2.png', 125, 125, 715, 175)

while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_w:
                player_1.move_up()
            if e.key == pg.K_s:
                player_1.move_down()

    win.fill((30,89,69))
    ball.draw()
    player_1.draw()
    player_2.draw()
    pg.display.update()
    clock.tick(40)