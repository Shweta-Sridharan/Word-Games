import pygame, sys, random
from PyDictionary import PyDictionary
import time, datetime
import battleshiprules
import trybuttonlogin
import mysql.connector
import scorecomparepage
import pygame_widgets as pw
import trybuttonlogin



con = mysql.connector.connect(host='localhost', user='root', passwd='Ananya@o104', database='mysql')
score2 = 0
import scorepage
import wordsearch



def main():
    global a

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('WORD BEND')

    font = pygame.font.Font('freesansbold.ttf', 32)

    import random
    with open("Words.txt") as fh:
        words = fh.readline().split(',')
    word = random.choice(words)
    d = ''
    global score2
    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    textY = 10

    def show_word(x, y):
        word_val = font.render('THIS IS THE WORD: ' + word, True, (255, 255, 255))
        screen.blit(word_val, (x, y))

    l = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h,
         pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o,
         pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w,
         pygame.K_x, pygame.K_y, pygame.K_z]

    def show_display(x, y):
        display_val = font.render('YOUR WORD: ' + d, True, (255, 255, 255))
        screen.blit(display_val, (x, y))

    def show_score(x, y):
        score_val = font.render('SCORE: ' + str(score2), True, (255, 255, 255))
        screen.blit(score_val, (x, y))

    def show_used(x, y):
        display_val = font.render('USED WORDS: ' + str(used), True, (255, 255, 255))
        screen.blit(display_val, (x, y))

    homebutton = pw.Button(screen, 40, 500, 140, 35, text='Back', fontSize=26, margin=50,
                           inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                           onClick=lambda: homepage.buttonmain())

    clock = pygame.time.Clock()
    timer = 10  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).

    n = ''
    used = []
    running = True
    while running:
        screen.fill((170, 20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    d = d[:-1]
                if event.key in l:

                    d += chr(event.key).upper()

                    if len(d) == 4:
                        dict = PyDictionary()

                        meaning = dict.meaning(d)
                        print(meaning)
                        if meaning:
                            ctr = 0
                            for i in range(len(d)):
                                if word[i] == d[i]:
                                    pass
                                else:
                                    ctr += 1
                            if ctr == 1:
                                score2 += 1

                                used.append(d)
                                c = 0
                                for i in used:
                                    if i == d:
                                        c += 1
                                    if c > 1:
                                        print('no')
                                        used.pop()
                                        score2 -= 1
                                        d = ''
                                        word = used[-1]
                                        print(word)
                                        break

                                if word != used[-1]:
                                    print(used)
                                    word = d
                                    d = ''

                            elif ctr == 0:
                                print('same word has been entered')
                                word = d
                                d = ''
                            else:
                                print('wrong input')
                                if len(used) == 0:
                                    d = ''
                                else:
                                    word = used[-1]
                                    d = ''


                        else:

                            d = ''
                            msg = True
                            while msg:
                                txt = font.render('WORD DOES NOT EXIST', True, (255, 255, 255))
                                screen.blit(txt, (350, 380))
                                pygame.display.update()
                                pygame.display.flip()
                                clock.tick(0.5)

                                msg = False

        timer -= dt
        if timer <= 0:

            pygame.init()

            font = pygame.font.Font('freesansbold.ttf', 32)

            clock = pygame.time.Clock()
            screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption('score')
            totalscore = int(str(wordsearch.score + score2))

            def show_main(x, y):
                opening = font.render('Score:' + str(wordsearch.score + score2), True, (255, 255, 255))
                screen.blit(opening, (x, y))

            clock = pygame.time.Clock()
            screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption('homepage')
            font = pygame.font.Font('freesansbold.ttf', 34)

            running = True

            if con.is_connected():

                mycursor = con.cursor()
                sql1 = "update user_accounts set userscore={} where username like '{}'".format(totalscore,
                                                                                               trybuttonlogin.name1)

                # this sql query is to update the score of the user if they r a member ie. if their username exists in the table
                # uname is the varibale for the user's username

                mycursor.execute(sql1)
                con.commit()
            con.close()
            while running:
                screen.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    show_main(300, 300)
                    pygame.display.update()
                    pygame.time.wait(4000)

        txt = font.render(str(round(timer, 0)), True, (255, 255, 255))
        screen.blit(txt, (0, 105))

        dt = clock.tick(60) / 1000
        show_word(350, 250)
        show_display(350, 300)
        show_score(0, 40)
        show_used(0, 70)

        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()