n = input()
try:
    n = int(n)
    #n = 10
    import pygame as pg
    W = 500
    H = 500
    pg.init()
    win = pg.display.set_mode((W, H))
    win2 = pg.display.set_mode((W, H))
    xn = 500//n//2
    while H:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                exit()
        
        for i in range(n):
            pg.draw.ellipse(win, (255, 255, 255), (0+xn*i, 0, H-xn*i*2, W), 1)
            pg.draw.ellipse(win, (255, 255, 255), (0, 0+xn*i, H, W-xn*i*2), 1)

        pg.display.update() 
except:
    print('Неправильный формат ввода')
    exit()
