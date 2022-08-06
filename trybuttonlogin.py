import pygame as pg
import finaltouches
import mysql.connector
import trybuttonlogin
import pygame_widgets as pw
import homepage
name1 = ''
con = mysql.connector.connect(host='localhost', user='root', passwd='Ananya@o104', database='mysql')
from pygame.locals import *
import hashlib, uuid
import transitionpage

pg.init()
font = pg.font.Font(None, 32)
font1 = pg.font.Font(None, 27)
screen = pg.display.set_mode((800, 600))
enter = ''

if con.is_connected():

    def show_un(x, y):
        clicked_val = font.render('Enter username:' + enter, True, (255, 255, 255))
        screen.blit(clicked_val, (x, y))


    def show_pwd(x, y):
        clicked_val = font.render('Enter password:' + enter, True, (255, 255, 255))
        screen.blit(clicked_val, (x, y))


      # password they are entering



    def show_incorrectpwd(x, y):
        clicked_val = font.render('Incorrect username or password', True, (255, 255, 255))
        screen.blit(clicked_val, (x, y))


    pg.init()
    pg.mixer.init()

    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption('login-page')
    font = pg.font.Font(None, 32)
    smallfont = pg.font.SysFont('Corbel', 16)
    clock = pg.time.Clock()
    input_box1 = pg.Rect(100, 85, 140, 32)
    input_box2 = pg.Rect(100, 340, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color1 = color_inactive
    color2 = color_inactive
    active1 = False
    active2 = False
    text1 = ''
    text2 = ''
    name1=''

    pwd1 = ''
    pwd = ''
    done = False
    registerbutton = pw.Button(screen, 600, 500, 140, 35, text='Register', fontSize=26, margin=50,
                               inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                               onClick=lambda: register.main())


    def main():
        global pwd
        global width
        global height
        global text
        global name1
        global pwd1
        screen = pg.display.set_mode((800, 600))
        backbutton = pw.Button(screen, 40, 530, 140, 35, text='Back', fontSize=26, margin=50,
                               inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                               onClick=lambda: homepage.buttonmain())
        import mysql.connector
        con = mysql.connector.connect(host='localhost', user='root', passwd='Ananya@o104', database='mysql')
        global pwd

        pg.init()
        pg.mixer.init()

        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('register-page')
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box1 = pg.Rect(100, 100, 140, 32)
        input_box2 = pg.Rect(100, 300, 140, 32)
        input_box3 = pg.Rect(100, 400, 140, 32)

        color_inactive = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')
        color1 = color_inactive
        color2 = color_inactive
        color3 = color_inactive
        active1 = False
        active2 = False
        active3 = False
        text1 = ''
        text2 = ''
        text3 = ''
        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN:

                    # If the user clicked on the input_box rect.
                    if input_box1.collidepoint(event.pos):
                        print(event.pos)

                        # Toggle the active variable.
                        active1 = not active1
                        active2 = False
                        active3 = False
                    elif input_box2.collidepoint(event.pos):
                        print(event.pos)
                        active2 = not active2
                        active1 = False
                        active3 = False
                    elif input_box3.collidepoint(event.pos):
                        print(event.pos)
                        active3 = not active3
                        active2 = False
                        active1 = False
                    else:
                        active1 = False
                        active2 = False
                        active3 = False
                    # Change the current color of the input box.
                    color1 = color_active if active1 else color_inactive
                    color2 = color_active if active2 else color_inactive
                    color3 = color_active if active3 else color_inactive

                if event.type == pg.KEYDOWN:
                    if active1:
                        if event.key == pg.K_RETURN:
                            print(text1)

                            active1 = False


                        elif event.key == pg.K_BACKSPACE:
                            text1 = text1[:-1]
                        elif event.key != pg.K_CAPSLOCK:
                            text1 += event.unicode

                        else:
                            text1 += event.unicode


                    elif active2:
                        if event.key == pg.K_RETURN:
                            print(pwd)
                            text2 = ''
                            atcive2 = False


                        elif event.key == pg.K_BACKSPACE:
                            text2 = text2[:-1]
                            pwd = pwd[:-1]
                        elif event.key != pg.K_CAPSLOCK:
                            text2 += '*'
                            pwd += event.unicode
                        else:
                            text2 += '*'
                            pwd += event.unicode

                    elif active3:
                        active2 = False
                        if event.key == pg.K_RETURN:
                            print(confpwd)

                            atcive3 = False
                        elif event.key == pg.K_BACKSPACE:
                            text3 = text3[:-1]
                            confpwd = confpwd[:-1]
                        elif event.key != pg.K_CAPSLOCK:
                            text3 += '*'
                            confpwd += event.unicode
                        else:
                            text3 += '*'
                            confpwd += event.unicode
            if con.is_connected():
                try:

                    mycursor = con.cursor()

                    sql = 'Select * from user_accounts'
                    mycursor.execute(sql)

                    r = mycursor.fetchall()
                    for i in r:

                        if event.type == pg.KEYDOWN:

                            if i[1] == text1:
                                print('right')

                                if event.key == pg.K_RETURN:
                                    active1 = False

                                    if event.key == pg.K_RETURN:

                                        if pwd != i[2]:
                                            if event.key == pg.K_RETURN:


                                                    show_incorrectpwd(300, 440)
                                                    active2 = True
                                                    pg.display.update()
                                                    pg.display.flip()


                                        else:
                                            name1 = i[1]
                                            pwd1 = i[2]
                                            print('please wait..logging in.')
                                            plswait = 'PLEASE WAIT...LOGGING IN.'

                                            pg.time.wait(1000)

                                            transitionpage.main()
                                            con.commit()




                            elif event.key == pg.K_RETURN:
                                if event.key == pg.K_RETURN:

                                    if pwd != i[2]:
                                        if event.key == pg.K_RETURN:
                                            show_incorrectpwd(300, 440)

                                            pg.display.update()
                                            pg.display.flip()



                except mysql.connector.Error as e:
                    print(e)

            else:
                print('Connection not establised.')

            screen.fill((30, 30, 30))
            show_un(10, 30)
            show_pwd(10, 260)


            # Render the current text.
            txt_surface1 = font.render(text1, True, color1)
            txt_surface2 = font.render(text2, True, color2)

            # Resize the box if the text is too long.
            width1 = max(200, txt_surface1.get_width() + 10)
            width2 = max(200, txt_surface2.get_width() + 10)

            input_box1.w = width1
            input_box2.w = width2


            # Blit the text.
            screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
            screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))

            # Blit the input_box rect.
            pg.draw.rect(screen, color1, input_box1, 2)
            pg.draw.rect(screen, color2, input_box2, 2)

            backbutton.listen(pg.event.get())
            backbutton.draw()
            pg.display.update()
            pg.display.flip()
            clock.tick(30)


    if __name__ == '__main__':
        pg.init()
        main()
        pg.quit()
con.close()