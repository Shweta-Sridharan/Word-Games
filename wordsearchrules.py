import pygame as pg
import sys
import finale
import pygame_widgets as pw
from pygame import mixer
import loadinpart

pg.init()


font = pg.font.Font('freesansbold.ttf', 32)
screen = pg.display.set_mode((800, 600))


def show_text1(x, y):  # show  coords
    text = font.render('Rules:', True, (255, 255, 255))
    screen.blit(text, (x, y))


def show_text2(x, y):
    text = font.render('1.Click on the moving letters to form words.', True, (255, 255, 255))
    screen.blit(text, (x, y))


def show_text3(x, y):
    text = font.render('2.There is a total of 15 words that can be made.', True, (255, 255, 255))
    screen.blit(text, (x, y))


def show_text4(x, y):
    text = font.render('3.Minimum of 3 letter words and a max of 4.', True, (255, 255, 255))
    screen.blit(text, (x, y))


def show_text5(x, y):
    text = font.render('There is a time limit of 50 sec.', True, (255, 255, 255))
    screen.blit(text, (x, y))




def main():
    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption('wordsearchrules')

    font = pg.font.Font('freesansbold.ttf', 34)

    skipbutton = pw.Button(screen, 600, 530, 140, 35, text='Play game', fontSize=26, margin=50,
                           inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                           onClick=lambda: loadinpart.main())

    running = True

    while running:

        screen.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        show_text1(300, 30)
        show_text2(30, 90)
        show_text3(30, 170)
        show_text4(30, 230)
        show_text5(50, 270)


        skipbutton.listen(pg.event.get())
        skipbutton.draw()
        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()