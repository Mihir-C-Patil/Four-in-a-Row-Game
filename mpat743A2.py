"""
Assignment 2
Student ID: 384132986
Name: Mihir Patil
Username: mpat743

Description: The Coin Strip Game:
This program is a two player game where there is a row of 9 spaces with four
coins ($) placed randomly on the row.
The game finishes when there are four coins lined up on the left. The last
player to move a coin wins.

RULES:
Two coins cannot share a space, No coin may pass another coin and coins only
move left.

Note: Program is PEP 8 compliant with line wrap at 80 characters.
"""

import random


def main():
    display_banner()
    play_game()


def play_game():
    player_num = 1
    game_finished = False
    game_string = create_game_string()

    while not game_finished:
        display_game_string(game_string)
        print("PLAYER NUMBER: " + str(player_num))
        position_num = get_position_number_from_user()
        move_num = get_number_places_to_move()
        game_string = move_dollar_to_the_left(game_string, position_num,
                                              move_num)
        game_finished = check_game_finished(game_string)

        if game_finished:
            congratulate_player(player_num)
        else:
            player_num = get_next_player_num(player_num)


def display_banner():
    game_title = 'COIN STRIP GAME'
    star_border = '*' * len(game_title)
    print()
    print(star_border)
    print(game_title)
    print(star_border)


def get_position_number_from_user():
    position_num = int(input('Enter position number of coin: '))

    return position_num


def get_number_places_to_move():
    places_to_move = int(input('Enter number of places to move coin: '))

    return places_to_move


def create_game_string():
    initial_string = ' $ $ $ $ '
    game_string = move_random_character_to_end(initial_string)
    game_string = move_random_character_to_end(game_string)
    game_string = move_random_character_to_end(game_string)
    game_string = move_random_character_to_end(game_string)

    return game_string


def move_random_character_to_end(game_string):
    rand_char_index = random.randrange(0, len(game_string))
    rand_char_remove_and_add = game_string[rand_char_index]
    game_string = (game_string[0:rand_char_index]
                   + game_string[rand_char_index + 1:]
                   + rand_char_remove_and_add)

    return game_string


def display_game_string(game_string):
    print()
    print('123456789')
    print('-' * 9)
    print(game_string)
    print()


def get_next_player_num(player_number):
    if player_number == 1:
        return 2
    else:
        return 1


def move_dollar_to_the_left(game_string, position_number, to_move):
    position_number -= 1
    char_to_remove_and_add = game_string[position_number]
    char_move_index = position_number - to_move
    game_string = (game_string[0:char_move_index] + char_to_remove_and_add
                   + game_string[char_move_index:position_number]
                   + game_string[position_number + 1:])

    return game_string


def check_game_finished(game_string):
    if game_string[0:4] == '$$$$':
        return True
    else:
        return False


def congratulate_player(player_number):
    game_win_message = '** Y O U   H A V E   W O N **'
    game_win_border = '=' * 29
    print()
    print(game_win_border)
    print(game_win_message)
    print('       PLAYER NUMBER:', player_number)
    print(game_win_border)
    print()


main()
