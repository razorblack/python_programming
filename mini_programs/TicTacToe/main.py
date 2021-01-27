import pygame
import sys
import numpy as np

pygame.init()

# Dimension of screen
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

# Colors
BACKGROUND = (28, 170, 156)
LINE_COLOR = (90, 90, 90)

# Board
board = np.zeros((3, 3))
print(board)

# Show screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BACKGROUND)


# Figure of X's and O's
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 2:
                pass

# Draw Lines on screen
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # Vertical Lines
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False

    return True


# Draw lines on screen
draw_lines()
# Setting first player to play
player = 1

# Game Loop
while True:
    for event in pygame.event.get():
        # Exit
        if event.type == pygame.QUIT:
            sys.exit()

        # Click on board
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clickedRow = int(mouseY // 200)
            clickedCol = int(mouseX // 200)

            if available_square(clickedRow, clickedCol):
                if player == 1:
                    mark_square(clickedRow, clickedCol, 1)
                    player = 2

                elif player == 2:
                    mark_square(clickedRow, clickedCol, player)
                    player = 1
    pygame.display.update()