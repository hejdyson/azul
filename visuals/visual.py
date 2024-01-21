import pygame
import button
from random import shuffle

# create display window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AZUL ONLINE')

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



NUM_PLAYERS = 4


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


    # create button instance
    square_button = button.Line(player_index, stone_pos_list_line1, 'line', 1, x, y, square_img1, square_img1_hover, scale, scale)
    square2_button = button.Line(player_index, stone_pos_list_line2, 'line', 2, x, y + diff_line, square_img2, square_img2_hover, scale, scale)
    square3_button = button.Line(player_index, stone_pos_list_line3, 'line', 3, x, y + diff_line * 2, square_img3, square_img3_hover, scale, scale)
    square4_button = button.Line(player_index, stone_pos_list_line4, 'line', 4, x, y + diff_line * 3, square_img4, square_img4_hover, scale, scale)
    square5_button = button.Line(player_index, stone_pos_list_line5, 'line', 5, x, y + diff_line * 4, square_img5, square_img5_hover, scale, scale)
    
    table_right_label = button.Line(player_index, 'stone pos here', 'table right', None, x + diff_tables, y, table_right_img, table_right_img, scale, scale)
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
    table_pos_list = [(220, 445), (1050 , 445), (1050, 70), (220, 70)]
    tables_list = []
    for i in range(num_players):
        table = create_table(i, table_pos_list[i])
        tables_list.append(table)
    
    return tables_list


def create_underlyings(num_players):
    underlying_pos_list2 = [(645, 460), (825, 368), (745, 180), (600, 180), (520, 320)]
    underlying_pos_list3 = [(545, 430), (680, 460), (825, 390), (825, 278), (745, 180), (600, 180), (520, 320)]
    underlying_pos_list4 = [(545, 430), (645, 460), (745, 460), (825, 368), (825, 278), (745, 180), (645, 180), (545, 210), (525, 320)]


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
    # TODO MAYBE ADD MORE PLACES IN THE MIDDLE
    for i in range(4):
        for j in range(4):
            diff = 7
            print('i', i, 'j', j, 'diff', diff)
            # same coordinates logit as in normal underlying, but also Bool to track if stone is placed there or not. It's dynamic underlying
            middle_stone_pos = [(middle_pos[0] - (37 * j) - diff, middle_pos[1] + diff + i * 37), False]
            middle_stone_pos_list.append(middle_stone_pos)
            print('middle_stone_pos', middle_stone_pos)
    middle_underlying_button = button.Underlying('middle u index', middle_stone_pos_list, 'middle underlying', middle_pos[0], middle_pos[1], middle_underlying_img, middle_underlying_img_hover, 0.2, 0.2)
    underlyings_list.append(middle_underlying_button)

    return underlyings_list

# drawing right side of table -NOT USED - only when table right os not a BUTTON OBJECT
def draw_table_right(num_players):
    table_right_pos_list = [(230, 450), (1060, 450), (1060, 70), (230, 70)]
    for i in range(num_players):
        screen.blit(table_right_img, table_right_pos_list[i])


# drawing player backgrounds
def draw_player_backgrounds(num_players):
    background_pos_list = [(15, 395), (845 , 395), (845, 15), (15, 15)]
    for i in range(num_players):
        screen.blit(player_background_img, background_pos_list[i])

        


# crating all tables
# 4 - number of players
list_of_tables = create_board(NUM_PLAYERS)

# creating all underlyings
list_of_underlyings = create_underlyings(NUM_PLAYERS)



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
    print('bag of tiles', bag_of_tiles)
    return bag_of_tiles
    

# button loop test stone on underlying WORKS
# HERE STONES WILL APPEND ACCORDING TO BAG OF TILES - SAME AS IN BACKEND
# IN GAME THE VALUE WILL COME FROM board.fill_in_underlyings - self.bag_of_tiles.pop()
def draw_stones_on_underlyings():
    bag_of_tiles = create_bag_of_stones()
    shuffle(bag_of_tiles)
    print('bag of tiles shuffled', bag_of_tiles)
    counter = 0
    for index, underlying in enumerate(list_of_underlyings):

        # MIDDLE UNDERLYING - add -1
        if index + 1 == len(list_of_underlyings):

            x = underlying.stone_pos[0][0][0]
            y = underlying.stone_pos[0][0][1]
            underlying.stone_pos[0][1] = True
            stone = button.Stone(-1, underlying, 'MINUS_STONE', x, y, stone_minus_img, stone_minus_img, 0.2, 0.2)
            underlying.stones.append(stone)
            
            print('middle underlying xxxxxxx')
            print(underlying.name)
            print(underlying.stone_pos)
            print(underlying.stones)
        
        else:
            # NORMAL UNDERLYINGS
            for i in range(4):
                value = bag_of_tiles[counter]
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
                counter += 1


draw_stones_on_underlyings()


# TEST BLUE STONE  - RATHER KEEP
# last coordinates  ( 430 - 3, 450 + 205 + 4)
                    #  427,     659
                    #  349
# blue_stone1 = button.Stone('None', 'not needed', 'blue_stone2', 1050 + 207-40*6 + 6, 450 + 205 + 4, blue_stone_img, blue_stone_img, 0.2, 0.2)


# set up background color
screen.fill((202, 228, 241))





# MAIN GAME LOOP
# drawing stuff and handling events (key presses)

possible_to_click_on_stones = True

run = True
while run:
    # THERE MUST BE ALWAYS TWO PARTS IN THE MAIN PYGAME LOOP
        # DRAWING OF STUFF ON SCREEN and
        # HANDLING USER INPUTS

    # DRAWING ---------------------------------------------------------------------->

    # handle drawing of tables
    draw_player_backgrounds(NUM_PLAYERS)
    # draw_table_right(NUM_PLAYERS)
    for table in list_of_tables:
        for line in table:
            # print('screen', butt.draw(screen))
            line.draw(screen)
            # ALWAYS ALSO DRAW STONE THATS ON THE LINE
            for stone in line.stones:
                stone.draw(screen)

    # handle drawing underlyings
    for underlying in list_of_underlyings:
        underlying.draw(screen)
        # print(underlying.player_index)
        # print(underlying.name)
        # print(underlying.stone_pos)
        # ALWAYS ALSO DRAW STONES THAT ARE ON UNDERLYING
        for i in range(len(underlying.stones)):
            underlying.stones[i].draw(screen)


    # TEST BLUE STONE RATHER KEEP
    # blue_stone1.draw(screen)


    # TODO HERE ADD SECOND LOOP FOR EACH PLAYERS PLAY
    
    # HANDLING OF PLAYER INPUTS -------------------------------------------------->

    # event handler
    for event in pygame.event.get():

    # quit game
        if event.type == pygame.QUIT:
            run = False

            
        # *** CLICK ***
        if event.type == pygame.MOUSEBUTTONDOWN:

            # FIRST - CLICK MUST BE ON STONE ON UNDERLYING -> SEARCH ONLY FOR THOSE CLICKS
            for underlying in list_of_underlyings:
                for stone in underlying.stones:
                    # it is possible only at first, then it needst click on line, no other stones can be clicked
                    if possible_to_click_on_stones:
                        # when clicked stone found
                        if stone.rect.collidepoint(event.pos):
                            # if stone clicked is not on line
                            if stone.placement.name == 'line' or stone.placement.name == 'minus points' or stone.placement.name == 'table right':
                                print('stone on line clicked')
                                break

                            # first disable another stone click - now only line click is accepted - ONLY CLICK SWITCHES THIS TO FALSE
                            possible_to_click_on_stones = False
                            print('possible_to_click_on_stones', possible_to_click_on_stones)
                            # helpful prints
                            print('stone placement, stones, name', stone.placement, stone.placement.stones, stone.placement.name)
                            # loop through all stones on the placement - decide what will go to line and what to the middle
                            to_line = []
                            to_the_middle = []
                            # appending to line same stones
                            for tile in stone.placement.stones:
                                if tile.value == stone.value:
                                    to_line.append(tile)
                                # IF TAKEN FIRST FORM THE MIDDLE
                                elif tile.value == -1:
                                    to_line.append(tile)
                                    # TODO LATER HANDLE
                                # different stones go to middle
                                else:
                                    to_the_middle.append(tile)
                            # help print what goes where
                            print('to line goes', to_line)
                            for item in to_line:
                                print(item.name)
                            print('to the middle goes', to_the_middle)
                            for item in to_the_middle:
                                print(item.name)

                            # CLICKED ON MIDDLE UNDERLYING
                            # if clicked on the middle - managing of coordinates
                            for item in to_line:
                                # handle of middle coordinates
                                if item.placement == list_of_underlyings[-1]:
                                    from_the_middle = True
                                    print('taking from the middle')
                                    for position in list_of_underlyings[-1].stone_pos:
                                        print('position', position)
                                        print('position of stone x', item.x, 'y:', item.y)
                                        # removing taken stones from the middle
                                        if position[0] == (item.x, item.y):
                                            print('occupied middle position to be freed', position)
                                            position[1] = False
                                    # handle of middle stones
                                    list_of_underlyings[-1].stones.remove(item)
                                else:
                                    from_the_middle = False

                            # HANDLE ADDING TILES TO MIDDLE
                            # append to the list of stones of middle underlying
                            # happens only when not taking from the middle
                            if not from_the_middle:
                                for tile in to_the_middle:
                                    list_of_underlyings[-1].stones.append(tile)
                                    tile.placement = list_of_underlyings[-1]
                                # change coordinates of stone to the ones from the middle that are available
                                for tile in to_the_middle:
                                    for stone_pos in list_of_underlyings[-1].stone_pos:
                                        if stone_pos[1] == False:
                                            tile.x = stone_pos[0][0]
                                            tile.y = stone_pos[0][1]
                                            stone_pos[1] = True
                                            break
            

            # SEDOND - CLICK MUST BE ON LINE OF PLAYER WHICH IS ON TURN - for now only player 1
            if not possible_to_click_on_stones:
                # now only player 1 - first table - list_of_tables [0]
                for line in list_of_tables[0]:
                    if line.rect.collidepoint(event.pos):
                        # just check if not clicked on minus points or on table right
                        if line == list_of_tables[0][-1] or line == list_of_tables[0][-2]:
                            print('table right or minus points')
                            break


                        if len(line.stones) != 0 and len(line.stones) != line.limit:
                            # check if line has different stones on it
                            if to_line[-1].value != line.stones[0].value:
                                print('different stones already on line')
                                break


                        # first enable clicking on stone on underlying again
                        possible_to_click_on_stones = True
                        print('possible_to_click_on_stones', possible_to_click_on_stones)

                        # Handling of stone click placement - either on line or to minus points if over the line limit: 1 APPEND 2 CHANGE COORDINATES
                        # LINE: append to the line list of stones
                        for stone in to_line:
                            if stone.value != -1:
                                line.stones.append(stone)
                                stone.placement = line
                            # if -1 taken
                            else:
                                list_of_tables[0][-1].stones.append(stone)
                                stone.placement = list_of_tables[0][-1]

                        # minus points - if over line limit
                        # MINUS_POINTS: append over the limit stones to minus points list of stones
                        if len(line.stones) > line.limit:
                            for i in range(len(line.stones) - line.limit):
                                # change stone placement to minus point
                                line.stones[-i-1].placement = list_of_tables[0][-1]
                                # append stone to minus point point list (only of there is still place)
                                # TODO HARD TO REACH EDGECASE - ALL LINES FULL AND ALSO MINUS POINTS FULL - STONES WONT GO TO MIDDLE
                                if len(list_of_tables[0][-1].stones) < list_of_tables[0][-1].limit:
                                    list_of_tables[0][-1].stones.append(line.stones[-i-1])
                            # remove excessive stones from line.stones
                            for i in range(len(line.stones) - line.limit):
                                line.stones.pop()

                        # LINE: change coordiates to the line coordinates
                        for i in range(len(line.stones)):
                            line.stones[i].x = line.stone_pos[i][0]
                            line.stones[i].y = line.stone_pos[i][1]

                        # MINUS_POINTS: change coordinates to minus points coordinates 
                        for i in range(len(list_of_tables[0][-1].stones)):
                            list_of_tables[0][-1].stones[i].x = list_of_tables[0][-1].stone_pos[i][0]
                            list_of_tables[0][-1].stones[i].y = list_of_tables[0][-1].stone_pos[i][1]

                print('middle positions:', list_of_underlyings[-1].stone_pos)
                


    pygame.display.update()

pygame.quit()
