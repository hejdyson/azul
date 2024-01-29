import pygame
import button
from random import shuffle

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


# load LOGO
logo_img = pygame.image.load('pictures\\azul_logo.png').convert_alpha()
logo_img = pygame.transform.scale(logo_img, (int(0.44 * logo_img.get_width()), (0.44 * logo_img.get_height())))

#load legend
legend_img = pygame.image.load('pictures\\legend.png').convert_alpha()
legend_img = pygame.transform.scale(legend_img, (int(0.38 * legend_img.get_width()), (0.38 * legend_img.get_height())))

# load first player icon
first_player_img = pygame.image.load('pictures\\first_player.png').convert_alpha()
first_player_img = pygame.transform.scale(first_player_img, (int(0.11 * first_player_img.get_width()), (0.11 * first_player_img.get_height())))

# load line images
square_img1 = pygame.image.load('pictures\square.png').convert_alpha()
square_img2 = pygame.image.load('pictures\square2.png').convert_alpha()
square_img3 = pygame.image.load('pictures\square3.png').convert_alpha()
square_img4 = pygame.image.load('pictures\square4.png').convert_alpha()
square_img5 = pygame.image.load('pictures\square5.png').convert_alpha()
table_right_img = pygame.image.load('pictures\\table_right.png').convert_alpha()
minus_points_img = pygame.image.load('pictures\minus_points.png').convert_alpha()
# only to create table right without actual button
# table_right_img = pygame.transform.scale(table_right_img, (int(0.2 * table_right_img.get_width()), (0.2 * table_right_img.get_height())))

# load line hover images
square_img1_hover = pygame.image.load('pictures\square_hover.png').convert_alpha()
square_img2_hover = pygame.image.load('pictures\square2_hover.png').convert_alpha()
square_img3_hover = pygame.image.load('pictures\square3_hover.png').convert_alpha()
square_img4_hover = pygame.image.load('pictures\square4_hover.png').convert_alpha()
square_img5_hover = pygame.image.load('pictures\square5_hover.png').convert_alpha()

# load player background image
player_background_img = pygame.image.load('pictures\player_background.png').convert_alpha()
player_background_img = pygame.transform.scale(player_background_img, (int(0.2 * player_background_img.get_width()), (0.2 * player_background_img.get_height())))

# load underlying images
underlying_img = pygame.image.load('pictures\\underlying.png').convert_alpha()
middle_underlying_img = pygame.image.load('pictures\\underlying_middle.png').convert_alpha()

# load underlying hover images
underlying_img_hover = pygame.image.load('pictures\\underlying_hover.png').convert_alpha()
middle_underlying_img_hover = pygame.image.load('pictures\\underlying_middle_hover.png').convert_alpha()

# load stone images
blue_stone_img = pygame.image.load('pictures\stone_blue.png').convert_alpha()        # VALUE 1
yellow_stone_img = pygame.image.load('pictures\stone_yellow.png').convert_alpha()    # VALUE 2
black_stone_img = pygame.image.load('pictures\stone_black.png').convert_alpha()      # VALUE 3
green_stone_img = pygame.image.load('pictures\stone_green.png').convert_alpha()      # VALUE 4
red_stone_img = pygame.image.load('pictures\stone_red.png').convert_alpha()          # VALUE 5
stone_minus_img = pygame.image.load('pictures\stone_minus.png').convert_alpha()      # VALUE -1





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
    
    stone_pos_minus_points = [(x + 207 - move_x*6 + 6, y + 209), (x + 207 - move_x*5 + 5, y + 209), (x + 207 - move_x*4 + 4, y + 209), 
                              (x + 206 - move_x*3 + 3, y + 209), (x + 207 - move_x*2 + 2, y + 209),
                              (x + 207 - move_x*1 + 1, y + 209), (x + 207, y + 209)]

    stone_pos_table_right = [((1, False, (x_stone + 50, y_stone)), (2, False, (x_stone + 50 + 1* move_x, y_stone)), (3, False, (x_stone + 50 + 2* move_x, y_stone)), (4, False, (x_stone + 50 + 3* move_x, y_stone)), (5, False, (x_stone + 50 + 4* move_x, y_stone))),
                             ((5, False, (x_stone + 50, y_stone + move_x)), (1, False, (x_stone + 50 + 1* move_x, y_stone + move_x)), (2, False, (x_stone + 50 + 2* move_x, y_stone + move_x)), (3, False, (x_stone + 50 + 3* move_x, y_stone + move_x)), (4, False, (x_stone + 50 + 4 * move_x, y_stone + move_x))),
                             ((4, False, (x_stone + 50, y_stone + move_x*2)), (5, False, (x_stone + 50 + 1* move_x, y_stone + move_x*2)), (1, False, (x_stone + 50 + 2* move_x, y_stone + move_x*2)), (2, False, (x_stone + 50 + 3* move_x, y_stone + move_x*2)), (3, False, (x_stone + 50 + 4 * move_x, y_stone + move_x*2))),
                             ((3, False, (x_stone + 50, y_stone + move_x*3)), (4, False, (x_stone + 50 + 1* move_x, y_stone + move_x*3)), (5, False, (x_stone + 50 + 2* move_x, y_stone + move_x*3)), (1, False, (x_stone + 50 + 3* move_x, y_stone + move_x*3)), (2, False, (x_stone + 50 + 4 * move_x, y_stone + move_x*3))),
                             ((2, False, (x_stone + 50, y_stone + move_x*4)), (3, False, (x_stone + 50 + 1* move_x, y_stone + move_x*4)), (4, False, (x_stone + 50 + 2* move_x, y_stone + move_x*4)), (5, False, (x_stone + 50 + 3* move_x, y_stone + move_x*4)), (1, False, (x_stone + 50 + 4 * move_x, y_stone + move_x*4))),
                             ]

    # create button instance
    square_button = button.Line(player_index, stone_pos_list_line1, 'line', 1, x, y, square_img1, square_img1_hover, scale, scale)
    square2_button = button.Line(player_index, stone_pos_list_line2, 'line', 2, x, y + diff_line, square_img2, square_img2_hover, scale, scale)
    square3_button = button.Line(player_index, stone_pos_list_line3, 'line', 3, x, y + diff_line * 2, square_img3, square_img3_hover, scale, scale)
    square4_button = button.Line(player_index, stone_pos_list_line4, 'line', 4, x, y + diff_line * 3, square_img4, square_img4_hover, scale, scale)
    square5_button = button.Line(player_index, stone_pos_list_line5, 'line', 5, x, y + diff_line * 4, square_img5, square_img5_hover, scale, scale)
    
    table_right_label = button.Line(player_index, stone_pos_table_right, 'table right', None, x + diff_tables, y, table_right_img, table_right_img, scale, scale)
    minus_points_label = button.Line(player_index, stone_pos_minus_points, 'minus points', 7, x + diff_tables, y + diff_line * 5 + 5, minus_points_img, minus_points_img, scale-0.005, scale-0.005)
    

    player_table = [square_button, square2_button, square3_button, square4_button, square5_button, table_right_label, minus_points_label]

    return player_table


# create one underlying
def create_underlying(player_index, pos, stone_pos):
    x = pos[0]
    y =  pos[1]
    scale = 0.20
    underlying_button = button.Underlying(player_index, stone_pos, 'underlying', x, y, underlying_img, underlying_img_hover, scale, scale)

    return underlying_button
    

# creating whole board -> all tables for all players
# COORDINATES FOR TABLES
def create_board(num_players):
    table_pos_list = [(220, 445), (1060 , 445), (1060, 70), (220, 70)]
    tables_list = []
    for i in range(num_players):
        table = create_table(i, table_pos_list[i])
        tables_list.append(table)
    
    return tables_list


def create_underlyings(num_players):
    underlying_pos_list2 = [(650, 460), (830, 368), (760, 180), (605, 180), (535, 320)]
    underlying_pos_list3 = [(550, 430), (685, 460), (830, 390), (830, 278), (750, 180), (605, 180), (530, 320)]
    underlying_pos_list4 = [(550, 430), (650, 460), (750, 460), (830, 368), (830, 278), (750, 180), (650, 180), (550, 210), (535, 320)]


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
    middle_pos = (725, 280)
    middle_stone_pos_list = []
    # TODO MAYBE ADD MORE PLACES IN THE MIDDLE IN THE FUTURE
    for i in range(4):
        for j in range(4):
            diff = 7
            # print('i', i, 'j', j, 'diff', diff)
            # same coordinates logit as in normal underlying, but also Bool to track if stone is placed there or not. It's dynamic underlying
            middle_stone_pos = [(middle_pos[0] - (37 * j) - diff, middle_pos[1] + diff + i * 37), False]
            middle_stone_pos_list.append(middle_stone_pos)
            # print('middle_stone_pos', middle_stone_pos)
    middle_underlying_button = button.Underlying('middle u index', middle_stone_pos_list, 'middle underlying', middle_pos[0], middle_pos[1], middle_underlying_img, middle_underlying_img_hover, 0.2, 0.2)
    underlyings_list.append(middle_underlying_button)

    return underlyings_list

# drawing right side of table -NOT USED - only when table right os not a BUTTON OBJECT
def draw_table_right(num_players):
    table_right_pos_list = [(230, 450), (1070, 450), (1070, 70), (230, 70)]
    for i in range(num_players):
        screen.blit(table_right_img, table_right_pos_list[i])


# drawing player backgrounds
def draw_player_backgrounds(num_players):
    background_pos_list = [(15, 390), (855 , 390), (855, 15), (15, 15)]
    for i in range(num_players):
        screen.blit(player_background_img, background_pos_list[i])


def draw_player_info(num_players):
    points_pos_list = [(15, 390), (855 , 390), (855, 15), (15, 15)]
    for i in range(num_players):
        # render player name
        name = font.render('Name here', True, (0, 0, 0), (200, 245, 249))
        screen.blit(name, (points_pos_list[i][0] + 15, points_pos_list[i][1] + 13))
        # render points
        points = font.render('Points: ' + '33', True, (0, 0, 0), (200, 245, 249))
        screen.blit(points, (points_pos_list[i][0] + 280, points_pos_list[i][1] + 13))
        # display first player card
        # WILL GO FROM ORDERED PLAYER LIST - first will always be first player
        if i == 0:
            screen.blit(first_player_img, (points_pos_list[i][0] + 15, points_pos_list[i][1] + 46))




def create_bag_of_stones():
    bag_of_tiles = []
    for i in range(5):
        for _ in range(20):
            if i == 0:
                bag_of_tiles.append(1)
            elif i == 1:
                bag_of_tiles.append(2)
            elif i == 2:
                bag_of_tiles.append(3)
            elif i == 3:
                bag_of_tiles.append(4)
            else:
                bag_of_tiles.append(5)  
    shuffle(bag_of_tiles)
    print('bag of tiles', bag_of_tiles)
    return bag_of_tiles
    

# button loop test stone on underlying WORKS
# HERE STONES WILL APPEND ACCORDING TO BAG OF TILES - SAME AS IN BACKEND
# IN GAME THE VALUE WILL COME FROM board.fill_in_underlyings - self.bag_of_tiles.pop()
def add_stones_on_underlyings(bag_of_tiles):
    # bag_of_tiles = create_bag_of_stones()
    #shuffle(bag_of_tiles)
    #print('bag of tiles shuffled', bag_of_tiles)
    counter = 0
    for index, underlying in enumerate(list_of_underlyings):

        # MIDDLE UNDERLYING - add -1
        if index + 1 == len(list_of_underlyings):

            x = underlying.stone_pos[0][0][0]
            y = underlying.stone_pos[0][0][1]
            underlying.stone_pos[0][1] = True
            stone = button.Stone(-1, underlying, 'MINUS_STONE', x, y, stone_minus_img, stone_minus_img, 0.2, 0.2)
            underlying.stones.append(stone)
            
            print(underlying.name)
            print(underlying.stone_pos)
            print(underlying.stones)
        
        else:
            # NORMAL UNDERLYINGS
            for i in range(4):
                value = bag_of_tiles.pop()
                x = underlying.stone_pos[i][0]
                y = underlying.stone_pos[i][1]
                # print('x', x, 'y', y)
                if value == 1:
                    stone = button.Stone(value, underlying, 'blue_stone' + str(counter), x, y, blue_stone_img, blue_stone_img, 0.2, 0.2)
                elif value == 2:
                    stone = button.Stone(value, underlying, 'yellow_stone' + str(counter), x, y, yellow_stone_img, yellow_stone_img, 0.2, 0.2)
                elif value == 3:
                    stone = button.Stone(value, underlying, 'black_stone' + str(counter), x, y, black_stone_img, black_stone_img, 0.2, 0.2)
                elif value == 4:
                    stone = button.Stone(value, underlying, 'green_stone' + str(counter), x, y, green_stone_img, green_stone_img, 0.2, 0.2)
                elif value == 5:
                    stone = button.Stone(value, underlying, 'red_stone' + str(counter), x, y, red_stone_img, red_stone_img, 0.2, 0.2)
                # id of object for unique verification
                # print(id(stone))
                # list of stones on underlying
                underlying.stones.append(stone)
                # counter += 1
    print('len(bag_of_tiles)', len(bag_of_tiles))



# move stones to right after round ends
def move_stones_to_right():
    # for all players
    for player_index in range(NUM_PLAYERS):
        for line in list_of_tables[player_index]:
            print('player_index', player_index)
            # dont loop over minus points and right table now
            if line.name == 'table right' or line.name == 'minus points':
                print('end of lines reached, moving to next player')
                break

            # if line is full
            if len(line.stones) == line.limit:
                print('line:', line.name)
                moving_stone = line.stones[0]
                print('stone taken', moving_stone.value)
                # append to .stones
                list_of_tables[player_index][-2].stones.append(moving_stone)
                # and change stone placement
                moving_stone.placement = list_of_tables[player_index][-2]

                # loop through all lines on right and find same line
                for index, row in enumerate(list_of_tables[player_index][-2].stone_pos):
                    print('index', index + 1, 'line', line.limit)
                    if index + 1 == line.limit:
                        print('HIT     index', index + 1, 'line', line.limit)
                        # loop through row items to find place for stone
                        print('looking for placement')
                        for item in row:
                            print('item value', item[0])
                            # when item found
                            if item[0] == moving_stone.value:
                                print('POSITION FOUND', item[0], '=', moving_stone.value)
                                # change placed status to True - done on backend alreadz - maybe not needed
                                # item[1] = True
                                # assign new coordinates to moving stone
                                moving_stone.x = item[2][0]
                                moving_stone.y = item[2][1]
                                break
                
                # clear line
                line.stones.clear()


# remove stones from inus points after end of round
def clear_minus_points():
    for player_index in range(NUM_PLAYERS):
        list_of_tables[player_index][-1].stones.clear()





# ##############################
# CLICK FUNCTION
def click_function():
    # FIRST - CLICK MUST BE ON STONE ON UNDERLYING -> SEARCH ONLY FOR THOSE CLICKS
    for underlying in bv.list_of_underlyings:
        for stone in underlying.stones:
            # it is possible only at first, then it needst click on line, no other stones can be clicked
            if bv.possible_to_click_on_stones:
                # when clicked stone found
                if stone.rect.collidepoint(event.pos):
                    # if stone clicked is not on line
                    if stone.placement.name == 'line' or stone.placement.name == 'minus points' or stone.placement.name == 'table right':
                        print('stone on line clicked')
                        break
                    if stone.placement == bv.list_of_underlyings[-1] and len(bv.list_of_underlyings[-1].stones) == 1 and bv.list_of_underlyings[-1].stones[0].value == -1:
                        print('clicked on minus - when its the only stone on underlying')
                        break
                    # first disable another stone click - now only line click is accepted - ONLY CLICK SWITCHES THIS TO FALSE
                    bv.possible_to_click_on_stones = False
                    print('bv.possible_to_click_on_stones', bv.possible_to_click_on_stones)
                    # helpful prints
                    print('stone placement, stones, name', stone.placement, stone.placement.stones, stone.placement.name)
                    # loop through all stones on the placement - decide what will go to line and what to the middle
                    bv.to_line = []
                    bv.to_the_middle = []
                    # appending to line same stones
                    for tile in stone.placement.stones:
                        if tile.value == stone.value:
                            bv.to_line.append(tile)
                        # IF TAKEN FIRST FORM THE MIDDLE
                        elif tile.value == -1:
                            bv.to_line.append(tile)
                            # TODO LATER HANDLE
                        # different stones go to middle
                        else:
                            bv.to_the_middle.append(tile)
                    # help print what goes where
                    print('to line goes', bv.to_line)
                    for item in bv.to_line:
                        print(item.name)
                    print('to the middle goes', bv.to_the_middle)
                    for item in bv.to_the_middle:
                        print(item.name)

                    # CLICKED ON MIDDLE UNDERLYING
                    # if clicked on the middle - managing of coordinates
                    # middle remove - to handle removes AFTER line is clicked, not before - end of round management
                    bv.middle_remove = []
                    for item in bv.to_line:
                        # handle of middle coordinates
                        if item.placement == bv.list_of_underlyings[-1]:
                            from_the_middle = True
                            print('taking from the middle')
                            for position in bv.list_of_underlyings[-1].stone_pos:
                                print('position', position)
                                print('position of stone x', item.x, 'y:', item.y)
                                # removing taken stones from the middle
                                if position[0] == (item.x, item.y):
                                    print('occupied middle position to be freed', position)
                                    position[1] = False
                            # handle of middle stones
                            bv.middle_remove.append(item)
                        else:
                            from_the_middle = False

                    # HANDLE ADDING TILES TO MIDDLE
                    # append to the list of stones of middle underlying
                    # happens only when not taking from the middle
                    if not from_the_middle:
                        for tile in bv.to_the_middle:
                            bv.list_of_underlyings[-1].stones.append(tile)
                            tile.placement = bv.list_of_underlyings[-1]
                        # change coordinates of stone to the ones from the middle that are available
                        for tile in bv.to_the_middle:
                            for stone_pos in bv.list_of_underlyings[-1].stone_pos:
                                if stone_pos[1] == False:
                                    tile.x = stone_pos[0][0]
                                    tile.y = stone_pos[0][1]
                                    stone_pos[1] = True
                                    break

                        # and removing stones from .stones of non middle underlying - to track if all empty to end round
                        bv.underlying_to_clear = stone.placement.stones
    

    # SEDOND - CLICK MUST BE ON LINE OF PLAYER WHICH IS ON TURN - for now only player 1
    if not bv.possible_to_click_on_stones:
        for line in bv.list_of_tables[bv.player_index]:
            if line.rect.collidepoint(event.pos):
                # just check if not clicked on minus points or on table right
                if line == bv.list_of_tables[bv.player_index][-1] or line == bv.list_of_tables[bv.player_index][-2]:
                    print('table right or minus points')
                    break

                # condition cannot put stones of different color when line is not empty
                if len(line.stones) != 0 and len(line.stones) != line.limit:
                    # check if line has different stones on it
                    if bv.to_line[-1].value != line.stones[0].value:
                        print('different stones already on line')
                        break
                # NOTE - can place ANY stone on ANY line if line is full - stones will go to MINUS

                # first enable clicking on stone on underlying again
                bv.possible_to_click_on_stones = True
                print('bv.possible_to_click_on_stones', bv.possible_to_click_on_stones)

                # Handling of stone click placement - either on line or to minus points if over the line limit: 1 APPEND 2 CHANGE COORDINATES
                # LINE: append to the line list of stones
                for stone in bv.to_line:
                    if stone.value != -1:
                        line.stones.append(stone)
                        stone.placement = line
                    # if -1 taken
                    else:
                        bv.list_of_tables[bv.player_index][-1].stones.append(stone)
                        stone.placement = bv.list_of_tables[bv.player_index][-1]

                # minus points - if over line limit
                # MINUS_POINTS: append over the limit stones to minus points list of stones
                if len(line.stones) > line.limit:
                    for i in range(len(line.stones) - line.limit):
                        # change stone placement to minus point
                        line.stones[-i-1].placement = bv.list_of_tables[bv.player_index][-1]
                        # append stone to minus point point list (only of there is still place)
                        # TODO HARD TO REACH EDGECASE - ALL LINES FULL AND ALSO MINUS POINTS FULL - STONES WONT GO TO MIDDLE
                        if len(bv.list_of_tables[bv.player_index][-1].stones) < bv.list_of_tables[bv.player_index][-1].limit:
                            bv.list_of_tables[bv.player_index][-1].stones.append(line.stones[-i-1])
                    # remove excessive stones from line.stones
                    for i in range(len(line.stones) - line.limit):
                        line.stones.pop()

                # LINE: change coordiates to the line coordinates
                for i in range(len(line.stones)):
                    line.stones[i].x = line.stone_pos[i][0]
                    line.stones[i].y = line.stone_pos[i][1]

                # MINUS_POINTS: change coordinates to minus points coordinates 
                for i in range(len(bv.list_of_tables[bv.player_index][-1].stones)):
                    bv.list_of_tables[bv.player_index][-1].stones[i].x = bv.list_of_tables[bv.player_index][-1].stone_pos[i][0]
                    bv.list_of_tables[bv.player_index][-1].stones[i].y = bv.list_of_tables[bv.player_index][-1].stone_pos[i][1]

                # after placing tiles to line, clear selected underlying.stones
                if bv.underlying_to_clear is not None:
                    print('clearing underlying')
                    bv.underlying_to_clear.clear()

                for i in range(len(bv.middle_remove)):
                    print('removing from middle')
                    bv.list_of_underlyings[-1].stones.remove(bv.middle_remove[i])

                # player index increment
                bv.player_index += 1
                if bv.player_index == NUM_PLAYERS:
                    bv.player_index = 0
                
        print('middle positions:', bv.list_of_underlyings[-1].stone_pos)


#############################
# DRAWING FUNCTIONS

def new_round_init():    
    # ADDING STONES ON UNDERLYINGS ROUND 1
    if bv.round == 0:
        print('filling underlyings')
        add_stones_on_underlyings(bv.bag_of_tiles)
        bv.round = 1

    # DISPLAY LOGO
    screen.blit(logo_img, (SCREEN_WIDTH / 2 - logo_img.get_width() / 2, -20))
    # DISPLAY LEGEND
    screen.blit(legend_img, (SCREEN_WIDTH / 2 - legend_img.get_width() / 2, 595))

    # EMPTY CHECK
    bv.empty = True
    # check if underlyings empty - next round - also for slower drawing
    for underlying in bv.list_of_underlyings:
        if len(underlying.stones) > 0:
            bv.empty = False

    # ROUND COUNTER TEXT
    if not bv.empty:
        img = font.render('Round: ' + str(bv.round), True, (0, 0, 0), (219, 235, 234))
        screen.blit(img, (SCREEN_WIDTH / 2 - img.get_width() / 2, 120))
    
    # EMPTY HANDLING FUNCTION CALLS
    if bv.empty:
        # move stones to right
        print('all empty - end of round')
        print('moving stones to right')
        move_stones_to_right()

        # clearing minus points
        # TODO SOME DELAY HERE
        print('removing minus points')
        clear_minus_points()

        # add stones on underlzing next rounds
        print('filling underlyings')
        add_stones_on_underlyings(bv.bag_of_tiles)

        # change starting player
        # TODO STARTING PLAYER - WILL BE THE ONE WHO TOOK MIDDLE
        bv.player_index = 0
        bv.round += 1


def draw_bg_lines_info_stones_left():
    # handle drawing of tables
    # draw background
    draw_player_backgrounds(NUM_PLAYERS)
    # drawing lines
    for table in bv.list_of_tables:
        for line in table:
            # print('screen', butt.draw(screen))
            line.draw(screen)

    # draw player info
    draw_player_info(NUM_PLAYERS)

    # drawing stones on the left side and on minus points
    for table in bv.list_of_tables:
        for line in table:    
            # ALWAYS ALSO DRAW STONE THATS ON THE LINE - separately
            if line.name != 'table right':
                for stone in line.stones:
                    stone.draw(screen)
    
    if bv.empty:
        pygame.time.wait(1500)


def draw_points_right_end_round():
    for table in bv.list_of_tables:
        for line in table:    
            if line.name == 'table right':
                if bv.empty:
                    img = font.render('Counting points... ' + 'Player ' + str(line.player_index), True, (0, 0, 0), (219, 235, 234))
                    screen.blit(img, (SCREEN_WIDTH / 2 - img.get_width() / 2, 120))
                    pygame.display.update()
                    pygame.time.wait(2000)
                for stone in line.stones:
                    stone.draw(screen)


def draw_underlyings_and_stones():
    # EMPTY UNDERLYING CHECK - END OF ROUND
    if bv.empty:
        # pause and text change before filling underlyings
        img = font.render('      Filling underlyings...      ', True, (0, 0, 0), (219, 235, 234))
        screen.blit(img, (SCREEN_WIDTH / 2 - img.get_width() / 2, 120))
        pygame.display.update()
        pygame.time.wait(1500)

    # handle drawing underlyings
    for underlying in bv.list_of_underlyings:
        underlying.draw(screen)
        # ALWAYS ALSO DRAW STONES THAT ARE ON UNDERLYING
        for i in range(len(underlying.stones)):
            underlying.stones[i].draw(screen)



NUM_PLAYERS = 2


# ASSIGNING bv OBJECT TO HANLDE GAME UPDATES
# game round
ROUND = 0

# crating all tables
# 4 - number of players
list_of_tables = create_board(NUM_PLAYERS)

# creating all underlyings
list_of_underlyings = create_underlyings(NUM_PLAYERS)

# create bag of tiles
bag_of_tiles = create_bag_of_stones()

# enable click on stone
possible_to_click_on_stones = True

# test looping through list of players
player_index = 0

# create board visual class instance that holds all info displayed on visual board
bv = button.BoardVisual(ROUND, list_of_tables, list_of_underlyings, bag_of_tiles, possible_to_click_on_stones, player_index)


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
    new_round_init()

    # drawing everything for player apart from right table
    draw_bg_lines_info_stones_left()

    # drawing points on the right side and after round end
    draw_points_right_end_round()

    # draw stones on underlying and undelrying and handles end of round drawing + its text
    draw_underlyings_and_stones()

    
    # HANDLING OF PLAYER INPUTS -------------------------------------------------->

    # event handler
    for event in pygame.event.get():

    # quit game
        if event.type == pygame.QUIT:
            run = False

        # *** CLICK ***
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_function()

    # Draw the game screen
    pygame.display.update()

    # Limit the FPS by sleeping for the remainder of the frame time
    clock.tick(fps)


pygame.quit()
