import pygame
import wordsearch
def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('wordgames')

    opening = 'LOADING IN...'
    font = pygame.font.Font('freesansbold.ttf', 64)

    def show_main(x, y):
        opening = font.render('LOADING IN...', True, (255, 255, 255))
        screen.blit(opening, (x, y))

    clock = pygame.time.Clock()
    timer = 5  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).

    running = True

    while running:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        timer -= dt
        if timer <= 0:
            l = []
            wordsearch.main()

        txt = font.render(str(round(timer, 0)), True, (255, 255, 255))
        screen.blit(txt, (310, 350))

        dt = clock.tick(30) / 1000
        show_main(200, 250)

        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()