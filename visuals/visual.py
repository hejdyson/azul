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

underlying_img = pygame.image.load('underlying.png').convert_alpha()

middle_underlying_img = pygame.image.load('underlying_middle.png').convert_alpha()


blue_stone_img = pygame.image.load('stone_blue.png').convert_alpha()


# test hover line 3
square_img1_hover = pygame.image.load('square_hover.png').convert_alpha()
square_img2_hover = pygame.image.load('square2_hover.png').convert_alpha()
square_img3_hover = pygame.image.load('square3_hover.png').convert_alpha()
square_img4_hover = pygame.image.load('square4_hover.png').convert_alpha()
square_img5_hover = pygame.image.load('square5_hover.png').convert_alpha()


blue_img = pygame.image.load('blue.png').convert_alpha()


# TODO create same list of coordinates for stones for each line

# creating sigle player table
def create_table(player_index, pos):
    # PLAYER
    # button positions
    x = pos[0]
    y =  pos[1]
    scale = 0.20
    diff_line = 200 * scale
    diff_tables = scale * 1000 + 10

    # create button instance
    square_button = button.Button(player_index, 'stone pos here', 'line 1', x, y, square_img1, square_img1_hover, scale, scale)
    square2_button = button.Button(player_index, 'stone pos here', 'line 2', x, y + diff_line, square_img2, square_img2_hover, scale, scale)
    square3_button = button.Button(player_index, 'stone pos here', 'line 3', x, y + diff_line * 2, square_img3, square_img3_hover, scale, scale)
    square4_button = button.Button(player_index, 'stone pos here', 'line 4', x, y + diff_line * 3, square_img4, square_img4_hover, scale, scale)
    square5_button = button.Button(player_index, 'stone pos here', 'line 5', x, y + diff_line * 4, square_img5, square_img5_hover, scale, scale)
    table_right_label = button.Button(player_index, 'stone pos here', 'table right', x + diff_tables, y, table_right, table_right, scale, scale)

    player_table = [square_button, square2_button, square3_button, square4_button, square5_button, table_right_label]

    return player_table


# create one underlying
def create_underlying(player_index, pos, stone_pos):
    x = pos[0]
    y =  pos[1]
    scale = 0.20
    underlying_button = button.Button(player_index, 'underlying', stone_pos, x, y, underlying_img, underlying_img, scale, scale)

    return underlying_button
    

# creating whole board -> all tables for all players
def create_board(num_players):
    table_pos_list = [(230, 450), (1030 , 450), (1030, 50), (230, 50)]
    tables_list = []
    for i in range(num_players):
        table = create_table('Player' + str(i), table_pos_list[i])
        tables_list.append(table)
    
    return tables_list


def create_underlyings(num_players):
    underlying_pos_list2 = [(645, 460), (825, 368), (745, 180), (600, 180), (520, 320)]
    underlying_pos_list3 = [(545, 430), (680, 460), (825, 390), (825, 278), (745, 180), (600, 180), (520, 320)]
    underlying_pos_list4 = [(545, 430), (645, 460), (745, 460), (825, 368), (825, 278), (745, 180), (645, 180), (545, 210), (520, 320)]

    

    # 503, 435            pos[i][0] - 42, pos[i][1] + 5
    # 540, 435            pos[i][0] - 5, pos[i][1] + 5
    # 503, 472            pos[i][0] - 42, pos[i][1] + 42   
    # 540, 472            pos[i][0] - 5, pos[i][1] + 42 


    underlyings_list = []
    # for i in range(num_players + 3 + (num_players - 2) * 1 + 1):
    if num_players == 2:
        for i in range(5):
            stone_pos = [(underlying_pos_list2[i][0] - 42, underlying_pos_list2[i][1] + 5), 
                         (underlying_pos_list2[i][0] - 5, underlying_pos_list2[i][1] + 5),
                         (underlying_pos_list2[i][0] - 42, underlying_pos_list2[i][1] + 42),
                         (underlying_pos_list2[i][0] - 5, underlying_pos_list2[i][1] + 42)]
            underlying = create_underlying('Underlying' + str(i), underlying_pos_list2[i], stone_pos)
            underlyings_list.append(underlying)
    if num_players == 3:
        for i in range(7):
            stone_pos = [(underlying_pos_list3[i][0] - 42, underlying_pos_list3[i][1] + 5), 
                         (underlying_pos_list3[i][0] - 5, underlying_pos_list3[i][1] + 5),
                         (underlying_pos_list3[i][0] - 42, underlying_pos_list3[i][1] + 42),
                         (underlying_pos_list3[i][0] - 5, underlying_pos_list3[i][1] + 42)]
            underlying = create_underlying('Underlying' + str(i), underlying_pos_list3[i], stone_pos)
            underlyings_list.append(underlying)
    if num_players == 4:
        for i in range(9):
            stone_pos = [(underlying_pos_list4[i][0] - 42, underlying_pos_list4[i][1] + 5), 
                         (underlying_pos_list4[i][0] - 5, underlying_pos_list4[i][1] + 5),
                         (underlying_pos_list4[i][0] - 42, underlying_pos_list4[i][1] + 42),
                         (underlying_pos_list4[i][0] - 5, underlying_pos_list4[i][1] + 42)]
            underlying = create_underlying('Underlying' + str(i), underlying_pos_list4[i], stone_pos)
            underlyings_list.append(underlying)
    
    # add middle underlying
    middle_pos = (720, 280)
    middle_stone_pos_list = []
    diff = 0
    for i in range(4):
        for j in range(4):
            if j > 0:
                diff = 5
            middle_stone_pos = (middle_pos[0] - 42 * (j + 1) + diff, middle_pos[1] + 5 + i * 42)
            middle_stone_pos_list.append(middle_stone_pos)
    middle_underlying_button = button.Button('middle u index', 'middle underlying', middle_stone_pos_list, middle_pos[0], middle_pos[1], middle_underlying_img, middle_underlying_img, 0.2, 0.2)
    underlyings_list.append(middle_underlying_button)

    return underlyings_list



# crating all tables
# 4 - number of players
list_of_tables = create_board(4)

# creating all underlyings
list_of_underlyings = create_underlyings(4)



# COORDINATES LINE 3, PLAYER 4
blue_stone = button.Button('None', 'not needed', 'blue_stone', 146, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone2 = button.Button('None', 'not needed', 'blue_stone2', 186, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone3 = button.Button('None', 'not needed', 'blue_stone3', 226, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone4 = button.Button('None', 'not needed', 'blue_stone4', 356, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)

blue_stone5 = button.Button('None', 'not needed', 'blue_stone5', 503, 435, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone6 = button.Button('None', 'not needed', 'blue_stone6', 540, 435, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone7 = button.Button('None', 'not needed', 'blue_stone7', 503, 472, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone8 = button.Button('None', 'not needed', 'blue_stone8', 540, 472, blue_stone_img, blue_stone_img, 0.2, 0.2)



# blue button just for testing
blue_button = button.Button('blue test player index', 'blue test', 'test stone pos', 300, 200, blue_img, blue_img, 0.7, 0.7)

screen.fill((202, 228, 241))


# main game loop
run = True
while run:

    # handle drawing of tables
    for table in list_of_tables:
        for butt in table:
            # print('screen', butt.draw(screen))
            if butt.draw(screen):
                print('clicked true')
                print(butt.player_index)
                print(butt.name)


    # handle drawing underlyings
    for underlying in list_of_underlyings:
        if underlying.draw(screen):
            print(underlying.player_index)
            print(underlying.name)
            print(underlying.stone_pos)
        


    # blue stones testing
    if blue_stone.draw(screen):
        print(blue_stone.name)
    if blue_stone2.draw(screen):
        print(blue_stone2.name)
    if blue_stone3.draw(screen):
        print(blue_stone3.name)
    if blue_stone4.draw(screen):
        print(blue_stone4.name)
    if blue_stone5.draw(screen):
        print(blue_stone5.name)
    if blue_stone6.draw(screen):
        print(blue_stone6.name)
    if blue_stone7.draw(screen):
        print(blue_stone7.name)
    if blue_stone8.draw(screen):
        print(blue_stone8.name)


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
