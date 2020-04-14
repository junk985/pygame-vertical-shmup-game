import pygame
import random
import os
from os import path
from random import randint
import time
import sys
 
# MODULLER BOLUMU BITTI

# RENK VE KALITE

oyunklasoru = os.path.abspath(__file__)
resimklasoru = os.path.join(os.path.dirname(__file__), "img")
sesklasoru = os.path.join(os.path.dirname(__file__), "snd")



EN = 1024
BOY = 768
FPS = 60


BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)
YESIL = (0, 255, 0)
MAVI = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((EN,BOY))
pygame.display.set_caption("test")
clock = pygame.time.Clock()


Z = 5000



yazitipi = pygame.font.match_font("arial")


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH

    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, YESIL, fill_rect)


def yaziyazma(yuzey, yazi, boyut, x, y):
    yazitp = pygame.font.Font(yazitipi, boyut)
    yaziyuzey = yazitp.render(yazi,True,BEYAZ)
    yazi_rect = yaziyuzey.get_rect()
    yazi_rect.midtop = (x, y)
    yuzey.blit(yaziyuzey,yazi_rect)


def yenidusman():
    m = dusman()
    all_sprites.add(m)
    dusmanlar.add(m)

def canbari(yuzey,x, y, yzd):
    if yzd < 0:
        yzd = 0
    uzunlk = 100
    ykslk = 10
    doldr = (yzd / 100) * uzunlk
    dd = pygame.Rect(x,y, uzunlk,ykslk)
    fill_rect = pygame.Rect(x,y, doldr, ykslk)
    pygame.draw.rect(yuzey,YESIL,fill_rect)
    pygame.draw.rect(yuzey,BEYAZ,dd,2)
    
def canlar(yuzey,x,y ,canlar, rm):
    rm.set_colorkey(BEYAZ)
    for i in range(canlar):
        rmrect = rm.get_rect()
        rmrect.x = x + 30 * i
        rmrect.y = y
        yuzey.blit(rm, rmrect)

    
def guc(yuzey,x,y ,canlar, rm):
    rm.set_colorkey(BEYAZ)
    for i in range(canlar):
        rmrect = rm.get_rect()
        rmrect.x = x + 30 * i
        rmrect.y = y
        yuzey.blit(rm, rmrect)

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = oyuncu_resmi
        self.image.set_colorkey(SIYAH)
        self.rect = self.image.get_rect()
        self.radius = 10
        #pygame.draw.circle(self.image,KIRMIZI,self.rect.center, self.radius)
        self.rect.center = (EN / 2,BOY / 2)
        self.speedx = 0
        self.speedy = 0
        self.asure = 250
        self.son = pygame.time.get_ticks()
        self.can = 3
        self.gzl = False
        zn = pygame.time.get_ticks()
        self.guc = 1
        self.zaman = pygame.time.get_ticks()
        
    def update(self):
        if self.gzl and pygame.time.get_ticks() - self.gz_sure > 3000:
            self.gzl = False
            time.sleep(0.5)
            self.rect.centerx = EN / 2
            self.rect.bottom = BOY / 2

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:            
            self.speedy = 5
        if keystate[pygame.K_z]:
            self.atis()
        if keystate[pygame.K_LEFT] and keystate[pygame.K_LSHIFT]:
            self.speedx = -2.5
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_LSHIFT]:
            self.speedx = 2.5
        if keystate[pygame.K_UP] and keystate[pygame.K_LSHIFT]:
            self.speedy = -2.5
        if keystate[pygame.K_DOWN] and keystate[pygame.K_LSHIFT]:            
            self.speedy = 2.5
        if keystate[pygame.K_z] and keystate[pygame.K_LSHIFT]:
            self.atis()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rect.clamp_ip(screen.get_rect())

        if self.speedx > 0:
            self.image = oyuncu_resmi_sag
            self.image.set_colorkey(SIYAH)
        if self.speedx < 0:
            self.image = oyuncu_resmi_sol
            self.image.set_colorkey(SIYAH)
        if self.speedx == 0:
            self.image = oyuncu_resmi
            self.image.set_colorkey(SIYAH)

    def gucl(self):
        self.guc += 0.1
        self.zaman = pygame.time.get_ticks()

    def atis(self):
        zamn = pygame.time.get_ticks()
        if zamn - self.son > self.asure:
            self.son = zamn
            if self.guc < 2:
                mermi = Mermi(self.rect.centerx,self.rect.top)
                all_sprites.add(mermi)
                mermiler.add(mermi)
                atissesi.play()
            elif self.guc >= 2 and self.guc < 3:
                mermi = Mermi(self.rect.left,self.rect.top)
                mermi2 = Mermi(self.rect.right,self.rect.top)
                all_sprites.add(mermi2)
                mermiler.add(mermi2)
                all_sprites.add(mermi)
                mermiler.add(mermi)
                atissesi.play()
            elif self.guc >= 3 and self.guc < 4:
                mermi = Mermi(self.rect.centerx  + 30,self.rect.top)
                mermi2 = Mermi(self.rect.centerx - 30,self.rect.top)
                mermi3 = Mermi(self.rect.centerx,self.rect.top)
                all_sprites.add(mermi)
                mermiler.add(mermi)
                all_sprites.add(mermi2)
                mermiler.add(mermi2)
                all_sprites.add(mermi3)
                mermiler.add(mermi3)
                atissesi.play()
            elif self.guc >= 4:
                mermi = Mermi(self.rect.left,self.rect.top)
                mermi2 = Mermi(self.rect.right,self.rect.top)
                mermi3 = Mermi(self.rect.centerx - 30,self.rect.bottom)
                mermi4 = Mermi(self.rect.centerx + 30,self.rect.bottom)
                mermi3.speedx = -4
                mermi4.speedx =  4
                all_sprites.add(mermi)
                mermiler.add(mermi)
                all_sprites.add(mermi2)
                mermiler.add(mermi2)
                all_sprites.add(mermi3)
                mermiler.add(mermi3)
                all_sprites.add(mermi4)
                mermiler.add(mermi4)
                atissesi.play()
            if self.guc > 4:
                self.guc = 4
                

    def gizle(self):
        self.gzl = True
        self.gz_sure = pygame.time.get_ticks()
        self.rect.center = (EN / 2,100)

def invert(num):
    if num > 0:
        numnew = "-" + str(num)
        num = int(numnew)
    elif num == 0:
        pass
    elif num < 0:
        num = int(abs(num))
    return num

class boss1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bos
        self.image.set_colorkey(SIYAH)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        #pygame.draw.circle(self.image,KIRMIZI,self.rect.center, self.radius)
        self.rect.x = EN / 2
        self.rect.y = 150
        self.speedy = 0
        self.speedx = 8
        self.asure = 250
        self.son = pygame.time.get_ticks()
        self.health = 100

        
    def update(self):
        if self.health == 0:
            self.kill()
            del self
        i = 2 
        while (i % 2 == 0):
            self.atis()
            i += 1 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rect.clamp_ip(screen.get_rect())
        if self.rect.centerx > 1000:
            self.speedx = -8
        if self.rect.centerx < 100:
            self.speedx = 8

        
    def atis(self):
        zamn = pygame.time.get_ticks()
        if zamn - self.son > self.asure:
            self.son = zamn
            mermi = dusmMermi(self.rect.left,self.rect.top,0,7)
            mermi2 = dusmMermi(self.rect.right,self.rect.top,0,7)
            mermi3 = dusmMermi(self.rect.left,self.rect.top,-5,7)
            mermi4 = dusmMermi(self.rect.right,self.rect.top,5,7)
            mermi5 = dusmMermi(self.rect.left,self.rect.bottom,-10,0)
            mermi6 = dusmMermi(self.rect.right,self.rect.bottom,10,0)
            all_sprites.add(mermi)
            dmermiler.add(mermi)
            all_sprites.add(mermi2)
            dmermiler.add(mermi2)
            all_sprites.add(mermi3)
            dmermiler.add(mermi3)
            all_sprites.add(mermi4)
            dmermiler.add(mermi4)
            all_sprites.add(mermi5)
            dmermiler.add(mermi5)
            all_sprites.add(mermi6)
            dmermiler.add(mermi6)
            if self.health < 25:
                mermi7 = dusmMermi(self.rect.right,self.rect.centery,5,5)
                mermi8 = dusmMermi(self.rect.left,self.rect.centery,5,5)
                all_sprites.add(mermi7)
                dmermiler.add(mermi7)
                all_sprites.add(mermi8)
                dmermiler.add(mermi8)
class dusman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(yaratikresimler)
        self.image.set_colorkey(SIYAH)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        #pygame.draw.circle(self.image,KIRMIZI,self.rect.center, self.radius)
        self.rect.x = random.randrange(EN - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.asure = 250
        self.son = pygame.time.get_ticks()

        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > BOY + 10 or self.rect.left < -25 or self.rect.right > EN + 20:
            self.rect.x = random.randrange(EN - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(-10, 10)

    def atis(self):
        zamn = pygame.time.get_ticks()
        if zamn - self.son > self.asure:
            self.son = zamn
            mermi = dusmMermi(self.rect.left,self.rect.top,0)
            mermi2 = dusmMermi(self.rect.right,self.rect.top,0)
            mermi3 = dusmMermi(self.rect.centerx - 50,self.rect.top,0)
            all_sprites.add(mermi)
            dmermiler.add(mermi)
            all_sprites.add(mermi2)
            dmermiler.add(mermi2)
            all_sprites.add(mermi3)

class siss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(resimklasoru, "sis.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = -500 
        self.rect.y = random.randint(0,480)
        self.speedx = random.randint(1,3)
        self.speedy = 0
    
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > EN:
            self.kill()

class bolum(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(resimklasoru, "bolum1.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = EN / 2
        self.rect.y = BOY / 4
        self.speedx = 0
        self.speedy = 0

    def update(self):
        simdi = pygame.time.get_ticks()
        if simdi > 25000:
            self.kill()
            
class Mermi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(resimklasoru, "mermi.png")).convert_alpha()
        self.image.set_colorkey(BEYAZ)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = 0
        self.radius = int(self.rect.width * .85 / 2)
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class dusmMermi(pygame.sprite.Sprite):
    def __init__(self, x, y, xspd,yspd):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(resimklasoru, "dmermi.png")).convert_alpha()
        self.image.set_colorkey(BEYAZ)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = yspd
        self.speedx = xspd
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > BOY:
            self.kill()



class Pow(pygame.sprite.Sprite):
    def __init__(self, mrkz):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["kalkan","guc"])
        self.image = pov[self.type]
        self.image.set_colorkey(SIYAH)
        self.rect = self.image.get_rect()
        self.rect.center = mrkz
        self.speedy = 2
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > BOY:
            self.kill()  


class Patlama(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = patlamanm[self.size][0]
        self.image.set_colorkey(BEYAZ)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100

    def update(self):
        zmn = pygame.time.get_ticks()
        if zmn - self.last_update > self.frame_rate:
            self.last_update = zmn
            self.frame += 1
            if self.frame == len(patlamanm[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = patlamanm[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



# OYUNCU VE YARATIKLAR BOLUMU BITTI


def main():
    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()

def bitisscreen():
    
    screen.blit(arkaplan2, arkaplansekl2)
    pygame.mixer.music.load(os.path.join(sesklasoru,"muzik.ogg"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    yaziyazma(screen, "test", 64, EN / 2, BOY / 4)
    yaziyazma(screen, "test", 22,
              EN / 2, BOY / 2)
    yaziyazma(screen, "test", 18, EN / 2, BOY * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def yenisis():
    a = siss()
    all_sprites.add(a)
    sis.add(a)



arkaplan = pygame.image.load(os.path.join(resimklasoru,"buyukgol.png")).convert()
arkaplansekl = arkaplan.get_rect()
arkaplan2 = pygame.image.load(os.path.join(resimklasoru,"arkaplan.png")).convert()
arkaplansekl2 = arkaplan2.get_rect()
bos = pygame.image.load(os.path.join(resimklasoru, "boss1.png")).convert_alpha()
oyuncu_resmi = pygame.image.load(os.path.join(resimklasoru, "adam.png")).convert_alpha()
oyuncu_resmi_sol = pygame.image.load(os.path.join(resimklasoru, "adamsol.png")).convert_alpha()
oyuncu_resmi_sag = pygame.image.load(os.path.join(resimklasoru, "adamsag.png")).convert_alpha()
kalp = pygame.image.load(os.path.join(resimklasoru,"kalp.png")).convert()
yaratikresimler = []
yaratiklar = ["peri.png","gucluperi.png","ruzgar.png","peri2.png"]

for resim in yaratiklar:
    yaratikresimler.append(pygame.image.load(path.join(resimklasoru,resim)).convert_alpha())

patlamanm = {}
patlamanm["lg"] = []
patlamanm["sm"] = []
patlamanm["oyuncu"] = []
for i in range(3):
    dosya = "pat{}.png".format(i)
    resm = pygame.image.load(os.path.join(resimklasoru, dosya)).convert_alpha()
    resm.set_colorkey(SIYAH)
    resm_lg = pygame.transform.scale(resm,(75,75))
    patlamanm["lg"].append(resm_lg)
    resm_sm = pygame.transform.scale(resm,(32,32))
    patlamanm["sm"].append(resm_sm)
    dosy = "patl{}.png".format(i)
    rsm = pygame.image.load(os.path.join(resimklasoru,dosy)).convert_alpha()
    rsm.set_colorkey(SIYAH)
    patlamanm['oyuncu'].append(rsm)
pov = {}
pov["kalkan"] = pygame.image.load(os.path.join(resimklasoru,"kalkan.png"))
pov["guc"] = pygame.image.load(os.path.join(resimklasoru,"guc.png"))


    
atissesi = pygame.mixer.Sound(os.path.join(sesklasoru, "vurus.wav"))
olme_sesler = []
for ses in ["oldurme2.wav","oldurme.wav"]:
    olme_sesler.append(pygame.mixer.Sound(os.path.join(sesklasoru, ses)))
pygame.mixer.music.load(os.path.join(sesklasoru,"muzik.ogg"))
pygame.mixer.music.set_volume(0.4)

ggsesi = pygame.mixer.Sound(os.path.join(sesklasoru, "olme.wav"))
               
secici = random.choice(olme_sesler)

pygame.mixer.music.play(loops=-1)

p = 0


calisma = True
oyunbitis = True
while calisma:
    zmn = pygame.time.get_ticks()
    if zmn >= 22000:
        for i in range(1):
            b = bolum()
            all_sprites.add(b)
    if zmn > 1000:
         p += 1
         if p % 100 == 0:
              yenisis()
    if zmn > 5000 and zmn < 5018:
        for i in range(1):
            t = boss1()
            all_sprites.add(t)
            bosslar.add(t)
            
    if oyunbitis:
        bitisscreen()
        oyunbitis = False
        all_sprites = pygame.sprite.Group()
        dusmanlar = pygame.sprite.Group()
        bs1 = boss1()
        bosslar = pygame.sprite.Group()
        mermiler = pygame.sprite.Group()
        dmermiler = pygame.sprite.Group()
        guclendirmeler = pygame.sprite.Group()
        sis = pygame.sprite.Group()
        oyuncu = Oyuncu()
        oyuncular = pygame.sprite.Group()
        oyuncular.add(oyuncu)
        all_sprites.add(oyuncu)
        skor = 0
        for i in range (10):
            yenidusman()



    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisma = False
            
    all_sprites.update()
    
    mcarp = pygame.sprite.groupcollide(dusmanlar,mermiler,True ,True)
    for carpp in mcarp:
            skor += 50 - carpp.radius
            pygame.mixer.Sound(secici).play()
            ptl = Patlama(carpp.rect.center, "lg")
            all_sprites.add(ptl)
            if random.random() > 0.2:
                guc = Pow(carpp.rect.center)
                all_sprites.add(guc)
                guclendirmeler.add(guc)
            yenidusman()

    ga = pygame.sprite.groupcollide(bosslar,mermiler,False,True)
    for carpp in ga:
            skor += 50 - carpp.radius
            pygame.mixer.Sound(secici).play()
            bs1.health -= 1
            print(bs1.health)

   
    ncarp = pygame.sprite.spritecollide(oyuncu,dmermiler,True, pygame.sprite.collide_circle)
    for arp in ncarp:
        pygame.mixer.Sound(ggsesi).play()
        ptl = Patlama(arp.rect.center, "lg")
        all_sprites.add(ptl)
        bom = Patlama(oyuncu.rect.center,'oyuncu')
        all_sprites.add(bom)  
        oyuncu.can -= 1

    carpisma = pygame.sprite.spritecollide(oyuncu,dusmanlar, True, pygame.sprite.collide_circle)
    for carp in carpisma:
        pygame.mixer.Sound(ggsesi).play()
        ptl = Patlama(carp.rect.center, "lg")
        all_sprites.add(ptl)
        yenidusman()
        bom = Patlama(oyuncu.rect.center,'oyuncu')
        all_sprites.add(bom)  
        oyuncu.can -= 1
            
    pcarp = pygame.sprite.spritecollide(oyuncu,guclendirmeler, True)
    for crp in pcarp:
        if crp.type == "kalkan":
            skor += 50
        if crp.type == "guc":
            oyuncu.gucl()
            
    if oyuncu.can == 0 and not bom.alive():
        oyunbitis = True



        
    q = int(oyuncu.guc)
    screen.fill(BEYAZ)
    screen.blit(arkaplan, arkaplansekl)
    all_sprites.draw(screen)
    pygame.display.set_caption("The Awkward Lake FPS :" + "{:.2f}".format(clock.get_fps()))
    yaziyazma(screen, str(int(skor)) + " points", 18, EN / 2,10)
    draw_shield_bar(screen, EN / 2, 40, bs1.health)
    canlar(screen, EN - 100,5, oyuncu.can, kalp)
    yaziyazma(screen, str(q) + " power", 18, EN / 4,10)
    pygame.display.flip()
    
pygame.quit()
