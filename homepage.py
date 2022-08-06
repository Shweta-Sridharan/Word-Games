import pygame as pg
import pygame_widgets as pw
import finale
import trybuttonlogin
import transitionpage
import register
import scorecomparepage
import rulespage
import logintoseescore
pimg = pg.image.load('vr-gaming.png')
pX = 250
pY = 450
def buttonmain():
    # Creating screen
    pg.init()
    screen = pg.display.set_mode((800, 600))
    font = pg.font.Font('freesansbold.ttf', 32)
    pimg = pg.image.load('game-controller.png')
    pX = 250
    pY = 450

    def show_main(x, y):
        opening = font.render('HOME', True, (255, 255, 255))
        screen.blit(opening, (x, y))
    def p(x, y):
        screen.blit(pimg, (x, y))
    running = True
    exitbutton1= pw.Button(screen, 40, 530, 140, 35, text='Exit',fontSize=26, margin=50,inactiveColour=(100, 100, 100),pressedColour=(255, 255, 255), radius=2,onClick=lambda:pg.quit())
    skipbutton2 = pw.Button(screen, 600, 530, 140, 35, text='Skip to game', fontSize=26, margin=50, inactiveColour=(100, 100, 100),pressedColour=(255, 255, 255), radius=2,onClick=lambda:finale.main())
    registerbutton = pw.Button(screen, 430, 320, 140, 35, text='Register', fontSize=26, margin=50,
                             inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                             onClick=lambda: register.main())
    rulesbutton = pw.Button(screen, 335, 530, 140, 35, text='Rules', fontSize=26, margin=50,
                               inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                               onClick=lambda: rulespage.main())
    scorepagebutton = pw.Button(screen, 335, 430, 140, 35, text='Score chart', fontSize=26, margin=50,
                            inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                            onClick=lambda: logintoseescore.main())

    loginbutton3 = pw.Button(screen, 240, 320, 140, 35, text='Login', fontSize=26, margin=50,inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,onClick=lambda:trybuttonlogin.main())
    while running:

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        exitbutton1.listen(events)
        skipbutton2.listen(events)
        loginbutton3.listen(events)
        registerbutton.listen(events)
        rulesbutton.listen(events)
        scorepagebutton.listen(events)

        registerbutton.draw()
        exitbutton1.draw()
        skipbutton2.draw()
        loginbutton3.draw()
        rulesbutton.draw()
        scorepagebutton.draw()

        pg.display.update()
        show_main(350,10)
        p(340,130)
if __name__ == '__main__':
    buttonmain()
    pg.quit()

