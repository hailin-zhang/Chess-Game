import pygame


class ChessBoardUI:
    def __init__(self, width, height, board_dimensions, literal_board, game_display, light_color, dark_color):
        self.width = width
        self.height = height
        self.board_dimensions = board_dimensions
        self.literal_board = literal_board
        self.game_display = game_display
        self.light_color = light_color
        self.dark_color = dark_color

    def update_board(self):
        if (self.board_dimensions[0] and self.board_dimensions[1]) > 0:
            for row in range(self.board_dimensions[0]):
                for col in range(self.board_dimensions[1]):
                    # cache current piece
                    curr_piece = self.literal_board[row][col]
                    pygame.draw.rect(self.game_display,
                                     ((self.light_color if (col % 2 == 0) else self.dark_color)  # even columns for even rows
                                      if (row % 2 == 0) else
                                      (self.light_color if (col % 2 == 1) else self.dark_color)),  # odd columns for odd rows
                                     [self.width * col,
                                      self.height * row,
                                      self.width,
                                      self.height])
                    # display the initial board pieces - done robustly for (future) irregular chessboards
                    if curr_piece != 0:
                        # IF the PIECE is BLACK:
                        if curr_piece % 2 == 1:
                            if curr_piece == 3:
                                self.game_display.blit(pygame.image.load("resources/images/blackPawn.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 5:
                                self.game_display.blit(pygame.image.load("resources/images/blackKing.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 7:
                                self.game_display.blit(pygame.image.load("resources/images/blackQueen.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 9:
                                self.game_display.blit(pygame.image.load("resources/images/blackRook.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 11:
                                self.game_display.blit(pygame.image.load("resources/images/blackBishop.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 13:
                                self.game_display.blit(pygame.image.load("resources/images/blackKnight.png"),
                                                  [self.width * col, self.height * row])
                        else:
                            # IF the PIECE is WHITE:
                            if curr_piece == 2:
                                self.game_display.blit(pygame.image.load("resources/images/whitePawn.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 4:
                                self.game_display.blit(pygame.image.load("resources/images/whiteKing.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 6:
                                self.game_display.blit(pygame.image.load("resources/images/whiteQueen.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 8:
                                self.game_display.blit(pygame.image.load("resources/images/whiteRook.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 10:
                                self.game_display.blit(pygame.image.load("resources/images/whiteBishop.png"),
                                                  [self.width * col, self.height * row])
                            elif curr_piece == 12:
                                self.game_display.blit(pygame.image.load("resources/images/whiteKnight.png"),
                                                  [self.width * col, self.height * row])
