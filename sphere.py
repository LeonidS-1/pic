a = input()
n = input()
try:
    a = int(a)
    n = int(n)
    if a%n!=0:
        print('Неправильный формат ввода')
        exit()

except:
    print('Неправильный формат ввода')
    exit()
import pygame as pg
step = a//n
pg.init()
win = pg.display.set_mode((a, a))
ycord = 0
for i in range(a//2): 

    for i in range(a): 
        if i %2!=0:
            pg.draw.rect(win, (255, 255, 255), (i*step, ycord, step, step))

    ycord+=step

    for i in range(a): 
        if i %2==0:
            pg.draw.rect(win, (255, 255, 255), (i*step, ycord, step, step))

    ycord+=step

pg.display.update() 

while a:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            exit()
    