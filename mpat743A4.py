"""
Assignment 4
Name: Mihir Patil
Username: mpat743
Description:
                          Word Guessing Game!
The aim of this game is to guess a given word. You enter a letter to see
if it is in the word, if it is, that letter is revealed. The game ends
when you have fully guessed the word!
This program is PEP 8 compliant.
"""

# import random (not importing as per instructions)
# random.seed(70) (not importing as per instructions)


def main():
    display_banner()
    play_game()


def play_game():
    game_finished = False
    words_list = get_words_from_file('words1.txt')
    words_dictionary = build_dictionary(words_list)
    level = int(input('Enter the number of letters in the guessing word: '))
    generated_word = get_word(words_dictionary[level])
    encrypted_list = get_encrypted_list(generated_word)
    while not game_finished:
        display_word(encrypted_list)
        letter = input('Enter a letter: ')
        check_guess(generated_word, encrypted_list, letter)
        game_finished = check_game_finished(encrypted_list)
        if game_finished:
            congratulate(generated_word)


def display_banner():
    game_title_length = len('WORD GUESSING GAME')
    print('*' * game_title_length)
    print('WORD GUESSING GAME')
    print('*' * game_title_length)


def congratulate(generated_word):
    print('GUESS THE WORD:', generated_word)
    congratulate_message_length = len('** W E L L   D O N E **')
    print('=' * congratulate_message_length)
    print('** W E L L   D O N E **')
    print('=' * congratulate_message_length)


def get_words_from_file(filename):
    words_file_input = open(filename, 'r')
    words_input = words_file_input.read()
    words_file_input.close()
    words_input_list = words_input.split()
    return words_input_list


def build_dictionary(words_list):
    words_dictionary = {}
    for index in range(len(words_list)):
        words_list[index] = words_list[index].lower()
    for word in sorted(words_list):
        key = len(word)
        words_dictionary[key] = []
    for word in sorted(words_list):
        key = len(word)
        words_dictionary[key].append(word)
    return words_dictionary


def get_word(words_list):
    random_index = random.randrange(len(words_list))
    random_word = words_list[random_index]
    return random_word


def get_encrypted_list(word):
    word_length = len(word)
    character_list = list(word)
    for index in range(1, word_length):
        character_list[index] = '*'
    return character_list


def display_word(encrypted_list):
    word = ''
    for character in encrypted_list:
        word += character
    print('GUESS THE WORD:', word)


def check_guess(generated_word, encrypted_list, letter):
    word_list = list(generated_word)
    for index in range((len(word_list))):
        if letter == word_list[index]:
            encrypted_list[index] = letter
    return encrypted_list


def check_game_finished(encrypted_list):
    if '*' not in encrypted_list:
        return True
    return False
