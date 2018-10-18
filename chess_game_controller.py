import pygame
import math

from classes.board.chess_board import ChessBoard
from classes.UI.chess_game_UI import ChessBoardUI

# UI constants
DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 800
GRID_WIDTH = 100
GRID_HEIGHT = 100
LIGHT_SHADE = (229, 197, 160)
DARK_SHADE = (158, 124, 85)

# pygame shenanigans
pygame.init()
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

# TODO: make some funky chessboards!
# print the initial board
chessBoardObject = ChessBoard()
board_dimensions = chessBoardObject.get_board().shape  # returns a tuple of (#rows, #cols)
literal_board = chessBoardObject.get_board()
ui_control = ChessBoardUI(GRID_WIDTH, GRID_HEIGHT, board_dimensions, literal_board, game_display, LIGHT_SHADE, DARK_SHADE)
ui_control.update_board()

# loops while running, handle I/O events & logic
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # cache the mouse coordinates
            selected_coords = pygame.mouse.get_pos()
            selected_row = math.floor(selected_coords[0] / GRID_WIDTH)
            selected_col = math.floor(selected_coords[1] / GRID_HEIGHT)
            if literal_board[selected_col][selected_row] != 0:
                chessBoardObject.set_selected_piece(selected_row, selected_col)
                game_display.blit(pygame.image.load("resources/images/selectedOverlay.png"),
                                  [selected_row * GRID_HEIGHT, selected_col * GRID_WIDTH])
        if event.type == pygame.MOUSEBUTTONUP:
            # cache the mouse coordinates
            new_coords = pygame.mouse.get_pos()
            new_row = math.floor(new_coords[0] / GRID_WIDTH)
            new_col = math.floor(new_coords[1] / GRID_HEIGHT)
            # TODO: if legal move:
            chessBoardObject.move_piece((selected_row, selected_col), (new_row, new_col))
            ui_control.update_board()
        elif event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        clock.tick(60)
