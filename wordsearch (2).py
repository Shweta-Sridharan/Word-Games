import pygame, random, sys, math
from pygame import mixer
#import wordbend
#from wordbend import *
import wordbendrules
score=0

l=[]
import pygame_widgets as pw

def main():
    pygame.init()
    pygame.mixer.init()


    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('wordsearch')
    #pygame.mixer.music.load('windows microsoft error song (techno version) .mp3')
    #pygame.mixer.music.play(-1)



    pimg = pygame.image.load('letter-a.png')
    pX = 250
    pY = 450
    pimg1 = pygame.image.load('letter-b.png')
    pX1 = 43
    pY1 = 350
    pimg2 = pygame.image.load('letter-p.png')
    pX2 = 350
    pY2 = 200
    pimg3 = pygame.image.load('letter-K.png')
    pX3 = 401
    pY3 = 100
    pimg4 = pygame.image.load('letter-n new.png')
    pX4 = 240
    pY4 = 150
    pimg5 = pygame.image.load('letter-o.png')
    pX5 = 540
    pY5 = 430
    pimg6 = pygame.image.load('letter-m.png')
    pX6 = 700
    pY6 = 150



    clicked = ''
    font = pygame.font.Font('freesansbold.ttf', 32)

    words_formed = ''
    font = pygame.font.Font('freesansbold.ttf', 32)


    font = pygame.font.Font('freesansbold.ttf', 32)
    global score



    textX = 10
    textY = 10


    clock = pygame.time.Clock()
    timer = 60  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).

    def show_score(x, y):
        score_val = font.render('Score:' + str(score), True, (255, 255, 255))
        screen.blit(score_val, (x, y))


    def show_clicked(x, y):
        clicked_val = font.render('Clicked:' + clicked, True, (255, 255, 255))
        screen.blit(clicked_val, (x, y))

    def show_caution(x, y):
        caution_val = font.render('Caution:' + 'min 3 letters.', True, (255, 255, 255))
        screen.blit(caution_val, (x, y))



    def show_words_formed(x, y):
        words_formed_val = font.render('Words formed:' + words_formed, True, (255, 255, 255))
        screen.blit(words_formed_val, (x, y))




    def p(x, y):
        screen.blit(pimg, (x, y))


    def P(x1, y1):
        screen.blit(pimg1, (x1, y1))


    def P2(x2, y2):
        screen.blit(pimg2, (x2, y2))


    def P3(x3, y3):
        screen.blit(pimg3, (x3, y3))


    def P4(x4, y4):
        screen.blit(pimg4, (x4, y4))


    def P5(x5, y5):
        screen.blit(pimg5, (x5, y5))


    def P6(x6, y6):
        screen.blit(pimg6, (x6, y6))

    exitbutton = pw.Button(screen, 40, 530, 140, 35, text='Exit', fontSize=26, margin=50, inactiveColour=(10, 100, 100),
                           pressedColour=(0, 0, 0), radius=2, onClick=lambda: pygame.quit())


     # starter tick

    running = True


    while running:

        screen.fill((0,0,0))

        p(pX, pY)
        P(pX1, pY1)
        P2(pX2, pY2)
        P3(pX3, pY3)
        P4(pX4, pY4)
        P5(pX5, pY5)
        P6(pX6, pY6)

        pX += 1.2
        pY += 1.3
        pX1 += 2.5
        pY1 += 2.7
        pX2 += 2.2
        pY2 += 2.6
        pX3 += 1.8
        pY3 += 2.4
        pX4 += 2.5
        pY4 += 2.3
        pX5 += 2.4
        pX6 += 1.6
        pY5 += 1.7
        pY6 += 2.1

        l1 = [(pX, pY), (pX1, pY1), (pX2, pY2), (pX3, pY3), (pX4, pY4), (pX5, pY5), (pX6, pY6)]
        l2 = ['A', 'B', 'P', 'K', 'N', 'O', 'M']

        d = dict(zip(l1, l2))

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

        if pX3 <= 0:
            pX3 = 0
        elif pX3 > 736:
            pX3 = 0
        if pY3 <= 0:
            pY3 = 0
        elif pY3 > 536:
            pY3 = 0

        if pX4 <= 0:
            pX4 = 0
        elif pX4 > 736:
            pX4 = 0
        if pY4 <= 0:
            pY4 = 0
        elif pY4 > 536:
            pY4 = 0

        if pX5 <= 0:
            pX5 = 0
        elif pX5 > 736:
            pX5 = 0
        if pY5 <= 0:
            pY5 = 0
        elif pY5 > 536:
            pY5 = 0

        if pX6 <= 0:
            pX6 = 0
        elif pX6 > 736:
            pX6 = 0
        if pY6 <= 0:
            pY6 = 0
        elif pY6 > 536:
            pY6 = 0



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos
                for i in d:
                    if (i[0] + 64 > x > i[0] and i[1] + 64 > y > i[1]):

                        clicked += d[i]

                        l3 = ['MAN', 'PAN', 'MAP', 'MOB', 'BAN', 'OAK', 'MOP', 'NAP', 'BOA','POP']

                        l4 = ['AMOK','BONK','KNOB','MONK','BANK']



                        if len(clicked)==3:

                            if clicked in l3:
                                words_formed=clicked

                                if clicked not in l:

                                    l.append(clicked)
                                    score+=1
                                    words_formed=clicked
                                    clicked=''
                                else:
                                    score+=0
                                    words_formed='Oops! Word is done'
                            pass


                        elif len(clicked)==4:
                            if clicked in l4:
                                words_formed = clicked

                                if clicked not in l:

                                    l.append(clicked)
                                    score += 1
                                    words_formed = clicked
                                    clicked = ''
                                else:
                                    score += 0
                                    words_formed = 'Oops! Word is done'


                            else:

                                words_formed = 'Oops! Not a word!'
                                score += 0
                                clicked = ''

        exitbutton.listen(pygame.event.get())
        exitbutton.draw()

        timer -= dt
        if timer <= 0:


            pygame.time.wait(2000)

            wordbendrules.main()

        txt = font.render(str(round(timer, 2)), True,(255,255,255))
        screen.blit(txt, (10, 130))

        dt = clock.tick(30) / 1000




        show_score(textX, textY)
        show_clicked(10, 40)
        show_words_formed(10, 70)
        show_caution(10,100)


        pygame.display.update()



if __name__ == '__main__':
    main()
    pygame.quit()
