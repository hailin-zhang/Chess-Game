import numpy

# if PIECE is ODD, PIECE is BLACK; otherwise WHITE
BLACK_MASK = 1

# A chess board:
# PIECES:
EMPTY  = 0   # 0b0
PAWN   = 2   # 0b10
KING   = 4   # 0b100
QUEEN  = 6   # 0b110
ROOK   = 8   # 0b1000
BISHOP = 10  # 0b1010
KNIGHT = 12  # 0b1100


class ChessBoard:
    def __init__(self):
        # Sets logic on board to initial locations: BLACK PIECES are ODD (i.e. BLACK_MASK)
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
        self._currently_selected = None

    def get_board(self):
        return self._board

    # TODO: for branch prediction in parallel in AI
    def set_selected_piece(self, row, col):
        self._currently_selected = self._board[row][col]

    def move_piece(self, old_coords, new_coords):
        old_piece = self._board[old_coords[1]][old_coords[0]]
        self._board[old_coords[1]][old_coords[0]] = 0
        self._board[new_coords[1]][new_coords[0]] = old_piece
