import pygame as pg
import os
import homepage
import time
import mysql.connector
import register
import scorecomparepage

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()
screen = pg.display.set_mode((800, 640), pg.RESIZABLE)
COLOR_INACTIVE = pg.Color(226, 226, 226)
COLOR_ACTIVE = pg.Color(74, 83, 107)
BFONT = pg.font.SysFont('Corbel', 15, bold=True)
font = pg.font.SysFont('Corbel', 32, bold=True)
FONT = pg.font.SysFont('Corbel', 25, bold=True)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text

        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:

            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode



                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen,user):
        if user:

            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        else:
            screen.blit(FONT.render('*'*len(self.text),True,COLOR_ACTIVE), (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)


def textobjects(text, font):
    textsurface = BFONT.render(text, True, (0, 0, 0))
    return textsurface, textsurface.get_rect()


def button(msg, x, y, w, h):
    pg.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    textsurf, textrect = textobjects(msg, font)
    textrect.center = ((x + (w // 2)), (y + (h // 2)))
    screen.blit(textsurf, textrect)




def validatePwd(username, pwd):
    def showError(message):

        start_time = time.time()
        levelfont = pg.font.SysFont('Corbel', 25)
        text = levelfont.render(message, True, (255, 0, 0))
        show = True
        while show:
            if time.time() - start_time < 2:
                screen.blit(text, (200, 600))
            else:
                show = False
            pg.display.update()

    con = mysql.connector.connect(host='localhost', user='root', passwd='Ananya@o104', database='mysql')
    if con.is_connected():
        try:
            cur = con.cursor()
            cur.execute('select userpwd from user_accounts where username = "{}"'.format(username))
            result = cur.fetchone()
            print(result)
            if result:
                if pwd == result[0]:
                    con.close()
                    return True
                else:
                    print('oops')
                    showError('Incorrect Username or Password. Try Again.')
            else:
                print('oops1')
                showError('Incorrect Username or password. Try Again.')
        except mysql.connector.Error:
            showError('Database Issue; Please Try Later')
        finally:
            con.close()
    else:
        showError('Error Connecting to Database; Please Try Later')
    return False


def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(350, 250, 140, 32)
    input_box2 = InputBox(350, 350, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for box in input_boxes:
            box.update()

        screen.fill((0, 0, 0))

        input_box1.draw(screen,True)
        input_box2.draw(screen, False)

        screen.blit(font.render(" LOGIN TO SEE YOUR SCORE AMONGST THE OTHERS' ", True, (255, 255, 255)), (10, 50))
        screen.blit(font.render(' _________________________________________________', True, (255, 255, 255)), (10, 65))



        screen.blit(FONT.render('Username:', True, (255, 255, 255)), (220, 250))
        screen.blit(FONT.render('Password:', True, (255, 255, 255)), (220, 350))
        screen.blit(FONT.render('Register', True, (255, 255, 255)), (650, 540))


        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        button('Login', 390, 450, 100, 32)
        button('Register!', 650, 540, 100, 32)
        button('Back', 70, 540, 100, 32)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                pg.quit()
            for box in input_boxes:
                box.handle_event(event)

        if 490 > mouse[0] > 390 and 482 > mouse[1] > 450 and click[0] == 1 and not done:
            username, pwd = input_boxes[0].text, input_boxes[1].text
            if username and pwd and validatePwd(username, pwd):
                done = True
                scorecomparepage.main()

        if 370 > mouse[0] > 270 and 572 > mouse[1] > 540 and click[0] == 1 and not done:
            done = True
            register.main()

        if 670 > mouse[0] > 520 and 572 > mouse[1] > 540 and click[0] == 1 and not done:
            done = True
            homepage.buttonmain()

        try:
            pg.display.update()
        except:
            pass
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()