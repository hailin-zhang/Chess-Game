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

# MOVED PIECE (for castling, pawn 1st move), FINAL and EQUIVALENT TO 0:
MOVED_PAWN = 14
MOVED_ROOK = 15
MOVED_KING = 16


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
        # Initial structure for attacked pieces:
        # 0 is not attacked
        # 1 is attacked by WHITE
        # 2 is attacked by BLACK
        # 3 is protected by WHITE
        # 4 is protected by BLACK
        self._attacked_board = numpy.array([[0, 0, 0, 0, 0, 0, 0, 0],
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
    # TODO: CASTLING, HANDLE 1ST MOVES
    def move_piece(self, old_coords, new_coords):
        old_col = old_coords[0]
        old_row = old_coords[1]
        old_piece = self._board[old_row][old_col]
        self._board[old_row][old_col] = 0
        self._board[new_coords[1]][new_coords[0]] = old_piece
