import pygame as pg 
pg.init() 

def get_move():
    global run
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_w:
                player_1.speed = 5
            if e.key == pg.K_s:
                player_1.speed = -5
            if e.key == pg.K_UP:
                player_2.speed = 5
            if e.key == pg.K_DOWN:
                player_2.speed = -5
        if e.type == pg.KEYUP:
            if e.key == pg.K_w:
                player_1.speed = 0
            if e.key == pg.K_s:
                player_1.speed = 0
            if e.key == pg.K_UP:
                player_2.speed = 0
            if e.key == pg.K_DOWN:
                player_2.speed = 0
                
        if player_1.rect.y < 0:
            player_1.speed = 0
            player_1.rect.y += 5
        if player_1.rect.y > 375:
            player_1.speed = 0
            player_1.rect.y -= 5

        if player_2.rect.y < 0:
            player_2.speed = 0
            player_2.rect.y += 5
        if player_2.rect.y > 375:
            player_2.speed = 0
            player_2.rect.y -= 5

class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, w, h, x, y, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def move(self):
        self.rect.y -= self.speed

class Player2(GameSprite):
    def move(self):
        self.rect.y -= self.speed

class Ball(GameSprite):
    def move(self):
        self.rect.y += self.speed
        self.rect.x += self.speed

win = pg.display.set_mode((850,500))
pg.display.set_caption('PingPong')

win.fill((30,89,69))

run = True
clock = pg.time.Clock()
ball = Ball('ball.png', 50, 50, 400, 225, 5)
player_1 = Player1('player_1.png', 125, 125, 10, 175, 0)
player_2 = Player2('player_2.png', 125, 125, 715, 175, 0)

while run:
    get_move()
    win.fill((30,89,69))
    ball.move()
    ball.draw()
    player_1.move()
    player_1.draw()
    player_2.move()
    player_2.draw()
    pg.display.update()
    clock.tick(60)