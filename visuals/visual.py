import pygame
import button

# create display window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button images
square_img1 = pygame.image.load('square.png').convert_alpha()
square_img2 = pygame.image.load('square2.png').convert_alpha()
square_img3 = pygame.image.load('square3.png').convert_alpha()
square_img4 = pygame.image.load('square4.png').convert_alpha()
square_img5 = pygame.image.load('square5.png').convert_alpha()
table_right = pygame.image.load('table_right.png').convert_alpha()

blue_img = pygame.image.load('blue.png').convert_alpha()


underlying_img = pygame.image.load('underlying.png').convert_alpha()

blue_stone_img = pygame.image.load('stone_blue.png').convert_alpha()






# Creating sigle player table
def create_table(player_index, pos):
    # PLAYER
    # button positions
    x = pos[0]
    y =  pos[1]
    scale = 0.20
    diff_line = 200 * scale
    diff_tables = scale * 1000 + 10

    # create button instance
    square_button = button.Button(player_index, 'line 1', x, y, square_img1, scale, scale)
    square2_button = button.Button(player_index, 'line 2', x, y + diff_line, square_img2, scale, scale)
    square3_button = button.Button(player_index, 'line 3', x, y + diff_line * 2, square_img3, scale, scale)
    square4_button = button.Button(player_index, 'line 4', x, y + diff_line * 3, square_img4, scale, scale)
    square5_button = button.Button(player_index, 'line 5', x, y + diff_line * 4, square_img5, scale, scale)
    table_right_label = button.Button(player_index, 'table right', x + diff_tables, y, table_right, scale, scale)

    player_table = [square_button, square2_button, square3_button, square4_button, square5_button, table_right_label]

    return player_table


def create_underlying(player_index, pos):
    x = pos[0]
    y =  pos[1]
    scale = 0.20
    underlying_button = button.Button(player_index, 'underlying', x, y, underlying_img, scale, scale)

    return underlying_button
    


# creating all tables for all players
def create_board(num_players):
    table_pos_list = [(230, 450), (1030 , 450), (1030, 50), ((230, 50))]
    tables_list = []
    for i in range(num_players):
        table = create_table('Player' + str(i), table_pos_list[i])
        tables_list.append(table)
    
    return tables_list


def create_underlyings():
    underlying_pos_list2 = [(533, 152), (489, 345), (675, 437), (802, 300), (735, 144)]
    underlying_pos_list3 = [(550)]
    underlying_pos_list4 = [(550)]

    underlyings_list = []
    # for i in range(num_players + 3 + (num_players - 2) * 1 + 1):
    for i in range(5):
        underlying = create_underlying('Underlying' + str(i), underlying_pos_list2[i])
        underlyings_list.append(underlying)

    return underlyings_list



# crating all tables
# 4 - number of players
list_of_tables = create_board(2)

# creating all underlyings
list_of_underlyings = create_underlyings()



# COORDINATES LINE 3, PLAYER 4
blue_stone = button.Button('None', 'blue_stone', 146, 135, blue_stone_img, 0.2, 0.2)
blue_stone2 = button.Button('None', 'blue_stone2', 186, 135, blue_stone_img, 0.2, 0.2)
blue_stone3 = button.Button('None', 'blue_stone3', 356, 135, blue_stone_img, 0.2, 0.2)




# blue button just for testing
blue_button = button.Button('blue test player index', 'blue test', 300, 200, blue_img, 0.7, 0.7)

screen.fill((202, 228, 241))

# game loop
run = True
while run:

    for table in list_of_tables:
        for butt in table:
            if butt.draw(screen):
                print(butt.player_index)
                print(butt.name)

    for underlying in list_of_underlyings:
        if underlying.draw(screen):
            print(underlying.player_index)
            print(underlying.name)


    # if square_button.draw(screen):
    #     print('square')
    # if square2_button.draw(screen):
    #     print('square2')
    # if square3_button.draw(screen):
    #     print('square3')
    # if square4_button.draw(screen):
    #     print('square4')
    # if square5_button.draw(screen):
    #     print('square5')
    # if table_right_label.draw(screen):
    #     print('table right')
                

    
    # underlying tests
        



    # blue stones testing
    if blue_stone.draw(screen):
        print(blue_stone.name)
    if blue_stone2.draw(screen):
        print(blue_stone2.name)
    if blue_stone3.draw(screen):
        print(blue_stone3.name)




    # test button after press changes background
    if blue_button.draw(screen):
        print('blue')
        screen.fill((0, 228, 241))



    # event handler
    for event in pygame.event.get():
    # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()