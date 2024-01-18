import pygame
import button

# create display window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Stone Demo')

# load line images
square_img1 = pygame.image.load('square.png').convert_alpha()
square_img2 = pygame.image.load('square2.png').convert_alpha()
square_img3 = pygame.image.load('square3.png').convert_alpha()
square_img4 = pygame.image.load('square4.png').convert_alpha()
square_img5 = pygame.image.load('square5.png').convert_alpha()
table_right = pygame.image.load('table_right.png').convert_alpha()

# load line hover images
square_img1_hover = pygame.image.load('square_hover.png').convert_alpha()
square_img2_hover = pygame.image.load('square2_hover.png').convert_alpha()
square_img3_hover = pygame.image.load('square3_hover.png').convert_alpha()
square_img4_hover = pygame.image.load('square4_hover.png').convert_alpha()
square_img5_hover = pygame.image.load('square5_hover.png').convert_alpha()

# load underlying images
underlying_img = pygame.image.load('underlying.png').convert_alpha()
middle_underlying_img = pygame.image.load('underlying_middle.png').convert_alpha()

# load underlying hover images
underlying_img_hover = pygame.image.load('underlying_hover.png').convert_alpha()
middle_underlying_img_hover = pygame.image.load('underlying_middle_hover.png').convert_alpha()

# load stone images
blue_stone_img = pygame.image.load('stone_blue.png').convert_alpha()
red_stone_img = pygame.image.load('stone_red.png').convert_alpha()





# just test image
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

    x_stone = x - 4
    y_stone = y + 5
    move_x = 40

    # coordinates for positioning stones on lines
    stone_pos_list_line1 = [(x_stone, y_stone)]
    stone_pos_list_line2 = [(x_stone - move_x * 1, y_stone + diff_line * 1),
                            (x_stone, y_stone + diff_line * 1)]
    stone_pos_list_line3 = [(x_stone - move_x * 2, y_stone + diff_line * 2),
                            (x_stone - move_x * 1, y_stone + diff_line * 2),
                            (x_stone, y_stone + diff_line * 2)]
    stone_pos_list_line4 = [(x_stone - move_x * 3, y_stone + diff_line * 3), 
                            (x_stone - move_x * 2, y_stone + diff_line * 3),
                            (x_stone - move_x * 1, y_stone + diff_line * 3),
                            (x_stone, y_stone + diff_line * 3)]
    stone_pos_list_line5 = [(x_stone - move_x * 4, y_stone + diff_line * 4),
                            (x_stone - move_x * 3, y_stone + diff_line * 4), 
                            (x_stone - move_x * 2, y_stone + diff_line * 4),
                            (x_stone - move_x * 1, y_stone + diff_line * 4),
                            (x_stone, y_stone + diff_line * 4)]

    # create button instance
    square_button = button.Line(player_index, stone_pos_list_line1, 'line 1', x, y, square_img1, square_img1_hover, scale, scale)
    square2_button = button.Line(player_index, stone_pos_list_line2, 'line 2', x, y + diff_line, square_img2, square_img2_hover, scale, scale)
    square3_button = button.Line(player_index, stone_pos_list_line3, 'line 3', x, y + diff_line * 2, square_img3, square_img3_hover, scale, scale)
    square4_button = button.Line(player_index, stone_pos_list_line4, 'line 4', x, y + diff_line * 3, square_img4, square_img4_hover, scale, scale)
    square5_button = button.Line(player_index, stone_pos_list_line5, 'line 5', x, y + diff_line * 4, square_img5, square_img5_hover, scale, scale)
    table_right_label = button.Line(player_index, 'stone pos here', 'table right', x + diff_tables, y, table_right, table_right, scale, scale)

    player_table = [square_button, square2_button, square3_button, square4_button, square5_button, table_right_label]

    return player_table


# create one underlying
def create_underlying(player_index, pos, stone_pos):
    x = pos[0]
    y =  pos[1]
    scale = 0.20
    underlying_button = button.Underlying(player_index, stone_pos, 'underlying', x, y, underlying_img, underlying_img_hover, scale, scale)

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
            # same coordinates logit as in normal underlying, but also Bool to track if stone is placed there or not. It's dynamic underlying
            middle_stone_pos = [(middle_pos[0] - 42 * (j + 1) + diff, middle_pos[1] + 5 + i * 42), False]
            middle_stone_pos_list.append(middle_stone_pos)
    middle_underlying_button = button.Underlying('middle u index', middle_stone_pos_list, 'middle underlying', middle_pos[0], middle_pos[1], middle_underlying_img, middle_underlying_img_hover, 0.2, 0.2)
    underlyings_list.append(middle_underlying_button)

    return underlyings_list


def get_off_screen(stone):
    stone.x = 2000
    stone.y = 2000
    print(stone.x, stone.y)




# crating all tables
# 4 - number of players
list_of_tables = create_board(4)

# creating all underlyings
list_of_underlyings = create_underlyings(4)


# MOVE X = 40
# COORDINATES LINE 3, PLAYER 4
blue_stone = button.Stone('None', 'not needed', 'blue_stone', 146, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone2 = button.Stone('None', 'not needed', 'blue_stone2', 186, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone3 = button.Stone('None', 'not needed', 'blue_stone3', 226, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone4 = button.Stone('None', 'not needed', 'blue_stone4', 356, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)

blue_stone5 = button.Stone('None', 'not needed', 'blue_stone5', 503, 435, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone6 = button.Stone('None', 'not needed', 'blue_stone6', 540, 435, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone7 = button.Stone('None', 'not needed', 'blue_stone7', 503, 472, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone8 = button.Stone('None', 'not needed', 'blue_stone8', 946, 535, blue_stone_img, blue_stone_img, 0.2, 0.2)



# button loop test stone on underlying WORKS
for i in range(4):
    x = list_of_underlyings[1].stone_pos[i][0]
    y = list_of_underlyings[1].stone_pos[i][1]
    red_stone = button.Stone('None', 'not needed', 'red_stone' + str(i), x, y, red_stone_img, red_stone_img, 0.2, 0.2)
    list_of_underlyings[1].stones.append(red_stone)




# blue button just for testing
blue_button = button.Stone('blue test player index', 'test stone pos', 'blue test', 300, 200, blue_img, blue_img, 0.7, 0.7)

screen.fill((202, 228, 241))



# main game loop
run = True
while run:



    # print(blue_stone8.x, blue_stone8.y)

    # handle drawing of tables
    for table in list_of_tables:
        for butt in table:
            # print('screen', butt.draw(screen))
            if butt.draw(screen):
                print('clicked true')
                print(butt.name)
                print(butt.player_index)
                print(butt.stone_pos)




    # handle drawing underlyings
    for underlying in list_of_underlyings:
        if underlying.draw(screen):
            print(underlying.player_index)
            print(underlying.name)
            print(underlying.stone_pos)
        for i in range(len(underlying.stones)):
            underlying.stones[i].draw(screen)
        


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
    
    blue_stone8.draw(screen)
        # print(blue_stone8.name)



    # test button after press changes background
    if blue_button.draw(screen):
        print('blue')
        screen.fill((0, 228, 241))


    # event handler
    for event in pygame.event.get():
    # quit game
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if blue_stone8.rect.collidepoint(event.pos):
        #         print('collideeee')
        #         blue_stone8.x += 10
        #         blue_stone8.y += 10

        if event.type == pygame.MOUSEBUTTONDOWN:
            for stone in list_of_underlyings[1].stones:
                if stone.rect.collidepoint(event.pos):
                    print('collideeee')
                    stone.x += 10
                    stone.y += 10
        

    pygame.display.update()

pygame.quit()
