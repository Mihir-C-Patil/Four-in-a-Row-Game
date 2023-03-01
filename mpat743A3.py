"""
Assignment 3
Student ID: 384132986
Name: Mihir Patil
Username: mpat743

Description: The Coin Strip Game:
This program is a two player game where there is a row of 9 spaces with
four coins ($) placed randomly on the row.
The game finishes when there are four coins lined up on the left. The
last player to move a coin wins.

RULES:
Two coins cannot share a space, No coin may pass another coin and coins
only move left.

Note: Program is PEP 8 compliant with line wrap at 79 characters and
comment and docstring wrap at 72 characters.
"""

import random


def main():
    display_banner()
    play_game()


def play_game():
    player_num = 1
    game_finished = False
    coins_list = create_coins_list()
    while not game_finished:
        display_coins_list(coins_list)
        print("PLAYER NUMBER: " + str(player_num))
        position_num = get_position_number_from_user()
        if validate_index(coins_list, position_num):
            move_num = get_number_places_to_move()
            if validate_move(coins_list, position_num, move_num):
                move_dollar_to_the_left(coins_list, position_num, move_num)
                game_finished = check_game_finished(coins_list)
                if game_finished:
                    congratulate_player(player_num)
            else:
                print("ERROR: Invalid move!")
        else:
            print("ERROR: Invalid position number!")
        player_num = get_next_player_num(player_num)


def display_banner():
    print('*' * 15)
    print('COIN STRIP GAME')
    print('*' * 15)


def get_position_number_from_user():
    user_position = input('Enter position number of coin: ')
    return int(user_position)


def get_number_places_to_move():
    user_places_to_move = input('Enter number of places to move coin: ')
    return int(user_places_to_move)


def get_next_player_num(player_number):
    if player_number == 1:
        return 2
    return 1


def congratulate_player(player_number):
    print('=' * 29)
    print('** Y O U   H A V E   W O N **')
    print(' ' * 6, 'PLAYER NUMBER:', player_number)
    print('=' * 29)


def display_coins_list(coins_list):
    print('123456789')
    print('-' * 9)
    for element in coins_list:
        print(element, end='')
    print()


def check_game_finished(coins_list):
    game_win_list = ['$', '$', '$', '$']
    if coins_list[:4] == game_win_list:
        return True
    return False


def move_random_character_to_end(coins_list):
    coins_list_len = len(coins_list)
    rand_index = random.randrange(0, coins_list_len)
    rand_char = coins_list[rand_index]
    coins_list.append(rand_char)
    coins_list.pop(rand_index)
    return coins_list


def create_coins_list():
    coins_list = ['-', '$', '-', '$', '-', '$', '-', '$', '-']
    coins_list = move_random_character_to_end(coins_list)
    coins_list = move_random_character_to_end(coins_list)
    coins_list = move_random_character_to_end(coins_list)
    coins_list = move_random_character_to_end(coins_list)
    return coins_list


def validate_move(coins_list, position_number, to_move):
    position_index = position_number - 1
    position_index_new = position_index - to_move
    if position_index_new >= 0:
        if '$' not in coins_list[position_index_new:position_index]:
            return True
    return False


def validate_index(coins_list, position_number):
    position_index = position_number - 1
    if 0 <= position_index <= 8 and coins_list[position_index] == '$':
        return True
    return False


def move_dollar_to_the_left(coins_list, position_number, to_move):
    position_index = position_number - 1
    position_index_new = position_index - to_move
    coins_list[position_index_new] = '$'
    coins_list[position_index] = '-'


main()
