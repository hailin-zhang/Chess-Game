import pygame

from classes.board.chess_board import ChessBoard

# UI constants
DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 800
GRID_WIDTH = 100
GRID_HEIGHT = 100
LIGHT_SHADE = (229, 197, 160)
DARK_SHADE = (158, 124, 85)

# pygame shenanigans
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

# TODO: make some funky chessboards!
# print the initial board
chessBoardObject = ChessBoard()
board_dimensions = chessBoardObject.get_board().shape  # returns a tuple of (#rows, #cols)=
if (board_dimensions[0] and board_dimensions[1]) > 0:
    # want to keep chess board data structure private
    literal_board = chessBoardObject.get_board()
    curr_piece = 0
    for row in range(board_dimensions[0]):
        for col in range(board_dimensions[1]):
            # cache current piece
            curr_piece = literal_board[row][col]
            pygame.draw.rect(gameDisplay,
                             ((LIGHT_SHADE if (col % 2 == 0) else DARK_SHADE)  # even columns for even rows
                              if (row % 2 == 0) else
                              (LIGHT_SHADE if (col % 2 == 1) else DARK_SHADE)),  # odd columns for odd rows
                             [GRID_WIDTH * col,
                              GRID_HEIGHT * row,
                              GRID_WIDTH,
                              GRID_HEIGHT])
            # display the initial board pieces - done robustly for future irregular chessboards
            if curr_piece != 0:
                # IF the PIECE is BLACK:
                if curr_piece % 2 == 1:
                    if curr_piece == 3:
                        gameDisplay.blit(pygame.image.load("resources/images/blackPawn.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 5:
                        gameDisplay.blit(pygame.image.load("resources/images/blackKing.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 7:
                        gameDisplay.blit(pygame.image.load("resources/images/blackQueen.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 9:
                        gameDisplay.blit(pygame.image.load("resources/images/blackRook.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 11:
                        gameDisplay.blit(pygame.image.load("resources/images/blackBishop.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 13:
                        gameDisplay.blit(pygame.image.load("resources/images/blackKnight.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                else:
                    # IF the PIECE is WHITE:
                    if curr_piece == 2:
                        gameDisplay.blit(pygame.image.load("resources/images/whitePawn.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 4:
                        gameDisplay.blit(pygame.image.load("resources/images/whiteKing.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 6:
                        gameDisplay.blit(pygame.image.load("resources/images/whiteQueen.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 8:
                        gameDisplay.blit(pygame.image.load("resources/images/whiteRook.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 10:
                        gameDisplay.blit(pygame.image.load("resources/images/whiteBishop.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])
                    if curr_piece == 12:
                        gameDisplay.blit(pygame.image.load("resources/images/whiteKnight.png"),
                                         [GRID_WIDTH * col, GRID_HEIGHT * row])

# loops while running, handle I/O events & logic
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        clock.tick(60)
