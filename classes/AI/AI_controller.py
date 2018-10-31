from classes.logic.chess_logic import ChessLogic
from classes.models.chess_board import ChessBoard


class VanillaBoardAI:
    def __init__(self):
        self._board_object = ChessBoard()
        self._board_logic = ChessLogic()
        self.turns = 1
        self.random_chance = 0.35  # ** ((self.turns + 9)/ 10)

    # needs best score between current location, new location(s)
    def calculate_score(self, piece, new_col, new_row):
        return self.calculate_attacks_and_protects_score(piece, new_col, new_row) \
               + self.calculate_heuristic_score(piece, new_col, new_row)

    def calculate_attacks_and_protects_score(self, piece, col, row):
        return self.number_pieces_attacked(piece, col, row) + self.number_pieces_protected(piece, col, row)

    # Heuristic is based on number of pieces close to enemy King - adopts a mobbing strategy to win game
    def calculate_heuristic_score(self, piece, col, row):
        return 0

    # Note: checkmates only checked for AI moves. Player has to find them themselves!
    def is_checkmate(self):
        return False

    def is_check(self):
        return False

    # Note: only considers pieces in close vicinity / attacking range of the piece!
    def number_pieces_attacked(self, piece, col, row):
        attacked = 0
        # PAWN
        if piece == 2 or piece == 3:
            if piece == 2:
                if self.is_black_piece(row-1, col+1):
                    attacked += 1
                if self.is_black_piece(row-1, col-1):
                    attacked += 1
            elif piece == 3:
                if self.is_white_piece(row+1, col+1):
                    attacked += 1
                if self.is_white_piece(row+1, col-1):
                    attacked += 1
        # KING
        elif piece == 4 or piece == 5:
            # TODO: finish attacking logic, do protecting
            if piece == 4:
                if self.is_black_piece(row-1, col-1):
                    attacked += 1
                if self.is_black_piece(row-1, col):
                    attacked += 1
                if self.is_black_piece(row-1, col+1):
                    attacked += 1
                if self.is_black_piece(row, col-1):
                    attacked += 1
                if self.is_black_piece(row, col+1):
                    attacked += 1
                if self.is_black_piece(row+1, col-1):
                    attacked += 1
                if self.is_black_piece(row+1, col):
                    attacked += 1
                if self.is_black_piece(row+1, col+1):
                    attacked += 1
            elif piece == 5:
                if self.is_white_piece(row-1, col-1):
                    attacked += 1
                if self.is_white_piece(row-1, col):
                    attacked += 1
                if self.is_white_piece(row-1, col+1):
                    attacked += 1
                if self.is_white_piece(row, col-1):
                    attacked += 1
                if self.is_white_piece(row, col+1):
                    attacked += 1
                if self.is_white_piece(row+1, col-1):
                    attacked += 1
                if self.is_white_piece(row+1, col):
                    attacked += 1
                if self.is_white_piece(row+1, col+1):
                    attacked += 1
        # QUEEN
        elif piece == 6 or piece == 7:
            if piece == 6:
                return self._bishop_attacks(col, row) + self._rook_attacks(col, row)

        return attacked

    def number_pieces_protected(self, piece, col, row):
        return 0

    # False if out of bounds
    def is_black_piece(self, row, col):
        if row > 7 or col > 7 or row < 0 or col < 0:
            return False
        board = self._board_object.get_board()
        piece = board[row][col]
        return piece != 0 and piece % 2 == 1

    # False if out of bounds
    def is_white_piece(self, row, col):
        if row > 7 or col > 7 or row < 0 or col < 0:
            return False
        board = self._board_object.get_board()
        piece = board[row][col]
        return piece != 0 and piece % 2 == 0
