from random import shuffle
from classes.player import Player


# create players with generic names
def create_players(board):
    for i in range(board.number_of_players):
        player = Player('Player ' + str(i + 1))
        player.position_on_board = i + 1
        board.list_of_players.append(player)
    
    for player in board.list_of_players:
        print('player name', player.name)

# choose player order - starts player with first player = True
def choose_player_order(board):
    # first round - random order
    if board.round_counter == 1:
        shuffle(board.list_of_players)
        for player in board.list_of_players:
            print('player ', player.name, 'position on board', player.position_on_board)
        # cont = int(input('after shuffle'))
    else:
        index = 0
        start_appending = False
        player_order = []
        # creating looped list 1 -> 2 -> 3 -> 4 -> 1   - first will be the one with first player mark - every round this can change
        while True:
            if board.list_of_players[index].first_player == True:
                start_appending = True
            if start_appending:
                player_order.append(board.list_of_players[index])
            if index + 1 == len(board.list_of_players):
                index = -1
            if len(player_order) == len(board.list_of_players):
                break

            index += 1
        board.list_of_players.clear()
        for i in range(len(player_order)):
            board.list_of_players.append(player_order[i])
        for player in board.list_of_players:
            print('player ', player.name)
        player_order.clear()


# Displaying final score
def display_final_score(board):
    players_to_sort = []
    for player in board.list_of_players:
        players_to_sort.append(player)
    players_sorted = sorted(players_to_sort, key=lambda player: player.points_total, reverse=True)
    print('')
    print('----------------------------')
    print('The Winner is: ', players_sorted[0].name)
    print('----------------------------')
    print()
    print('Final score:')
    print('----------------------------')
    print('Player Name\tTotal Points')
    print('-------------+--------------')
    for player in players_sorted:
        print(player.name, '\t', player.points_total)
    
    display_stats_from_rounds(players_sorted)


# Displaying stats from all rounds
def display_stats_from_rounds(players_sorted):
    print()
    print('Stats from all rounds:')
    print('----------------------')
    # header print
    print('Round   ', end='\t')
    for player in players_sorted:
        print(player.name, end='\t')
    print()
    # first for loop - number of rounds (printing rows)
    for round_index in range(len(players_sorted[0].list_of_points_from_rounds)):
        print('Round', round_index + 1, end='\t\t')
        # for every player print points from each round (columns)
        for player in players_sorted:
            print(player.list_of_total_points[round_index], ' (', player.list_of_points_from_rounds[round_index], ') ', end='\t')
        print()
    print('Ending points', end='\t')
    for player in players_sorted:
        print(player.ending_points, end='\t\t')
    print()
    print('-'*60)
    # printing total points from the end
    print('Total', end='\t\t')
    sum_points_total = 0
    for player in players_sorted:
        print(player.points_total, end='\t\t')
        sum_points_total += player.points_total
    print('||', sum_points_total, '||')