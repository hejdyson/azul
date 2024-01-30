import pygame
import frontend


pygame.init()

# create display window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AZUL ONLINE')

# set up clock
clock = pygame.time.Clock()
fps = 60

# set up font
font = pygame.font.SysFont('calibri', 27, True)




# MAIN GAME LOOP
# drawing stuff and handling events (key presses)
run = True
while run:
    # set up background color
    screen.fill((219, 235, 234))
    # THERE MUST BE ALWAYS TWO PARTS IN THE MAIN PYGAME LOOP
        # DRAWING OF STUFF ON SCREEN and
        # HANDLING USER INPUTS


    # DRAWING ---------------------------------------------------------------------->
    
    # INITIALIZING EVERY NEW ROUND
    frontend.new_round_init(font, screen, SCREEN_WIDTH)

    # drawing everything for player apart from right table
    frontend.draw_bg_lines_info_stones_left(screen, font)

    # drawing points on the right side and after round end
    frontend.draw_points_right_end_round(font, screen, SCREEN_WIDTH)

    # draw stones on underlying and undelrying and handles end of round drawing + its text
    frontend.draw_underlyings_and_stones(font, screen, SCREEN_WIDTH)

    
    # HANDLING OF PLAYER INPUTS -------------------------------------------------->

    # event handler
    for event in pygame.event.get():

    # quit game
        if event.type == pygame.QUIT:
            run = False

        # *** CLICK ***
        if event.type == pygame.MOUSEBUTTONDOWN:
            frontend.click_function(event)

    # Draw the game screen
    pygame.display.update()

    # Limit the FPS by sleeping for the remainder of the frame time
    clock.tick(fps)


pygame.quit()
