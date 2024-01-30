from classes.board import Board
import backend


def main():
    brd = Board()

    brd.select_num_players()
    backend.create_players(brd)
    brd.draw_underlyings()
    brd.append_bag_of_tiles()
    #print('after addition', brd.bag_of_tiles)
    brd.scramble_bag_of_tiles()

    while True:
        print('Round:', brd.round_counter)
        brd.fill_in_underlyings()
        # Assign player order
        print('choosing order')
        backend.choose_player_order(brd)

        for index, player in enumerate(brd.list_of_players):
            print('index:', index, 'Player:', player.name, 'first player', player.first_player, 'position on board', player.position_on_board)
        # cont = int(input('cont?'))
        # REMOVING FIRST PLAYER MARK
        for player in brd.list_of_players:
            if player.first_player == True:
                player.first_player = False

        # ONE ROUND
        player_index = 0
        while not brd.all_underlyings_empty():
            player = brd.list_of_players[player_index]
            print()
            print('Player on turn:', player.name)

            player.print_player_table()
            # if brd.round_counter == 2:
                # cont = int(input('cont?'))
            print()
            player.choose_tile(brd)
            print('underlyings', brd.underlyings)
            player.choose_line()
            player.move_all_minus_points()
            player.print_player_table()
            player_index += 1
            if player_index == len(brd.list_of_players):
                player_index = 0

        # COUNTING POINTS AFTER END OF A ROUND
        game_over = False
        for player in brd.list_of_players:
            print('all underlyings empty - end of round. Start counting points..')
            player.print_player_table()
            player.place_all_tiles_to_right(brd)
            player.add_minus_points_to_points_from_round(brd)
            print('After move to right')
            player.print_player_table()

            # check if row of player completed
            if player.row_completed():
                game_over = True
        
        # print of board stats
        print()
        # print('Print all board attributes')
        # brd.print_board_stats()
        print('bag of tiles: ', brd.bag_of_tiles, '(', len(brd.bag_of_tiles), ')')
        print('bag of used tiles: ', brd.bag_of_used_tiles, '(', len(brd.bag_of_used_tiles), ')')
        print()

        if game_over:
            print('GAME ENDS, round', brd.round_counter)
            print('Counting final points for all players')
            for player in brd.list_of_players:
                player.print_player_table()
                player.count_ending_points()
            backend.display_final_score(brd)
            break
        
        # another = int(input('Continue?'))

        brd.round_counter += 1


if __name__ == '__main__':
    main()
