from random import randint, shuffle


class Board:
    def __init__(self):
        self.number_of_players = 0
        self.underlyings = []
        self.bag_of_tiles = []
        self.bag_of_used_tiles = [] # used tiles after plays, wait for bag of tiles to be low on tiles to refill it wit everything
        self.tiles = dict()
    
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
        for underlying in self.underlyings:
            if len(underlying) > 0:
                print(underlying)

    # checks what tiles are on top of underlying - returns dictionary
    def count_tiles_on_underlying(self, index):
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
            print('Select a valif tile. ')
            return False


class Player():
    def __init__(self, name):
        self.name = name
        self.take = []
        self.table = [[            [0], [0, 0, 0, 0, 0]],
                      [         [0, 0], [0, 0, 0, 0, 0]], 
                      [      [0, 0, 0], [0, 0, 0, 0, 0]], 
                      [   [0, 0, 0, 0], [0, 0, 0, 0, 0]], 
                      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]

    def choose_underlying(self, board):
        while True:
            # choose underlying
            underlying_choice = int(input('Which underlying do you choose? ')) - 1
            # check if not empty
            if board.underlying_is_empty(underlying_choice):
                board.print_available_underlyings()
                continue
            else:
                board.count_tiles_on_underlying(underlying_choice)
                print('Player ' + self.name + 'chose ' + str(underlying_choice + 1) + ' -> ' +str(board.underlyings[underlying_choice]))
                return underlying_choice

    def choose_tile(self, board):
        index = self.choose_underlying(board)
        while True:
            # choose specific tiles
            tile_choice = int(input('Which tile do you want? '))
            # check if tiles available
            if board.valid_tile_selected(tile_choice):
                # if yes - give them to players hand
                for tile in board.underlyings[index]:
                    if tile == tile_choice:
                        self.take.append(tile)
                print('self.take', self.take)

                # remove them from underlying
                for tile in board.underlyings[index]:    
                   board.underlyings[index].remove(tile_choice)
                
                # append the rest to the middle underlying
                for rest_item in board.underlyings[index]:
                    board.underlyings[-1].append(rest_item)
                
                # empty the underlying
                board.underlyings[index].clear()
                break

            else:
                continue

            
def main():
    brd = Board()
    print('number of players', brd.number_of_players)
    print('underlyings', brd.underlyings)
    brd.select_num_players()
    brd.draw_underlyings()

    print('number of players', brd.number_of_players)
    print('underlyings', brd.underlyings)

    brd.append_bag_of_tiles()
    print('after addition', brd.bag_of_tiles)
    brd.scramble_bag_of_tiles()
    print('after shuffle', brd.bag_of_tiles)

    brd.fill_in_bag_of_tiles()
    print('brd underlyings after fill', brd.underlyings)

    print('bag_of_tiles after fill', len(brd.bag_of_tiles), brd.bag_of_tiles)

    player1 = Player('Borec')

    player1.choose_tile(brd)

    print('Print players take: ')
    print(player1.take)

    print('underlyings', brd.underlyings)

    print('bag of used tiles: ', brd.bag_of_used_tiles)

if __name__ == '__main__':
    main()