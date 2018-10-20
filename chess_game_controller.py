import pygame
import math

from classes.models.chess_board import ChessBoard
from classes.UI.chess_game_UI import ChessBoardUI
from classes.logic.chess_logic import ChessLogic

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
pygame.display.set_caption("Chess - Hai Lin Zhang V1.0.0")
clock = pygame.time.Clock()
on_move_sound = pygame.mixer.Sound("resources/sounds/onMove.wav")
on_castle_sound = pygame.mixer.Sound("resources/sounds/onCastle.wav")
on_error_sound = pygame.mixer.Sound("resources/sounds/onError.wav")

# TODO: make some funky chessboards!
# print the initial models
chessBoardObject = ChessBoard()
board_dimensions = chessBoardObject.get_board().shape  # returns a tuple of (#rows, #cols)
literal_board = chessBoardObject.get_board()
UI_control = ChessBoardUI(GRID_WIDTH, GRID_HEIGHT, board_dimensions, literal_board, game_display, LIGHT_SHADE,
                          DARK_SHADE)
UI_control.update_board()

logic_control = ChessLogic()
# loops while running, handle I/O events & logic
is_whites_turn = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # cache the mouse coordinates
            selected_coords = pygame.mouse.get_pos()
            selected_col = math.floor(selected_coords[0] / GRID_WIDTH)
            selected_row = math.floor(selected_coords[1] / GRID_HEIGHT)
            # print(math.floor(selected_coords[0] / GRID_WIDTH),  math.floor(selected_coords[1] / GRID_HEIGHT))
            current_piece = literal_board[selected_row][selected_col]
            if is_whites_turn and current_piece % 2 == 0 or not is_whites_turn and current_piece % 2 == 1:
                if not (current_piece == 0 or current_piece == 14):
                    chessBoardObject.set_selected_piece(selected_row, selected_col)
                    game_display.blit(pygame.image.load("resources/images/selectedOverlay.png"),
                                      [selected_col * GRID_WIDTH, selected_row * GRID_HEIGHT])
            else:
                game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                  [selected_col * GRID_WIDTH, selected_row * GRID_HEIGHT])
                on_error_sound.play()
        if event.type == pygame.MOUSEBUTTONUP:
            # cache the mouse coordinates
            new_coords = pygame.mouse.get_pos()
            new_col = math.floor(new_coords[0] / GRID_WIDTH)
            new_row = math.floor(new_coords[1] / GRID_HEIGHT)
            if logic_control.is_valid_move(literal_board,
                                           board_dimensions,
                                           (selected_col, selected_row),
                                           (new_col, new_row)) \
                    and (
                    (is_whites_turn and current_piece % 2 == 0) or (not is_whites_turn and current_piece % 2 == 1)):
                chessBoardObject.move_piece((selected_col, selected_row), (new_col, new_row))
                on_move_sound.play()
                # change PAWN to QUEEN! Note to self: consider refactoring this into piece_logic
                if current_piece == 2 and new_row == 0:
                    literal_board[new_row][new_col] = 6
                elif current_piece == 3 and new_row == board_dimensions[1]-1:
                    literal_board[new_row][new_col] = 7
                # if KING or ROOK moves, cannot castle anymore!
                elif current_piece == 4 or current_piece == 5 or current_piece == 8 or current_piece == 9:
                    logic_control.cannot_castle(current_piece, board_dimensions, selected_col)
                is_whites_turn = not is_whites_turn
                UI_control.update_board()
            # castling
            elif current_piece == 4 and ((is_whites_turn and current_piece % 2 == 0) or
                    (not is_whites_turn and current_piece % 2 == 1)):
                if new_col == selected_col + 2 and new_row == selected_row and logic_control.white_can_castle_right:
                    if logic_control.free_to_castle(selected_col, new_col, new_row, literal_board):
                        chessBoardObject.white_castle_right()
                        on_castle_sound.play()
                        logic_control.castled_white()
                        is_whites_turn = not is_whites_turn
                        UI_control.update_board()
                    else:
                        UI_control.update_board()
                        game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                          [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                        on_error_sound.play()
                elif new_col == selected_col - 2 and new_row == selected_row and logic_control.white_can_castle_left:
                    if logic_control.free_to_castle(selected_col, new_col, new_row, literal_board):
                        chessBoardObject.white_castle_left()
                        on_castle_sound.play()
                        logic_control.castled_white()
                        is_whites_turn = not is_whites_turn
                        UI_control.update_board()
                    else:
                        UI_control.update_board()
                        game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                          [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                        on_error_sound.play()
                else:
                    UI_control.update_board()
                    game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                      [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                    on_error_sound.play()
            elif current_piece == 5 and ((is_whites_turn and current_piece % 2 == 0) or
                    (not is_whites_turn and current_piece % 2 == 1)):
                if new_col == selected_col + 2 and new_row == selected_row and logic_control.black_can_castle_right:
                    if logic_control.free_to_castle(selected_col, new_col, new_row, literal_board):
                        chessBoardObject.black_castle_right()
                        on_castle_sound.play()
                        logic_control.castled_black()
                        is_whites_turn = not is_whites_turn
                        UI_control.update_board()
                    else:
                        UI_control.update_board()
                        game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                          [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                        on_error_sound.play()
                elif new_col == selected_col - 2 and new_row == selected_row and logic_control.black_can_castle_left:
                    if logic_control.free_to_castle(selected_col, new_col, new_row, literal_board):
                        chessBoardObject.black_castle_left()
                        on_castle_sound.play()
                        logic_control.castled_black()
                        is_whites_turn = not is_whites_turn
                        UI_control.update_board()
                    else:
                        UI_control.update_board()
                        game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                          [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                        on_error_sound.play()
                else:
                    UI_control.update_board()
                    game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                      [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                    on_error_sound.play()
            else:
                UI_control.update_board()
                game_display.blit(pygame.image.load("resources/images/invalidOverlay.png"),
                                  [new_col * GRID_WIDTH, new_row * GRID_HEIGHT])
                on_error_sound.play()
        elif event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        clock.tick(60)
