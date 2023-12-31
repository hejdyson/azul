from random import shuffle


class Board:
    def __init__(self):
        self.number_of_players = 0
        self.underlyings = []
        self.bag_of_tiles = []
        self.bag_of_used_tiles = [] # used tiles after plays, wait for bag of tiles to be low on tiles to refill it wit everything
        self.tiles = dict()
        self.list_of_players = []
        self.minus_points = [-1, -1, -2, -2, -2, -3]
    
    # initialization functions
    def select_num_players(self):
        # input from player for testing
        # self.number_of_players = int(input('How many players will play? <2-4>: '))
        self.number_of_players = 3
    
    def draw_underlyings(self):
        # last underlying will be the middle field
        num_underlyings = self.number_of_players + 3 + (self.number_of_players - 2) * 1 + 1
        for _ in range(num_underlyings):
            self.underlyings.append([])

    def append_bag_of_tiles(self):
        for i in range(5):
            for _ in range(20):
                if i == 0:
                    self.bag_of_tiles.append(1)
                elif i == 1:
                    self.bag_of_tiles.append(2)
                elif i == 2:
                    self.bag_of_tiles.append(3)
                elif i == 3:
                    self.bag_of_tiles.append(4)
                else:
                    self.bag_of_tiles.append(5)

    def scramble_bag_of_tiles(self):
        shuffle(self.bag_of_tiles)

    def fill_in_bag_of_tiles(self):
        for i in range(len(self.underlyings)):
            if i == len(self.underlyings) - 1:
                self.underlyings[i].append(-1)
                break
            for _ in range(4):
                self.underlyings[i].append(self.bag_of_tiles.pop())
    
    def underlying_is_empty(self, index):
        if len(self.underlyings[index]) == 0:
            print('You can\'t choose empty underlying.')
            return True
        return False
    
    def print_available_underlyings(self):
        print('Available underlyings: ')
        for index, underlying in enumerate(self.underlyings, start=1):
            if len(underlying) > 0:
                print(underlying, 'index: ', index)

    # checks what tiles are on top of underlying - returns dictionary
    def count_tiles_on_underlying(self, index):
        self.tiles.clear()
        print('tiles on selected underlying:', self.underlyings[index])

        # create a dict with tile and number of the on the underlying
        for tile in self.underlyings[index]:
            if tile not in self.tiles:
                self.tiles[tile] = 1
            else:
                self.tiles[tile] += 1
        
        print('possible takes:')
        for item in self.tiles:
            print(item, ' : ', self.tiles[item])
        
    
    def valid_tile_selected(self, tile_choice):
        if tile_choice in self.tiles:
            return True
        else:
            print('Select a valid tile. ')
            return False


class Player():
    def __init__(self, name):
        self.name = name
        self.first_player = False
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
        
    def print_player_table(self):
        print('Player table: ')
        for i in range(5):
            print(self.table_left[i], ' | ', self.table_right[i])
        print('Minus points: ', self.minus_points)
        

    def choose_underlying(self, board):
        while True:
            # choose underlying
            print('Board underlyings: ' ,board.underlyings)
            underlying_choice = int(input('Which underlying do you choose? ')) - 1
            # check if not empty
            if board.underlying_is_empty(underlying_choice):
                board.print_available_underlyings()
                continue
            else:
                board.count_tiles_on_underlying(underlying_choice)
                print('Player ' + self.name + ' chose ' + str(underlying_choice + 1) + ' -> ' +str(board.underlyings[underlying_choice]))
                # first to take middle underlying gets start player status and receives -1 to the minus points
                if -1 in board.underlyings[underlying_choice]:
                    board.underlyings[underlying_choice].remove(-1)
                    self.first_player = True
                    self.minus_points.append(-1)
                    print('first to take the middle')
                return underlying_choice

    def choose_tile(self, board):
        index = self.choose_underlying(board)
        middle_underlying = False
        if index == board.number_of_players + 3 + (board.number_of_players - 2) * 1:
            print('middle underlying')
            middle_underlying = True
        while True:
            # choose specific tiles
            tile_choice = int(input('Which tile do you want? '))
            # check if tiles available
            if board.valid_tile_selected(tile_choice):
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
            # if not - select another tile       
            else:
                continue
    
    # FUNCTIONS TO HANDLE INPUT OF TAKEN TILE TO THE LEFT OF THE BOARD #
    def tile_already_placed_on_right(self, line):
        for i in range(len(self.table_right[line])):
            if self.table_right[line][i][0] == self.take[0]:
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
            print('line has free space, ', free_spaces, ' positions are free')
            if len(self.take) > free_spaces:
                print('Warning, not enough space - points will be deducted.')
            return True
        else:
            print('line is full!, Free: ', free_spaces)
            return False
    
    def line_fully_free(self, line):
        if len(self.table_left[line][0]) == 0:
            print('line ', line + 1, 'is fully free')
            return True
        print('line ', line + 1, 'is not fully free')
        return False
    
    def same_tile_on_line(self, line):
        for tile in self.table_left[line][0]:
            if tile == self.take[0]:
                print('same tiles on line ', line + 1, 'possible to place here')
                return True
        print('different tiles on line ', line + 1, 'cannot place here')
        return False

    def is_line_placeable(self, line):
        # first check if tile is not already placed on the right
        if not self.tile_already_placed_on_right(line):
            if self.line_has_free_space(line):
                if self.line_fully_free(line):
                    print('Line placeable - free')
                    return True
                else:
                    if self.same_tile_on_line(line):
                        print('Line placeable - same tiles')
                        return True
        print('Line not placeable')
        return False
    
    # check all lines if there is place for selected tiles
    def no_lines_placeable(self):
        empty = False
        for i in range(5):
            print('line: ', i + 1, end=' - ')
            # same tiles already on line and still free space -> then OK
            if len(self.table_left[i][0]) > 0 and len(self.table_left[i][0]) < self.table_left[i][1]:
                if self.take[0] == self.table_left[i][0][0]:
                    print('still place, not empty, only for ', self.take, 'free places: ', self.table_left[i][1] - len(self.table_left[i][0]))
                    empty = True
                else:
                    print('life occupied with', self.table_left[i][0])
            # or if the line is still empty
            if len(self.table_left[i][0]) == 0:
                print('still place, line empty')
                empty = True
            if len(self.table_left[i][0]) >= self.table_left[i][1]:
                print('line full')
        if empty == True:
            return False
        # if no line has free space for selected tile - returns True
        print('no lines placeable')
        return True

    # main functions that takes all checking functions above and places seleted tiles to the line
    def choose_line(self):
        while True:
            # if there are no lines to place selected tiles, tiles ppend to self.minus_points
            if self.no_lines_placeable():
                for item in self.take:
                    self.minus_points.append(item)
                    self.take.clear()
                    self.to_the_middle.clear()
                break
            # choose specific tiles
            self.print_player_table()
            line_choice = int(input('Which line do you choose to place your tiles? ' + str(self.take) + ' :')) - 1
            if self.is_line_placeable(line_choice):
                # place all tiles from hand to table left line choice
                for item in self.take:
                    self.table_left[line_choice][0].append(item)
                # empty the hand
                self.take.clear()
                self.to_the_middle.clear()
                break
            else:
                continue



            
def main():
    brd = Board()
    # print('number of players', brd.number_of_players)
    # print('underlyings', brd.underlyings)
    brd.select_num_players()
    brd.draw_underlyings()

    # print('number of players', brd.number_of_players)
    # print('underlyings', brd.underlyings)

    brd.append_bag_of_tiles()
    #print('after addition', brd.bag_of_tiles)
    brd.scramble_bag_of_tiles()
    #print('after shuffle', brd.bag_of_tiles)

    brd.fill_in_bag_of_tiles()
    # print('brd underlyings after fill', brd.underlyings)

    #print('bag_of_tiles after fill', len(brd.bag_of_tiles), brd.bag_of_tiles)

    player1 = Player('Player 1')

    while True:
        player1.choose_tile(brd)

        print('underlyings', brd.underlyings)
        player1.choose_line()

        player1.print_player_table()

        print('bag of used tiles: ', brd.bag_of_used_tiles)

if __name__ == '__main__':
    main()