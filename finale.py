import pygame, sys
from pygame import mixer
import wordsearch
import loadinpart
import pygame_widgets as pw
import homepage
import wordsearchrules


def main():
    import wordsearch
    import loadinpart
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('wordgames')

    opening = 'Welcome! Click backspace to start!'
    font = pygame.font.Font('freesansbold.ttf', 34)

    pimg = pygame.image.load('game.png')
    pX = 250
    pY = 450
    pimg1 = pygame.image.load('alpha.png')
    pX1 = 130
    pY1 = 350
    pimg2 = pygame.image.load('ga2.png')
    pX2 = 650
    pY2 = 350

    def show_main(x, y):
        opening = font.render('Welcome! Click backspace to start!', True, (255, 255, 255))
        screen.blit(opening, (x, y))

    def p(x, y):
        screen.blit(pimg, (x, y))

    def P(x1, y1):
        screen.blit(pimg1, (x1, y1))

    def P(x2, y2):
        screen.blit(pimg2, (x2, y2))

    running = True
    backbutton = pw.Button(screen, 40, 530, 140, 35, text='Back', fontSize=26, margin=50,
                           inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                           onClick=lambda: homepage.buttonmain())

    while running:

        pX += 0.5
        pY += 0.3
        pX1 += 0.5
        pY1 += 0.7
        pX2 += 1.2
        pY2 += 0.6

        screen.fill((255, 100, 100))
        p(pX, pY)
        P(pX1, pY1)
        P(pX2, pY2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    wordsearchrules.main()




        if pX <= 0:
            pX = 0
        elif pX > 736:
            pX = 0
        if pY <= 0:
            pY = 0
        elif pY > 536:
            pY = 0

        if pX1 <= 0:
            pX1 = 0
        elif pX1 > 736:
            pX1 = 0
        if pY1 <= 0:
            pY1 = 0
        elif pY1 > 536:
            pY1 = 0

        if pX2 <= 0:
            pX2 = 0
        elif pX2 > 736:
            pX2 = 0
        if pY2 <= 0:
            pY2 = 0
        elif pY2 > 536:
            pY2 = 0

        show_main(200, 200)
        backbutton.listen(pygame.event.get())
        backbutton.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()