"""
Name: Four in a Row Game
Author: Mihir Patil
UPI: mpat743
Student ID: 384132986

Description:
    This program runs a Four in a Row game. The goal of the
    game is to attain the most points by placing disks to make as many
    sequences of four or more as possible before the board is full.
    Click above each column to insert a disk.

Instructions:
    This program makes use of the pygame library.
    To use this program, pip and pygame must be installed in the Python
    installation
    
    1. Installing pip:
        a. Open Command Prompt
        b. Run command: py -m ensurepip --default-pip
    
    2. Installing pygame:
        a. Open Command Prompt
        b. Run command: py -m pip install pygame
    
    After completing these steps, the game will successfully run

This program is PEP8 Compliant
"""

import pygame
import sys
import math
import ctypes

# Get Screensize
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Colours
blue = (0, 0, 139)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)


class GameBoard:
    def __init__(self, size):
        """
        Construct a GameBoard object, and create a game board with the
        parameter size. Also initialise points for each player and the
        number of entries in each column.
        :param size: int
        """
       
        self.size = size
        self.num_entries = [0] * size
        self.items = [[0] * size for _ in range(size)]
        self.points = [0, 0]
    
    def num_free_positions_in_column(self, column):
        """
        Return the number of free positions in the parameter column.
        :param column: int
        :return: int
        """
        
        return self.size - self.num_entries[column]
    
    def game_over(self):
        """
        Determine when the game is over.
        :return: bool
        """
        
        for column in self.items:
            if column.count(0) > 0:
                return False
        return True
    
    def add(self, column, player):
        """
        Add an 'o' or 'x' into the board depending on the player and if
        the selected column is not full.
        Return True if a slot has been successfully filled and False
        otherwise.
        :param column: int
        :param player: int
        :return: bool
        """
        
        row = self.num_entries[column]
        if row < self.size and self.size > column >= 0:
            self.items[column][row] = player
            self.num_entries[column] += 1
            self.points[player - 1] += self.num_new_points(column, row, player)
            return True
        else:
            return False
    
    def num_new_points(self, column, row, player):
        """
        Determine the number of points attained by placing a disk in
        the parameter position as defined by 'column' and 'row'.
        :param column: int
        :param row: int
        :param player: int
        :return: int
        """
        
        # Impossible to get 4 in a row with a size less than 4.
        if self.size < 4:
            return 0
        
        column_points = 0
        row_points = 0
        diagonal_left_points = 0
        diagonal_right_points = 0
        
        point_check_list = [player] * 4
        column_list = self.items[column]
        row_list = [column[row] for column in self.items]
        
        # Calculate points for rows
        for column1 in range(column - 3, column + 1):
            try:
                if point_check_list == row_list[column1: column1 + 4]:
                    row_points += 1
            except IndexError:
                continue
        
        # Calculate points for columns
        for row1 in range(row - 3, row + 1):
            try:
                if point_check_list == column_list[row1: row1 + 4]:
                    column_points += 1
            except IndexError:
                continue
        
        # Calculate diagonal points
        for offset in range(-3, 1):
            c_index = column + offset
            r_index = row + offset
            r_index_minus = row - offset
            diagonal_left_list = []
            diagonal_right_list = []
            for shift in range(4):
                # Right diagonals
                try:
                    diagonal_right_list.append(self.items[c_index + shift]
                                               [r_index + shift])
                except IndexError:
                    pass
                # Left diagonals
                try:
                    diagonal_left_list.append(self.items[c_index + shift]
                                              [r_index_minus - shift])
                except IndexError:
                    continue
            if point_check_list == diagonal_right_list:
                diagonal_right_points += 1
            if point_check_list == diagonal_left_list:
                diagonal_left_points += 1
        
        return row_points + column_points \
            + diagonal_right_points + diagonal_left_points
    
    def free_slots_as_close_to_middle_as_possible(self):
        """
        Return a list of free slots that are as close to the middle of
        the board as possible
        :return: list
        """
        
        free_slots_list = []
        
        # Even Sized Boards
        if self.size % 2 == 0:
            right_column = int(self.size / 2)
            left_column = right_column - 1
            for shift in range(self.size // 2):
                if self.num_free_positions_in_column(
                        left_column - shift) > 0:
                    free_slots_list.append(left_column - shift)
                if self.num_free_positions_in_column(
                        right_column + shift) > 0:
                    free_slots_list.append(right_column + shift)
        
        # Odd Sized Boards
        else:
            board_middle = self.size // 2
            if self.num_free_positions_in_column(board_middle) > 0:
                free_slots_list.append(board_middle)
            right_column = board_middle + 1
            left_column = board_middle - 1
            for shift in range(self.size // 2):
                if self.num_free_positions_in_column(
                        left_column - shift) > 0:
                    free_slots_list.append(left_column - shift)
                if self.num_free_positions_in_column(
                        right_column + shift) > 0:
                    free_slots_list.append(right_column + shift)
        
        return free_slots_list
    
    def column_resulting_in_max_points(self, player):
        """
        Return the column that results in the parameter player attaining
        the maximum points.
        :param player: int
        :return: int
        """
        
        column_points_list = []
        for column in self.free_slots_as_close_to_middle_as_possible():
            row = self.num_entries[column]
            self.items[column][row] = player
            points = self.num_new_points(column, row, player)
            self.items[column][row] = 0
            column_points_list.append(tuple([column, points]))
        
        return max(column_points_list, key=lambda values: values[-1])


class FourInARow:
    def __init__(self, size):
        """
        Create a FourInARow object and initialise a pygame GUI.
        :param size: int
        """
        
        self.grid_size = 100
        # If window too big, crop to fit screen
        if (size + 1) * self.grid_size > min(screensize):
            size = int((min(screensize) - 100) / self.grid_size)
        # Dimensions and Initializing
        self.board = GameBoard(size)
        self.size = size
        pygame.init()
        pygame.display.set_caption('4 in a Row!')
        self.radius = (self.grid_size / 2 - 5)
        self.width = self.grid_size * size + 260
        self.height = (size + 1) * self.grid_size
        window_size = self.width, self.height
        self.window = pygame.display.set_mode(window_size)
        self.draw_board()
        pygame.display.update()
    
    def draw_board(self):
        """
        Draw the game board in the pygame GUI
        :return:
        """
        
        # Create a blank grid with unfilled circles.
        grid_size = self.grid_size
        for column in range(self.size):
            for row in range(self.size):
                pygame.draw.rect(self.window, blue,
                                 (grid_size * column, grid_size + grid_size
                                  * row, grid_size, grid_size))
                pygame.draw.circle(self.window, black,
                                   (int(column * grid_size + grid_size / 2),
                                    int(row * grid_size + grid_size
                                        + grid_size / 2)), self.radius)
        
        # Add disks for each insertion into a slot.
        for row in range(self.size):
            for column in range(self.size):
               
                # Player disks
                if self.board.items[column][row] == 1:
                    pygame.draw.circle(self.window, red,
                                       (int(column * grid_size
                                            + grid_size / 2), self.height
                                        - (row * grid_size + grid_size / 2)),
                                       self.radius)
                
                # AI disks
                elif self.board.items[column][row] == 2:
                    pygame.draw.circle(self.window, yellow,
                                       (int(column * grid_size
                                            + grid_size / 2), self.height
                                        - int(row * grid_size + grid_size
                                              / 2)), self.radius)
    
    def play(self):
        """
        Allow the user to interact with the game, also allow mouse
        movement and mouse click input.
        :return:
        """
        
        player_number = 0
        win_font = pygame.font.SysFont('monospace', 40)
        full_font = pygame.font.SysFont('monospace', 20)
        
        while not self.board.game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # Draw Selection disk (follows mouse)
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.window, blue,
                                     (0, 0, self.width + 250, self.grid_size))
                    x_position = event.pos[0]
                    if x_position < self.size * self.grid_size:
                        pygame.draw.circle(self.window, red,
                                           (x_position, int(self.grid_size
                                                            / 2)), self.radius)
                    pygame.display.update()
                    
                # insert disk into column
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_number == 0:
                        x_position = event.pos[0]
                        if x_position < self.grid_size * self.size:
                            column = int(
                                math.floor(x_position / self.grid_size))
                            if self.board.add(column, player_number + 1):
                                self.draw_board()
                                pygame.display.update()
                                player_number = (player_number + 1) % 2
                                
                                # Display Player 1 Points
                                pygame.draw.rect(self.window, black,
                                                 (self.grid_size * self.size,
                                                  100, 400, 400))
                                player_point_label = full_font.render(
                                    f'Player 1 Points: {self.board.points[0]}',
                                    True, red)
                                self.window.blit(player_point_label,
                                                 (self.grid_size * self.size
                                                  + 20, 100))
                            
                            # Prompt user that column is full
                            else:
                                column_full_label = \
                                    full_font.render(
                                        f'Column {column + 1} is full'
                                        f', please choose another.',
                                        True, white)
                                self.window.blit(column_full_label, (55, 40))
                                pygame.display.update()
                
                elif player_number == 1:
                    # Choose move which maximises new points for computer
                    # player
                    (best_column, max_points) = \
                        self.board.column_resulting_in_max_points(2)
                    if max_points > 0:
                        column = best_column
                    else:
                        # if no move adds new points choose move which
                        # minimises points opponent player gets
                        (best_column,
                         max_points) = \
                            self.board.column_resulting_in_max_points(1)
                        if max_points > 0:
                            column = best_column
                        else:
                            # if no opponent move creates new points then
                            # choose column as close to middle as possible
                            column = self.board. \
                                free_slots_as_close_to_middle_as_possible()[0]
                    self.board.add(column, player_number + 1)
                    self.draw_board()
                    
                    # Display AI points
                    player_point_label = full_font.render(
                        f'AI Points: {self.board.points[1]}', True, yellow)
                    self.window.blit(player_point_label,
                                     (self.grid_size * self.size + 20, 150))
                    pygame.display.update()
                    player_number = (player_number + 1) % 2
        
        # Display Game End Prompts
        pygame.draw.rect(self.window, blue,
                         (0, 0, self.width, self.grid_size))
        if self.board.points[0] > self.board.points[1]:
            player_win_label = win_font.render("You're the winner!", True, red)
            self.window.blit(player_win_label, (40, 10))
            pygame.display.update()
        elif self.board.points[0] < self.board.points[1]:

            ai_win_label = win_font.render("The AI is the winner!", True,
                                           yellow)
            self.window.blit(ai_win_label, (40, 10))
            pygame.display.update()
        else:
            draw_label = win_font.render("It's a draw!", True, white)
            self.window.blit(draw_label, (40, 10))
            pygame.display.update()
        if self.board.game_over():
            pygame.time.wait(3000)
            

game = FourInARow(6)
game.play()
