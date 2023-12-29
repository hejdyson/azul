from random import randint, shuffle


class Board:
    def __init__(self):
        self.number_of_players = 0
        self.underlyings = []
        self.bag_of_tiles = []
        self.bag_of_used_tiles = [] # used tiles after plays, wait for bag of tiles to be low on tiles to refill it wit everything
    
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


class Player():
    def __init__(self):
        self.take = []
        self.table = [[            [0], [0, 0, 0, 0, 0]],
                      [         [0, 0], [0, 0, 0, 0, 0]], 
                      [      [0, 0, 0], [0, 0, 0, 0, 0]], 
                      [   [0, 0, 0, 0], [0, 0, 0, 0, 0]], 
                      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]

    def take_tiles(self, board):
        pass
    


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


if __name__ == '__main__':
    main()