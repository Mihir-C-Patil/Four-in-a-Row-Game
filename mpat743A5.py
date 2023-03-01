"""
Aim: This program prints a pattern consisting of two coloured rectangles
in a new window according to a users pattern choice.
Author: Mihir Patil
Username: mpat743
This program is fully PEP 8 compliant
"""

from tkinter import *


def main():
    colours = ['gray', 'orange', 'teal', 'turquoise', 'brown', 'darkseagreen',
               'purple', 'lavender', 'magenta']
    pattern_dictionary = create_pattern_dictionary(colours)
    size = 50
    canvas_width = canvas_height = size * 5
    window = Tk()
    window.title("A5 by mpat743")
    geometry_string = str(canvas_width) + "x" + str(canvas_height) + "+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand=True)
    pattern_number = get_pattern_number()
    values = pattern_dictionary[pattern_number]
    draw_pattern(a_canvas, size, size, values[0], values[1], values[2], size)
    window.mainloop()  # Added for compatibility with third-party IDEs


def get_pattern_number():
    user_number = int(input('Enter a number (0-8): '))
    while not 0 <= user_number <= 8:
        user_number = int(input('Enter a number (0-8): '))
    return user_number


def draw_pattern(a_canvas, x, y, row_number, col_number, colour, size):
    x_start = x + (size * col_number)
    y_start = y + (size * row_number)
    length = 3 * size
    x_end = x_start + size
    y_end = y_start + size
    a_canvas.create_rectangle(x, y_start, x + length, y_end, fill=colour)
    a_canvas.create_rectangle(x_start, y, x_end, y + length, fill=colour)


def create_pattern_dictionary(colours):
    pattern_dictionary = {}
    column = 0
    row = 0
    for index in range(9):
        pattern_dictionary[index] = (row, column, colours[index])
        if column == 2:
            row += 1
            column = 0
        else:
            column += 1
    return pattern_dictionary


main()
