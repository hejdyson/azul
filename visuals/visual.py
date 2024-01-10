import pygame
import button

# create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button images
square_img1 = pygame.image.load('square.png').convert_alpha()
square_img2 = pygame.image.load('square2.png').convert_alpha()
square_img3 = pygame.image.load('square3.png').convert_alpha()
square_img4 = pygame.image.load('square4.png').convert_alpha()
square_img5 = pygame.image.load('square5.png').convert_alpha()

blue_img = pygame.image.load('blue.png').convert_alpha()

# button positions
x = 100
y = 0
diff = 64
scale = 0.30

# create button instance
square_button = button.Button(x, y, square_img1, scale, scale)
square2_button = button.Button(x, y + diff, square_img2, scale, scale)
square3_button = button.Button(x, y + diff * 2, square_img3, scale, scale)
square4_button = button.Button(x, y + diff * 3, square_img4, scale, scale)
square5_button = button.Button(x, y + diff * 4, square_img5, scale, scale)



blue_button = button.Button(300, 200, blue_img, 0.7, 0.7)


# game loop
run = True
while run:

    screen.fill((202, 228, 241))

    if square_button.draw(screen):
        print('square')
    if square2_button.draw(screen):
        print('square2')
    if square3_button.draw(screen):
        print('square3')
    if square4_button.draw(screen):
        print('square4')
    if square5_button.draw(screen):
        print('square5')

    
    if blue_button.draw(screen):
        print('blue')

    # event handler
    for event in pygame.event.get():
    # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()