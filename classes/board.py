from random import shuffle


class Board:
    def __init__(self):
        self.round_counter = 1
        self.number_of_players = 2
        self.tiles_on_underlying = 4
        self.underlyings = []
        self.bag_of_tiles = []
        self.bag_of_used_tiles = [] # used tiles after plays, wait for bag of tiles to be low on tiles to refill it wit everything
        self.tiles = dict()
        self.list_of_players = []
        self.minus_points = [-1, -1, -2, -2, -2, -3, -3]
    
    # INITIALIZING FUNCTION - only happens once at the beginning
    def select_num_players(self):
        # input from player for testing
        # self.number_of_players = int(input('How many players will play? <2-4>: '))
        self.number_of_players = 3
    
    # INITIALIZING FUNCTION
    def draw_underlyings(self):
        # last underlying will be the middle field
        num_underlyings = self.number_of_players + 3 + (self.number_of_players - 2) * 1 + 1
        for _ in range(num_underlyings):
            self.underlyings.append([])

    # INITIALIZING FUNCTION
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

    # Functions for every round:
    def scramble_bag_of_tiles(self):
        shuffle(self.bag_of_tiles)
        
        # FOR TESTING -  to play with the number of tiles
        # self.bag_of_tiles = self.bag_of_tiles[:15]

    def fill_in_underlyings(self):
        for i in range(len(self.underlyings)):
            # if middle underlying, also append -1
            if i == len(self.underlyings) - 1:
                self.underlyings[i].append(-1)
                break
            for _ in range(self.tiles_on_underlying):
                # if no tiles in the bag and still tiles in the used bad -> refill bag with tiles
                if len(self.bag_of_tiles) == 0 and len(self.bag_of_used_tiles) != 0:
                    self.refil_bag_of_tiles()
                # if there are tiles in the bag, append to underlying
                if len(self.bag_of_tiles) > 0:
                    self.underlyings[i].append(self.bag_of_tiles.pop())                
    
    def underlying_is_empty(self, index, printing=True):
        if len(self.underlyings[index]) == 0:
            if printing:
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
        
    # check if all underlyings are empty - end of round
    def all_underlyings_empty(self):
        count = 0
        for underlying in self.underlyings:
            if len(underlying) == 0:
                count += 1
        if count == len(self.underlyings):
            return True
        return False
    
    # refilling empty bag of tiles from bag of used tiles
    def refil_bag_of_tiles(self):
        for tile in self.bag_of_used_tiles:
            self.bag_of_tiles.append(tile)
        # empty bag of used tiles 
        self.bag_of_used_tiles.clear()
        # and scramble bag of tiles
        self.scramble_bag_of_tiles()
    
    def print_board_stats(self):
        print('len bag of tiles', len(self.bag_of_tiles))
        print('len bag of used tiles', len(self.bag_of_used_tiles))
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))