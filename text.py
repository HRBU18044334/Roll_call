
import pygame,sys
import random

pygame.init()
crash_sound = pygame.mixer.Sound("13571.wav")
crash_sound.set_volume(0.2)
size=width,height=690,800
speed=[10,0]
BLACK=246,246,246#设置刷新的颜色
screen=pygame.display.set_mode(size)
icon=pygame.image.load('PYG03-flower.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('No.1')
screen.fill(BLACK)
wh=[]
for i in range(0,6):
    for j in range(0,6):
        x=30+j*110,30+i*110
        wh.append(x)
name_png=[]
name_rect={}
name_png_={}
tot=30
for i in range(1,32):
    name_png.append(pygame.image.load('./png/'+str(i)+'.png'))
    # screen.blit(name_png[i-1],wh[i-1])
    name_rect[name_png[i-1]]=name_png[i-1].get_rect()
    name_rect[name_png[i-1]].x=wh[i-1][0]
    name_rect[name_png[i-1]].y = wh[i - 1][1]
    screen.blit(name_png[i-1], name_rect[name_png[i-1]])

fps=300
nb=30
fclock=pygame.time.Clock()
def info(pn,re):
    global nb
    tot=10
    while tot:
        x=re.x
        y=re.y
        pygame.draw.rect(screen, BLACK, [x, y, 90, 90], 0)
        screen.blit(pn,[x-10,y])
        pygame.display.flip()
        pygame.time.delay(50)
        pygame.draw.rect(screen, BLACK, [x-10, y, 90, 90], 0)
        screen.blit(pn,[x+10,y])
        pygame.display.flip()
        pygame.time.delay(50)
        tot-=1
    pygame.draw.rect(screen, BLACK, [x + 10, y, 90, 90], 0)
    screen.blit(pn,(wh[nb+1][0],wh[nb+1][1]+130))
    nb+=1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and nb==35:
            screen.fill(BLACK)
            name_png = []
            name_rect = {}
            name_png_ = {}
            tot = 30
            for i in range(1, 32):
                name_png.append(pygame.image.load('./png/' + str(i) + '.png'))
                # screen.blit(name_png[i-1],wh[i-1])
                name_rect[name_png[i - 1]] = name_png[i - 1].get_rect()
                name_rect[name_png[i - 1]].x = wh[i - 1][0]
                name_rect[name_png[i - 1]].y = wh[i - 1][1]
                screen.blit(name_png[i - 1], name_rect[name_png[i - 1]])
            nb=30
        if event.type == pygame.MOUSEBUTTONDOWN and nb<35:
            crash_sound.play()
            x=random.randint(0,tot)
            tot-=1
            name_png_[name_png[x]]=name_rect[name_png[x]]
            info(name_png[x],name_rect[name_png[x]])
            del name_rect[name_png[x]]
            name_png.pop(x)

    pygame.display.update()