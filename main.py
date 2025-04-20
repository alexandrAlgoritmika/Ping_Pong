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

def get_finish():
    global finish, text
    if ball.rect.x < 0:
        text = "Player 1 lose"
        finish = True
    if ball.rect.x > 800:
        text = "Player 2 lose"
        finish = True

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
    def init(self):
        self.speed_x = self.speed
        self.speed_y = self.speed
    def move(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
        if self.rect.colliderect(player_1.rect) or self.rect.colliderect(player_2.rect):
            self.speed_x *= -1

win = pg.display.set_mode((850,500))
pg.display.set_caption('PingPong')

win.fill((30,89,69))

run = True
finish = False
text = ''
clock = pg.time.Clock()
ball = Ball('ball.png', 50, 50, 400, 225, 5)
ball.init()
player_1 = Player1('player_1.png', 125, 125, 10, 175, 0)
player_2 = Player2('player_2.png', 125, 125, 715, 175, 0)
number_1 = pg.font.SysFont('arial', 65).render('1', True, (255,255,255))
number_2 = pg.font.SysFont('arial', 65).render('2', True, (255,255,255))

while run:
    if not finish:
        get_move()
        win.fill((30,89,69))
        win.blit(number_1,(200,215))
        win.blit(number_2,(650,215))
        ball.move()
        ball.draw()
        player_1.move()
        player_1.draw()
        player_2.move()
        player_2.draw()
        get_finish()
    else:
        get_move()
        win.fill((30,89,69))
        label = pg.font.SysFont('arial', 65).render(text, True, (255,255,255))
        win.blit(label, (275, 200))
    pg.display.update()
    clock.tick(60)