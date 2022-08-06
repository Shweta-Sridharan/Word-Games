import pygame as pg
import sys
import finale
from pygame import mixer
pg.init()
import homepage
font = pg.font.Font('freesansbold.ttf', 32) 
screen = pg.display.set_mode((800, 600))
def show_main(x, y):#show  coords
    opening = font.render('Logging in...', True, (255, 255, 255))#Enter your coords
    screen.blit(opening, (x, y))
def main():
    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    timer = 2  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).

    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption('homepage')


    font = pg.font.Font('freesansbold.ttf', 34)



    running = True

    while running:


        screen.fill((0,0,0))#0-255,

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        timer -= dt
        if timer <= 0:
            finale.main()
        dt = clock.tick(30) / 1000

        show_main(300, 300)#800,600-x,y
        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()