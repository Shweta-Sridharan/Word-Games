import pygame, sys
import mysql.connector
import pygame_widgets as pw
pygame.init()
con = mysql.connector.connect(host='localhost', user='root', passwd='Ananya@o104', database='mysql')
c2 = mysql.connector.connect(host='localhost', user='root', passwd='Ananya@o104', database='mysql')
import homepage
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('compare_your_score_page')
mycursor = con.cursor(buffered=True)
cursor = c2.cursor(buffered=True)
exitbutton= pw.Button(screen, 40, 530, 140, 35, text='Exit',fontSize=26, margin=50,inactiveColour=(100, 100, 100),pressedColour=(255, 255, 255), radius=2,onClick=lambda:pygame.quit())
homebutton = pw.Button(screen, 600, 530, 140, 35, text='Home', fontSize=26, margin=50,
                               inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                               onClick=lambda: homepage.buttonmain())


def show_main(x, y):
    opening = font.render('Score chart', True, (255, 255, 255))
    screen.blit(opening, (x, y))
def main():

        def show_scores(x, y):
            sql2 = "select username from user_accounts order by userscore desc"
            sql1 = "select userscore from user_accounts order by userscore desc"
            mycursor.execute(sql1)
            cursor.execute(sql2)
            s = True
            while s:
                r = mycursor.fetchone()
                j = cursor.fetchone()
                try:
                    k = str(j[0]) + ":" + str(r[0])
                    print(k)
                    opening = font.render(k, True, (255, 255, 255))
                    screen.blit(opening, (x, y))
                    homebutton.listen(pygame.event.get()) 
                    exitbutton.listen(pygame.event.get())
                    show_main(300, 50)
                    homebutton.draw()
                    exitbutton.draw()
                    pygame.time.delay(1000)
                    pygame.display.update()
                    screen.fill((0, 0, 0))
                except:
                    s = None
        def displ():
            pygame.init()
            pygame.mixer.init()
            clock = pygame.time.Clock()
            screen = pygame.display.set_mode((800, 600))
            font = pygame.font.Font('freesansbold.ttf', 34)
            running = True
            if con.is_connected():
                while running:
                    screen.fill((0, 0, 0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    show_main(300, 50)
                    show_scores(300, 350)
                    homebutton.listen(pygame.event.get())
                    exitbutton.listen(pygame.event.get())
                    homebutton.draw()
                    exitbutton.draw()
                    pygame.display.update()
                con.close()
            else:
                print('Connection not established')
        displ()
if __name__ == '__main__':
    main()
    pygame.quit()
