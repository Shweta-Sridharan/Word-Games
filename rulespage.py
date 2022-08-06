import pygame as pg
import sys
import finale
import pygame_widgets as pw
from pygame import mixer
pg.init()
import homepage
font = pg.font.Font('freesansbold.ttf', 32)
screen = pg.display.set_mode((800, 600))
def show_text1(x, y):#show  coords
    text = font.render('Rules:', True, (255, 255, 255))
    screen.blit(text, (x, y))

def show_text2(x,y):
    text = font.render('1.This is a game that consists of 3 small games.', True, (255, 255, 255))
    screen.blit(text, (x, y))

def show_text3(x,y):
    text = font.render('2.You must play all 3 games to receive a score.', True, (255, 255, 255))
    screen.blit(text, (x, y))

def show_text4(x,y):
    text = font.render('3.The games will load one after the other', True, (255, 255, 255))
    screen.blit(text, (x, y))
    
def show_text5(x,y):
    text = font.render('immediately.', True, (255, 255, 255))
    screen.blit(text, (x, y))

def show_text6(x,y):
    text = font.render('4.If you wish to compare your scores with ', True, (255, 255, 255))
    screen.blit(text, (x, y))
def show_text7(x,y):
    text = font.render('players around the world,', True, (255, 255, 255))
    screen.blit(text, (x, y))

def show_text8(x,y):
    text = font.render('you can do so by registering with us for free!', True,
                       (255, 255, 255))
    screen.blit(text, (x, y))

def main():

    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption('homepage')


    font = pg.font.Font('freesansbold.ttf', 34)
    backbutton = pw.Button(screen, 40, 530, 140, 35, text='Back', fontSize=26, margin=50,
                           inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                           onClick=lambda: homepage.buttonmain())
    skipbutton = pw.Button(screen, 40, 530, 140, 35, text='Play game', fontSize=26, margin=50,
                           inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                           onClick=lambda: finale.main())



    running = True

    while running:


        screen.fill((0,0,0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        show_text1(300, 30)
        show_text2(30, 90)
        show_text3(30, 170)
        show_text4(30, 230)
        show_text5(50,270)
        show_text6(30, 330)
        show_text7(50, 365)
        show_text8(50,400)

        backbutton.listen(pg.event.get())
        backbutton.draw()
        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()