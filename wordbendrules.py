import pygame, sys
import wordbend
import pygame_widgets as pw
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('WORD BEND RULES')

def main():
    skipbutton = pw.Button(screen, 550, 530, 140, 35, text='Play game', fontSize=26, margin=50,
                           inactiveColour=(100, 100, 100), pressedColour=(255, 255, 255), radius=2,
                           onClick=lambda: wordbend.main())
    
    
    font = pygame.font.Font('freesansbold.ttf', 22)
    def line1(x, y):
        word= font.render('WORD BEND!!', True, (255, 255, 255))
        screen.blit(word, (x, y))
    
    def line2(x, y):
        word_val = font.render('1.LOOK AT THE WORD DISPLAYED ON THE SCREEN. ', True, (255, 255, 255))
        screen.blit(word_val, (x, y))
    
    def line3(x, y):
        line_val = font.render('2.TYPE IN A NEW WORD BY CHANGING EXACTLY ONE LETTER OF IT.', True, (255, 255, 255))
        screen.blit(line_val, (x, y))
    
    def line4(x,y):
        liness_val=font.render('3.REMEMBER TO ENTER A NEW AND MEANINGFUL WORD EACH TIME.', True, (255, 255, 255))
        screen.blit(liness_val, (x, y))
    
    def line5(x, y):
        lines_val = font.render('4.GO ON AND MAKE AS MANY WORDS AS POSSIBLE IN 1 MINUTE! ', True, (255, 255, 255))
        screen.blit(lines_val, (x, y))
    
    font1 = pygame.font.Font('freesansbold.ttf', 64)
    
    
    
    
    running = True
    while running:
        screen.fill((0, 0, 0))
    
    
    
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    
        line1(310, 30)
        line2(30,180)
        line3(30,220)
        line4(30,260)
        line5(30,300)
        skipbutton.listen(pygame.event.get())
        skipbutton.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()
    pygame.quit()