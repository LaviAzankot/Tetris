import pygame
from random import choice, randint

# Grid
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
LINE_COLOR = '#FFFFFF'

# Shapes
PURPLE = "#800080"
YELLOW = "#ffd504"
BLUE = "#0441ae"
ORANGE = "#ff971d"
CYAN = "#00ffff"
GREEN = "#72cb3b"
RED = "#ff3215"

SHAPES = {
    'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, 1)], 'color': PURPLE},
    'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': YELLOW},
    'J': {'shape': [(0, 0), (0, -1), (0, 1), (-1, -1)], 'color': BLUE},
    'L': {'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': ORANGE},
    'I': {'shape': [(0, 0), (0, 1), (0, 2), (-1, 2)], 'color': CYAN},
    'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': GREEN},
    'Z': {'shape': [(0, 0), (-1, 0), (0, 1), (1, 1)], 'color': RED},
}

MOVING_DISTANCE_HORIZONTALLY = 40
MOVING_DISTANCE_VERTICALLY = 40

