from random import randint, shuffle


class Player():
    def __init__(self, name, bot):
        self.name = name
        self.bot = bot
        self.position_on_board = 0
        self.first_player = False
        self.points_from_round = 0
        self.list_of_points_from_rounds = []
        self.list_of_total_points = []
        self.ending_points = 0
        self.points_total = 0
        self.take = []
        self.to_the_middle = []
        self.minus_points = []
        self.table_left = [[[], 1],
                           [[], 2], 
                           [[], 3], 
                           [[], 4], 
                           [[], 5]]
        # value of the tile to be placed there and bool if already placed
        self.table_right = [[[1, False], [2, False], [3, False], [4, False], [5, False]],
                            [[5, False], [1, False], [2, False], [3, False], [4, False]],
                            [[4, False], [5, False], [1, False], [2, False], [3, False]],
                            [[3, False], [4, False], [5, False], [1, False], [2, False]],
                            [[2, False], [3, False], [4, False], [5, False], [1, False]]]
        
        self.table_right_transposed = [list(i) for i in zip(*self.table_right)]

        self.table_front = None

        # mainly for bot for drawing state backto frontend - maybe also for clicks prettier version for the future
        self.underlying_choice = None
        self.tile_choice = None
        self.line_choice = None
        

    # Function to print player table
    def print_player_table(self):
        print('Player', self.name, 'table: ')
        # compute longest left side
        max_len = 0
        for i in range(5):
            if len(self.table_left[i][0]) > max_len:
                max_len = len(self.table_left[i][0])
        # then print
        for i in range(5):
            len_to_print = max_len - len(self.table_left[i][0])
            print_setup = len_to_print
            if len(self.table_left[i][0]) > 0:
                print_setup = len_to_print + 2
            print(print_setup*' ', len_to_print*'  ', self.table_left[i], ' | ', self.table_right[i])
        print('Minus points: ', self.minus_points)
        

    # Function to choose underlying
    def choose_underlying(self, board, click_under, bot):
        while True:
            # choose underlying
            print('Board underlyings: ' , board.underlyings)
            # PLAYER
            # underlying_choice = int(input('Which underlying do you choose? ')) - 1
            # RANDOM BOT FOR TESTING
            # underlying_choice = self.bot_underlying_choice_simple(board) - 1
            # BETTER BOT FOR TESTING BOT CHOICE
            if bot:
                underlying_choice = self.bot_underlying_choice_advanced(board)
            # CLICK CHOICE
            else:
                underlying_choice = click_under
            print('underlying choice: ', underlying_choice + 1)
            # check if not empty
            if board.underlying_is_empty(underlying_choice):
                board.print_available_underlyings()
                continue
            else:
                board.count_tiles_on_underlying(underlying_choice)
                print('Player ' + self.name + ' chose ' + str(underlying_choice + 1) + ' -> ' +str(board.underlyings[underlying_choice]))
                # first to take middle underlying gets start player status and receives -1 to the minus points
                if -1 in board.underlyings[underlying_choice]:
                    if len(board.underlyings[underlying_choice]) == 1:
                        continue
                    else:
                        board.underlyings[underlying_choice].remove(-1)
                        self.first_player = True
                        self.minus_points.append(-1)
                        print('first to take the middle')
                        print('self.name, self.first_player', self.name, self.first_player)
                self.underlying_choice = underlying_choice
                return underlying_choice


    # Function to choose specific tile from the the underlying
    def choose_tile(self, board, click_tile, click_under, bot):
        index = self.choose_underlying(board, click_under, bot)
        middle_underlying = False
        if index == board.number_of_players + 3 + (board.number_of_players - 2) * 1:
            print('middle underlying')
            middle_underlying = True
        # max 5 tiles can be selected - counter will run max 5 times
        counter_index = 0
        if not bot:
            tile_choice = click_tile
            print('tile choice: ', tile_choice)
            # CHOOSING LOOP NOT BOT
            while True:
                # if yes - give them to players hand
                for tile in board.underlyings[index]:
                    if tile == tile_choice:
                        self.take.append(tile)
                    else:
                        self.to_the_middle.append(tile)
                    
                print(self.name, 'took ', self.take)                         
                print('to the middle goes ', self.to_the_middle)  
                # if not middle underlying selected
                if not middle_underlying:
                    for item in self.to_the_middle:
                        board.underlyings[-1].append(item)
                    board.underlyings[index].clear()
                    break
                # if middle underlying
                else:     
                    board.underlyings[index] = [value for value in board.underlyings[index] if value != tile_choice]
                    break 
        # choosing loop BOT
        if bot:
            while True:
                # choose specific tiles
                # PLAYER
                # tile_choice = int(input('Which tile do you want? '))
                # RANDOM BOT
                # tile_choice = randint(1, 5)
                # ADVANCED BOT
                list_of_ideal_tiles = self.bot_tile_choice_advanced(board)
                tile_choice = list_of_ideal_tiles[counter_index][0]
                # CLICK TILE CHOICE
                # check if tiles available
                if board.valid_tile_selected(tile_choice):
                    # if yes - give them to players hand
                    for tile in board.underlyings[index]:
                        if tile == tile_choice:
                            self.take.append(tile)
                        else:
                            self.to_the_middle.append(tile)
                    
                    self.tile_choice = tile_choice
                    print(self.name, 'took ', self.take)                         
                    print('to the middle goes ', self.to_the_middle)  
                    # if not middle underlying selected
                    if not middle_underlying:
                        for item in self.to_the_middle:
                            board.underlyings[-1].append(item)
                        board.underlyings[index].clear()
                        break
                    # if middle underlying
                    else:     
                        board.underlyings[index] = [value for value in board.underlyings[index] if value != tile_choice]
                        break 
                #### maybe for bot
                # if not - select another tile       
                else:
                    counter_index += 1
                    continue


    
    # FUNCTIONS TO HANDLE INPUT OF TAKEN TILE TO THE LEFT OF THE BOARD #
    def tile_already_placed_on_right(self, line, take):
        for i in range(len(self.table_right[line])):
            # print('i', i, 'self.table_right[line][i]', self.table_right[line][i])
            if self.table_right[line][i][0] == take:
                index = i
                break
        if self.table_right[line][index][1] == True:
            print('tile already placed on the right')
            return True
        else:
            print('tile is not on the right, free to place here')
            return False

    def line_has_free_space(self, line):
        free_spaces = self.table_left[line][1] - len(self.table_left[line][0])
        if free_spaces > 0:
            # print('line has free space, ', free_spaces, ' positions are free')
            # if len(self.take) > free_spaces:
                # print('Warning, not enough space - points will be deducted.')
            return True
        else:
            # print('line is full!, Free: ', free_spaces)
            return False
    
    def line_fully_free(self, line):
        if len(self.table_left[line][0]) == 0:
            # print('line ', line + 1, 'is fully free')
            return True
        else:
            # print('line ', line + 1, 'is not fully free')
            return False
    
    def same_tile_on_line(self, line, take):
        for tile in self.table_left[line][0]:
            if tile == take:
                # print('same tiles on line ', line + 1, 'possible to place here')
                return True
        # print('different tiles on line ', line + 1, 'cannot place here')
        return False
    
    def line_full(self, line):
        # edit to make posible clicking on full line - points go to minus
        # KEEP it like this for bot?
        if self.table_left[line][1] == len(self.table_left[line][0]):
            print('line full - points will go to minus') 
            return True
        return False

    
    def is_line_placeable(self, line, take):
        # first check if tile is not already placed on the right
        if not self.tile_already_placed_on_right(line, take):
            if self.line_has_free_space(line):
                if self.line_fully_free(line):
                    print('Line placeable - free')
                    return True
                else:
                    if self.same_tile_on_line(line, take):
                        print('Line placeable - same tiles')
                        return True
        if self.line_full(line):
            return True
        print('Line not placeable')
        return False
    
    # v2 version of no lines placeable function
    def no_lines_placeable_v2(self, take):
        placeable = False
        for i in range(5):
            print('line:', i + 1, ' - ', end='')
            if self.is_line_placeable(i, take):
                placeable = True
        if placeable:
            return False
        return True

    # Main functions that takes all checking functions above and places seleted tiles to the line
    def choose_line(self, line_front, bot):
        while True:
            # if there are no lines to place selected tiles, tiles ppend to self.minus_points
            if self.no_lines_placeable_v2(self.take[0]):
                for item in self.take:
                    self.minus_points.append(item)
                self.take.clear()
                self.to_the_middle.clear()
                break
            # choose specific tiles
            self.print_player_table()
            # PLAYER CHOICE
            # line_choice = int(input('Which line do you choose to place your tiles? ' + str(self.take) + ' :')) - 1
            # BOT CHOICE
            if bot:
                line_choice = self.bot_line_choice()
            # FRONTEND CHOICE
            else:
                line_choice = line_front
            print('line choice: ', line_choice)
            line_choice -= 1
            if self.is_line_placeable(line_choice, self.take[0]):
                self.line_choice = line_choice
                # place all tiles from hand to table left line choice
                for item in self.take:
                    self.table_left[line_choice][0].append(item)
                # empty the hand
                self.take.clear()
                self.to_the_middle.clear()
                break
            else:
                # choosing takes place int this while loop for in input or bot, but for visual its done bz click - loop wont end because if fails - cant select another within the loop
                # for bot it needs to keep continue - perhaps separate 2 taking functions in main loop and condition if bot
                if bot:
                    continue
                else:
                    break
    

    # bot LINE CHOICE
    def bot_line_choice(self):
        # list of line indexes
        line_choice_list = [1, 2, 3, 4, 4, 5, 5]
        # goes through all lines and chooses good ones
        for index, line in enumerate(self.table_left):
            # condition - same tile already on line - 
            if line[1] > len(line[0]) > 0:
                if line[0][0] == self.take[0]:
                    # print('line: ', line[1])
                    # ideal_take = int(input('take same as line value, continue?'))
                    for _ in range(2):
                        line_choice_list.append(index + 1)
                    # condition - exactly same remaining places on line as taken
                    if (line[1] - len(line[0])) == len(self.take):
                        for _ in range(20):
                            line_choice_list.append(index + 1)
                        # print('line: ', line[1])
                        # ideal_take = int(input('ideal value hit, continue?')) 
            # condition - line empty and equal length of take
            if line[1] == len(self.take) and len(line[0]) == 0:
                # print('line: ', line[1])
                # ideal_take = int(input('line empty and equal length of take, continue?'))
                for _ in range(5):
                    line_choice_list.append(index + 1)
            
        line_choice = line_choice_list[randint(0, len(line_choice_list) - 1)]
        print('line_choice_list', line_choice_list)
        return line_choice

        
    def bot_underlying_choice_simple(self, board):
        # select only non empty underlyings
        underlying_choice_list = []
        for index, underlying in enumerate(board.underlyings):
            if len(underlying) != 0:
                underlying_choice_list.append(index + 1)
            # condition if underlying is longer than 7 - more probability to take it
            if len(underlying) >= 7:
                for _ in range(5):
                    underlying_choice_list.append(index + 1)
        underlying_choice = underlying_choice_list[randint(0, len(underlying_choice_list) - 1)]
        print('underlying choice list', underlying_choice_list)
        # print('underlying choice:', underlying_choice)
        # ideal_take = int(input('underlying choice check, continue?'))
        return underlying_choice
    

    # function for determining best tiles and underlyings
    def bot_underlying_tile_choice_advanced(self, board):
        # first determine which tile is most desired, then find underlying with this tile
        list_of_possible_tile_choices = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]
        # Search on RIGHT
        for i, line in enumerate(self.table_right):
            for index, item in enumerate(line):
                expected_points_from_tile = 0
                # if item is not occupied
                if item[1] == False:
                    # print('item', item[0], 'line', i + 1)
                    item[1] = True
                    # count the expected value
                    points_from_row = self.count_points_from_row(item[0], i, self.table_right)
                    points_from_col = self.count_points_from_row(item[0], index, self.table_right_transposed)
                    expected_points_from_tile += points_from_row
                    expected_points_from_tile += points_from_col
                    expected_points_from_tile += self.compute_row_col_point_substraction(points_from_row, points_from_col)
                    # TODO ADD COUNT OF COLORS AND IF 5 THEN INCREASE EXPECTED VALUE
                    # if column can be completed (5 points from column)
                    if points_from_col == 5:
                        expected_points_from_tile += 5
                    # print('expected points', expected_points_from_tile)
                    item[1] = False
                    # add expected value from the tile to the list
                    for tile in list_of_possible_tile_choices:
                        if tile[0] == item[0]:
                            tile[1] += expected_points_from_tile
        # Search on LEFT
        # value to increase if line on left is neither full nor empty
        increase_value = 2
        for line in self.table_left:
            if len(line[0]) > 0 and len(line[0]) < line[1]:
                ideal_tile = line[0][0]
                # add increase value from the tile to the list
                for tile in list_of_possible_tile_choices:
                    if tile[0] == ideal_tile:
                        tile[1] += increase_value
        # sort the list accroding to expected value
        sorted_list_of_possible_tile_choices = sorted(list_of_possible_tile_choices, key=lambda x: x[1], reverse=True)
        # find desired underlying - for each best tile - go from the best ti the worst - if it finds it - cycle will break so only the best remains
        for tile_choice in sorted_list_of_possible_tile_choices:
            ideal_underlyings = []
            for index, underlying in enumerate(board.underlyings):
                if tile_choice[0] in underlying:
                    ideal_underlyings.append([index + 1, tile_choice[0]])
            if len(ideal_underlyings) > 0:
                break
        sorted_ideal_underlyings = sorted(ideal_underlyings, key=lambda x: x[0], reverse=True)
        shuffle(sorted_ideal_underlyings)
        choices = [sorted_list_of_possible_tile_choices, sorted_ideal_underlyings]
        print('choices', choices)
        return choices

    def bot_underlying_choice_advanced(self, board):
        choices = self.bot_underlying_tile_choice_advanced(board)[1]
        return choices[0][0] - 1

    def bot_tile_choice_advanced(self, board):
        choice = self.bot_underlying_tile_choice_advanced(board)[0]
        return choice
    

    
    # FUNCTIONS TO HANDLE MINUS POINTS ON THE LEFT SIDE - if more than allowed ammount of tiles is placet to a line #
    # calculate number of minus points to move from single line, move them and remove them
    def calculate_minus_points_to_move(self, line):
        # if line is fully free - dont do this calculation
        if self.line_fully_free(line[1] - 1):
            return
        # value is the last element on line, not first - important when removing
        value = line[0][-1]
        # if there are more tiles on line than allowed
        if len(line[0]) > line[1]:
            num_to_move = len(line[0]) - line[1]
            print('Line: ', line[1], 'num of tiles to move to minus points:', num_to_move)
            # append all of them to the self.minus_points
            for _ in range(num_to_move):
                print(value, 'goes to minus points')
                self.minus_points.append(value)
            # and remove them from the line - kepp only the number of tiles that is allowed
            for _ in range(num_to_move):
                # edit for when clicked on full line
                if value in line[0]:
                    line[0].remove(value)
        else:
            print('Line: ', line[1],': Nothing to move')

    # move all minus point from all lines to the minus_points list - just moving the points
    def move_all_minus_points(self):
        print('Handling of minus points')
        for line in self.table_left:
            self.calculate_minus_points_to_move(line)

    # adding minus points to score from round
    def add_minus_points_to_points_from_round(self, board):
        print('Points from round after tiles placed to the right: ', self.points_from_round)
        print('Adding minus points...')
        minus_points = 0
        if len(self.minus_points) > 0:
            for i in range(len(self.minus_points)):
                # maximum of minus points defined in board (-1, -1, -2, -2, -2, -3, -3)
                if i == len(board.minus_points):
                    break
                minus_points += board.minus_points[i]
            # add minus points to points from round
            self.points_from_round += minus_points
        print('Minus points this round:', minus_points)
        print('Points from round after minus points accounted:', self.points_from_round)
        self.points_total += self.points_from_round
        # POINTS CANT BE NEGATIVE - IF BELOW 0 - RESET TO 0
        if self.points_total < 0:
            self.points_total = 0
        print()
        print('Total points so far: ', self.points_total)
        # TODO HERE IS THE PLACE TO ADD FUNCTION TO TAKE STATS FOR EVERY ROUND FOR ALL PLAYERS

        # move minus points to bag of used tiles
        for minus_point in self.minus_points:
            if minus_point != -1:
                board.bag_of_used_tiles.append(minus_point)
        # append points from round to list of points from rounds, reset minus points and reset points from round to 0
        self.list_of_points_from_rounds.append(self.points_from_round)
        self.list_of_total_points.append(self.points_total)
        self.minus_points.clear()
        self.points_from_round = 0
    

    # SECTION FOR PLACING FULL LINE TILES TO THE RIGHT TABLE after end of each round #
    # Main function for placing ONE tile to right - under more functions to calculate points while placing
    def place_tile_to_right(self, board, i):
        points_from_value_placed = 0
        print()
        # print('start placing full tiles to right, line', i + 1)
        if len(self.table_left[i][0]) == self.table_left[i][1]:
            # print('line full - will be placed to the right, value:', self.table_left[i][0][0])
            # go through right and place to right place on the right side of the table
            for index, item in enumerate(self.table_right[i]):
                if item[0] == self.table_left[i][0][0]:
                    item[1] = True
                    # HERE WILL BE THE FUNCTION TO GO THROUGH ALL OF THE RIGHT SIDE AND COUNT POINTS SO FAR
                    # ROW COUNTER: i = line_number, value = item[0], table = self.table_right
                    points_from_row = self.count_points_from_row(item[0], i, self.table_right)
                    # COLUMN COUNTER: i = line_number, value = item[0]
                    points_from_col = self.count_points_from_row(item[0], index, self.table_right_transposed)
                    row_col_substraction = self.compute_row_col_point_substraction(points_from_row, points_from_col)
                    # THIS IS DURING GAME!! NOT AFTER - IT IS CORRECT
                    points_from_value_placed += points_from_row
                    points_from_value_placed += points_from_col
                    points_from_value_placed += row_col_substraction
                    # print('Total points from value placed: ', points_from_value_placed)
                    self.points_from_round += points_from_value_placed
            # remove 1 tile from left line
            self.table_left[i][0].pop()
            # and rest put into bag of used tiles
            if len(self.table_left[i][0]) != 0:
                for item in self.table_left[i][0]:
                    board.bag_of_used_tiles.append(item)
                # and clear the line
                self.table_left[i][0].clear()
            # and add points to whole counter
    
    # -> THIS GOES INTO MAIN
    # Places tiles from all lines 
    def place_all_tiles_to_right(self, board):
        for i in range(5):
            self.place_tile_to_right(board, i)

    # input - value of tile, line number from function above and table - For column the same only table and line_number are transposed
    def count_points_from_row(self, value, line_number, table):
        # print('value', value)
        # print('line number', line_number + 1)
        lock = False
        row_points_counter = 0
        count_further = True
        # goes through single row
        for item in table[line_number]:
            if item[1] == True:
                # print('filled value hit')
                if item[0] == value:
                    # print('value hit, locking counter')
                    lock = True
                if count_further:
                    # print('adding + 1')
                    row_points_counter += 1
            else:
                # print('empty value')
                if not lock:
                    # print('not locked yet')
                    row_points_counter = 0
                else:
                    # print('false after true hit, stop adding points')
                    count_further = False
        # print('Adding + ', row_points_counter, 'points.')
        return row_points_counter
    
    # to remove duplicit points when column or row have only single tile
    #   # # #                            #
    #   #                    # # #       #
    #   #    ... 6 points ,         or   #  ... 3 points (function calculates 4 - therefore this function to substract -1)
    def compute_row_col_point_substraction(self, row_points, col_points):
        if row_points > 1 and col_points > 1:
            # print('both row and col have more than 1 point - no substraction')
            return 0
        else: 
            # print('row or col or both have 1 point - substracting -1')
            return -1
        
    # to check AFTER ROUND ENDS if one whole row on the right is filled - when yes - game ends
    def row_completed(self):
        for index, row in enumerate(self.table_right):
            true_counter = 0
            for item in row:
                if item[1] == True:
                    true_counter += 1
                    if true_counter == 5:
                        print()
                        print('Row', index + 1, 'is completed. GAME ENDS')
                        print()
                        return True
        print()
        print('No rows completed yet, game continues.')
        print()
        return False
    
    # FUNCTIONS TO COUNT EXTRA POINTS AFTER GAME ENDS #
    # Counting full rows
    def count_completed_rows(self):
        full_rows_counter = 0
        for index, row in enumerate(self.table_right):
            true_counter = 0
            for item in row:
                if item[1] == True:
                    true_counter += 1
                    if true_counter == 5:
                        print('Row', index + 1, 'completed. + 2 points.')
                        full_rows_counter += 1
        print('Rows completed: ', full_rows_counter)
        print('Points from rows: ', full_rows_counter * 2)
        return full_rows_counter

    # Counting full columns
    def count_completed_cols(self):
        full_cols_counter = 0
        for index, row in enumerate(self.table_right_transposed):
            true_counter = 0
            for item in row:
                if item[1] == True:
                    true_counter += 1
                    if true_counter == 5:
                        print('Column', index + 1, 'completed. + 7 points.')
                        full_cols_counter += 1
        print('Columns completed: ', full_cols_counter)
        print('Points from columns: ', full_cols_counter * 7)
        return full_cols_counter
    
    # Counting full colors
    def count_completed_colors(self):
        all_placed_tiles_dict = dict()
        # append all placed tiles (True on right) to a dict
        for row in self.table_right:
            for item in row:
                if item[1] == True:
                    if item[0] not in all_placed_tiles_dict:
                        all_placed_tiles_dict[item[0]] = 1
                    else:
                        all_placed_tiles_dict[item[0]] += 1
        full_color_counter = 0
        for item in all_placed_tiles_dict:
            if all_placed_tiles_dict[item] == 5:
                print('Color', item, 'completed, + 10 points.')
                full_color_counter += 1
        print('Colors completed: ', full_color_counter)
        print('Points from colors: ', full_color_counter * 10)
        return full_color_counter
    
    # main function
    def count_ending_points(self):
        self.ending_points += self.count_completed_rows() * 2
        self.ending_points += self.count_completed_cols() * 7
        self.ending_points += self.count_completed_colors() * 10
        print('Total points so far: ', self.points_total)
        # print ending points
        print('Points from rows, columns and colors: ', self.ending_points)
        # and add them to ending points list

        # add ending points to total points
        self.points_total += self.ending_points
        print()
        print('Total points: ', self.points_total)
        print('\n')
        # reseting points from round
        self.points_from_round = 0


    # help function to print all attributes
    def print_all_attributes(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))