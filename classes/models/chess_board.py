import numpy

# if PIECE is ODD, PIECE is BLACK; otherwise WHITE
BLACK_MASK = 1

# PIECES:
EMPTY = 0  # 0b0
PAWN = 2  # 0b10
KING = 4  # 0b100
QUEEN = 6  # 0b110
ROOK = 8  # 0b1000
BISHOP = 10  # 0b1010
KNIGHT = 12  # 0b1100


class ChessBoard:
    def __init__(self):
        # Sets pieces to initial locations: BLACK PIECES are ODD (i.e. BLACK_MASK)
        self._board = numpy.array([[ROOK + BLACK_MASK, KNIGHT + BLACK_MASK, BISHOP + BLACK_MASK, QUEEN + BLACK_MASK,
                                    KING + BLACK_MASK, BISHOP + BLACK_MASK, KNIGHT + BLACK_MASK, ROOK + BLACK_MASK],
                                   [PAWN + BLACK_MASK, PAWN + BLACK_MASK, PAWN + BLACK_MASK, PAWN + BLACK_MASK,
                                    PAWN + BLACK_MASK, PAWN + BLACK_MASK, PAWN + BLACK_MASK, PAWN + BLACK_MASK],
                                   [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                                   [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                                   [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                                   [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                                   # WHITE PIECES are EVEN
                                   [PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN],
                                   [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]])
        # Initial structure for attacked/protected pieces:
        # 0 is not attacked or protected
        # ATTACK MASK is 0b0010
        # 2 - 0b0010 is attacked by WHITE
        # 3 - 0b0011 is attacked by BLACK
        # DEFENSE MASK is 0b0100
        # 4 - 0b0100 is protected by WHITE
        # 5 - 0b0101 is protected by BLACK
        # BLACK MASK is 0b0001
        self._strategy_board = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [2, 2, 2, 2, 2, 2, 2, 2],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [2, 2, 2, 2, 2, 2, 2, 2],
                                            [0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0]])
        self._currently_selected = None

    def get_board(self):
        return self._board

    # TODO: for branch prediction in parallel in AI
    def set_selected_piece(self, row, col):
        self._currently_selected = self._board[row][col]

    # REQUIRES: piece moved is a valid piece (i.e. not EMPTY)
    # RETURNS: 1 if moved to KING, 0 OTHERWISE (i.e. normal move)
    def move_piece(self, old_coords, new_coords):
        new_piece = self._board[new_coords[1], new_coords[0]]
        old_col = old_coords[0]
        old_row = old_coords[1]
        old_piece = self._board[old_row][old_col]
        self._board[old_row][old_col] = 0
        self._board[new_coords[1]][new_coords[0]] = old_piece
        if new_piece == KING or new_piece == KING + BLACK_MASK:
            return 1
        else:
            return 0


    # TODO: make robust ? ? ?  or not
    def white_castle_right(self):
        self._board[7][4] = 0
        self._board[7][6] = 4
        self._board[7][7] = 0
        self._board[7][5] = 8


    def white_castle_left(self):
        self._board[7][4] = 0
        self._board[7][2] = 4
        self._board[7][0] = 0
        self._board[7][3] = 8


    def black_castle_right(self):
        self._board[0][4] = 0
        self._board[0][6] = 5
        self._board[0][7] = 0
        self._board[0][5] = 9


    def black_castle_left(self):
        self._board[0][4] = 0
        self._board[0][2] = 5
        self._board[0][0] = 0
        self._board[0][3] = 9
