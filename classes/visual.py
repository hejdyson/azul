import pygame


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')


# game loop
run = True
while run:
    # event handler
    for event in pygame.event.get():
    # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()