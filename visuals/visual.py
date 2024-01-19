import pygame
import button
from random import shuffle

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
blue_stone_img = pygame.image.load('stone_blue.png').convert_alpha()        # VALUE 1
yellow_stone_img = pygame.image.load('stone_yellow.png').convert_alpha()    # VALUE 2
black_stone_img = pygame.image.load('stone_black.png').convert_alpha()      # VALUE 3
green_stone_img = pygame.image.load('stone_green.png').convert_alpha()      # VALUE 4
red_stone_img = pygame.image.load('stone_red.png').convert_alpha()          # VALUE 5





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
        table = create_table(i, table_pos_list[i])
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
    for i in range(4):
        for j in range(4):
            diff = 5
            print('i', i, 'j', j, 'diff', diff)
            # same coordinates logit as in normal underlying, but also Bool to track if stone is placed there or not. It's dynamic underlying
            middle_stone_pos = [(middle_pos[0] - (37 * j) - diff, middle_pos[1] + 5 + i * 42), False]
            middle_stone_pos_list.append(middle_stone_pos)
            print('middle_stone_pos', middle_stone_pos)
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


# STONE MANUAL TESTING
# MOVE X = 40
# COORDINATES LINE 3, PLAYER 4
blue_stone = button.Stone(1, 'not needed', 'blue_stone', 146, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone2 = button.Stone(1, 'not needed', 'blue_stone2', 186, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone3 = button.Stone(1, 'not needed', 'blue_stone3', 226, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)
blue_stone4 = button.Stone(1, 'not needed', 'blue_stone4', 356, 135, blue_stone_img, blue_stone_img, 0.2, 0.2)

blue_stone8 = button.Stone(1, 'not needed', 'blue_stone8', 946, 535, blue_stone_img, blue_stone_img, 0.2, 0.2)


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

        # skip the middle underlying for now
        if index + 1 == len(list_of_underlyings):
            break

        for i in range(4):
            value = bag_of_tiles[counter]
            x = underlying.stone_pos[i][0]
            y = underlying.stone_pos[i][1]
            # print('x', x, 'y', y)
            if value == 1:
                stone = button.Stone(value, 'not needed', 'blue_stone' + str(counter), x, y, blue_stone_img, blue_stone_img, 0.2, 0.2)
            elif value == 2:
                stone = button.Stone(value, 'not needed', 'yellow_stone' + str(counter), x, y, yellow_stone_img, yellow_stone_img, 0.2, 0.2)
            elif value == 3:
                stone = button.Stone(value, 'not needed', 'black_stone' + str(counter), x, y, black_stone_img, black_stone_img, 0.2, 0.2)
            elif value == 4:
                stone = button.Stone(value, 'not needed', 'green_stone' + str(counter), x, y, green_stone_img, green_stone_img, 0.2, 0.2)
            elif value == 5:
                stone = button.Stone(value, 'not needed', 'red_stone' + str(counter), x, y, red_stone_img, red_stone_img, 0.2, 0.2)
            print(id(stone))
            # list of stones on underlying
            underlying.stones.append(stone)
            counter += 1


draw_stones_on_underlyings()


# blue button just for testing
blue_button = button.Stone('blue test value', 'test stone pos', 'blue test', 300, 200, blue_img, blue_img, 0.7, 0.7)

screen.fill((202, 228, 241))

# appends stones from selected underlying, then used to compute how many fresh stones appended
stone_move_handler = []

# 
middle_stone_move_handler = []

# MAIN GAME LOOP
# drawing stuff and handling events (key presses)
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
                print('player', butt.player_index)
                print(butt.stone_pos)
            # ALWAYS ALSO DRAW STONE THATS ON THE LINE
            for stone in butt.stones:
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
        


    # blue stones testing
    if blue_stone.draw(screen):
        print(blue_stone.name)
    if blue_stone2.draw(screen):
        print(blue_stone2.name)
    if blue_stone3.draw(screen):
        print(blue_stone3.name)
    if blue_stone4.draw(screen):
        print(blue_stone4.name)
    
    blue_stone8.draw(screen)
        # print(blue_stone8.name)

    # test button after press changes background
    if blue_button.draw(screen):
        print('blue')
        screen.fill((0, 228, 241))



    # TODO HERE ADD SECOND LOOP FOR EACH PLAYERS PLAY
    
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


        # handle stone click
            


        if event.type == pygame.MOUSEBUTTONDOWN:
            # track len of stone move handler before and after to loop only through new stones
            len_stone_move_handler_before = len(stone_move_handler)
            print('len_stone_move_handler_before', len_stone_move_handler_before)

            # first click on stone on underlying - takes all stones from underlying and appends them into list
            for stone in list_of_underlyings[1].stones:
                if stone.rect.collidepoint(event.pos):
                    stone_move_handler.append(stone)
                    # check for memory adress
                    print('stone id', id(stone))
                    checker = True
                    print('stone move handler after first append', len(stone_move_handler))
                    print('collideeee')
                    # stone.x += 10
                    # stone.y += 10

            # CONDITION:   IF CLICKED ON STONE
            if len(stone_move_handler) > 0:

                # append all stones from underlying with same value
                print('stone move handler appending')
                for stone in list_of_underlyings[1].stones:
                    if stone.value == stone_move_handler[-1].value:
                        stone_move_handler.append(stone)
                        print(id(stone))


                    # rest of stones append to the MIDDLE
                    else:
                        list_of_underlyings[-1].stones.append(stone)
                
                        
                        # print('len middle stone handler', len(middle_stone_move_handler))
                        # print('middle pos check')
                        for stone_pos in (list_of_underlyings[-1].stone_pos):
                            if stone_pos[1] == False:
                                stone.x = stone_pos[0][0]
                                stone.y = stone_pos[0][1]
                                # print('stone x', stone.x)
                                # print('stone y', stone.y)
                                stone_pos[1] = True
                                break
                            
                list_of_underlyings[1].stones.clear()

                # removing last duplicate
                if checker == True:
                    print('removing', id(stone_move_handler.pop(0)))
                    checker = False

            # tracking actual length to loop over when selecting same value stones
            len_stone_move_handler_after = len(stone_move_handler) - len_stone_move_handler_before
            print('stone move handler after', len_stone_move_handler_after)

            # TESTING WHOLE CYCLE - still only line 4!!
            if list_of_tables[0][3].rect.collidepoint(event.pos):
                print('stone move handler')
                for stone in stone_move_handler:
                    print(id(stone))
                for i in range(len_stone_move_handler_before):
                    list_of_tables[0][3].stones.append(stone_move_handler[-i-1])
                    print('moving stone x', stone_move_handler[-i-1].x, 'y', stone_move_handler[-i-1].y)
                    stone_move_handler[-i-1].x = list_of_tables[0][3].stone_pos[i][0]
                    stone_move_handler[-i-1].y = list_of_tables[0][3].stone_pos[i][1]
                    print('moving stone after x', list_of_tables[0][3].stone_pos[i][0], 'y', list_of_tables[0][3].stone_pos[i][1])
                    
                
                # for stone in middle_stone_move_handler:
                # for stone_pos in (list_of_underlyings[-1].stone_pos):
                #     if stone_pos[1] == False:
                #         stone.x = stone_pos[0][0]
                #         stone.y = stone_pos[0][1]
                #         print('stone x', stone.x)
                #         print('stone y', stone.y)
                #         break


            # TODO LIST GETS EMPTY - LOOP DOESNT WAIT FOR NEXT CLICK - MUST IMPLEMENT SOME CLOCK OR WAIT MECHANISM
            # handle line choice
            # if list_of_tables[0][3].rect.collidepoint(event.pos):

                # print('stone_move_handler[0].x, list_of_tables[0][0].stone_pos[0]')
                # print('stone move handle', stone_move_handler)
                # stone_move_handler[-1].x = list_of_tables[0][3].stone_pos[0][0]
                # stone_move_handler[-1].y = list_of_tables[0][3].stone_pos[0][1]

                
        

    pygame.display.update()

pygame.quit()
