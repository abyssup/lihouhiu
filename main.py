#Создай собственный Шутер!

from pygame import *
from pygame import *
from random import randint
mixer.init()
font.init()

class GameSprait(sprite.Sprite):
    def __init__(self, image1, x, y, speed, w=65, h=65):
        super().__init__()
        self.image = transform.scale(image.load(image1), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#игроки 
class Player(GameSprait):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 695:
            self.rect.x += self.speed

class Player2(GameSprait):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 695:
            self.rect.x += self.speed
        
#фрукты осла
class Enemy(GameSprait):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 503:
            self.rect.y = 0
            self.rect.x = randint(0, 650)
# фрукты шрека
class Enemy2(GameSprait):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 503:
            self.rect.y = 0
            self.rect.x = randint(0, 650)
#бомба
class Buum(GameSprait):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 503:
            self.rect.y = 0
            self.rect.x = randint(0, 650)

class Buum2(GameSprait):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 503:
            self.rect.y = 0
            self.rect.x = randint(0, 650)



#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Шрек и Осел")

#задай фон сцены
'''if bl >= 5:
    finish0 = True
    time += FPS
if time >= 10800:
    time = 0
    finish0 = False
    bl = 0'''
background = transform.scale(image.load("0_7c779_5df17311_png.jpg"), (700, 500))
game = True
clock = time.Clock()
FPS = 60

font1 = font.Font(None, 70)
win = font1.render('WIN ШРЕК', True, (255, 215, 0))
text = font1.render('WIN ОСЕЛ', True, (0, 255, 255))

fonter = font.Font(None, 30)

pl = Player('osel.png', 30, 400, 5, 75, 90)
pl2 = Player2('shrek.png', 30, 400, 5, 75, 90)
#фрукты осла
fruit1 = Enemy('pngwing1.png', 60, 0, 3, 65, 45)
fruit21 = Enemy('apple.png', 354, 0, 1, 65, 45)
fruit31 = Enemy('pngwing1.png', 607, 0, 3, 65, 45)
fruit41 = Enemy('apple.png', 100, 0, 2, 65, 45)
fruit51 = Enemy('pngwing1.png', 500, 0, 1, 65, 45)
fruit2 = Enemy('apple.png', 60, 0, 3, 65, 45)
fruit22 = Enemy('pngwing1.png', 354, 0, 1, 65, 45)
fruit32 = Enemy('apple.png', 607, 0, 3, 65, 45)
fruit42 = Enemy('pngwing1.png', 100, 0, 2, 65, 45)
fruit52 = Enemy('apple.png', 500, 0, 1, 65, 45)

fruits1 = sprite.Group()
fruits1.add(fruit1)
fruits1.add(fruit21)
fruits1.add(fruit31)
fruits1.add(fruit41)
fruits1.add(fruit51)
#бомбы осла
bum11 = Buum('bum.png', 30, 0, 5, 65, 65)
bum21 = Buum('bum.png', 300, 0, 5, 65, 65)
bum31 = Buum('bum.png', 500, 0, 4, 65, 65)
bum12 = Buum('bum.png', 30, 0, 5, 65, 65)
bums1 = sprite.Group()
bums1.add(bum11)
bums1.add(bum21)
bums1.add(bum31)
bums1.add(bum12)
#фрукты шрека 

fruits1.add(fruit2)
fruits1.add(fruit22)
fruits1.add(fruit32)
fruits1.add(fruit42)
fruits1.add(fruit52)

finish = False
time = 3
finish0 = False
j = 0
i = 0

while game:
    for e in event.get():
#обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False

        if finish != True:
            window.blit(background, (0, 0))

            pl.reset()
            pl.update()
            pl2.reset()
            pl2.update()
            fruits1.draw(window)
            fruits1.update()

            bums1.draw(window)
            bums1.update()

            sch_osl = fonter.render('счет:' + str(i), True, (255, 255, 255))
            sch = fonter.render('счет: ' + str(j), True, (255, 255, 255))
            window.blit(sch, (10, 10))
            window.blit(sch_osl, (10, 30))
            sprite_list = sprite.spritecollide(pl2, fruits1, False)
            r_list = sprite.spritecollide(pl, fruits1, False)

            for d in r_list:
                i += 1
                d.rect.y = 0
                fruits1.add(d)

            for k in sprite_list:
                j += 1
                k.rect.y = 0
                fruits1.add(k)

        


    clock.tick(FPS)
    display.update()