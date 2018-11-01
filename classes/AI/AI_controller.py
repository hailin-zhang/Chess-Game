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
        return self.number_pieces_attacked_and_protected(piece, col, row)

    # Heuristic is based on number of pieces close to enemy King - adopts a mobbing strategy to win game
    def calculate_heuristic_score(self, piece, col, row):
        return 0

    # Note: checkmates only checked for AI moves. Player has to find them themselves!
    def is_checkmate(self):
        return False

    def is_check(self):
        return False

    # Returns [#attacked, #protected]
    def number_pieces_attacked_and_protected(self, piece, col, row):
        attacked = 0
        protected = 0
        # PAWN
        if piece == 2 or piece == 3:
            if piece == 2:
                current_score = self._handle_white_move(row - 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 3:
                current_score = self._handle_black_move(row + 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
        # KING
        elif piece == 4 or piece == 5:
            if piece == 4:
                current_score = self._handle_white_move(row - 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 5:
                current_score = self._handle_black_move(row - 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
        # QUEEN
        elif piece == 6 or piece == 7:
            bishop_score = self._handle_bishop_move(col, row, piece)
            attacked += bishop_score[0]
            protected += bishop_score[1]
            rook_score = self._handle_rook_move(col, row, piece)
            attacked += rook_score[0]
            protected += rook_score[1]
        # ROOK
        elif piece == 8 or piece == 9:
            rook_score = self._handle_rook_move(col, row, piece)
            attacked += rook_score[0]
            protected += rook_score[1]
        # BISHOP
        elif piece == 10 or piece == 11:
            bishop_score = self._handle_bishop_move(col, row, piece)
            attacked += bishop_score[0]
            protected += bishop_score[1]
        # KNIGHT
        elif piece == 12 or piece == 13:
            if piece == 12:
                current_score = self._handle_white_move(row, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 13:
                current_score = self._handle_black_move(row, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
        return [attacked, protected]

    # Returns -1 if protected, 1 if attacked, 0 otherwise
    def _handle_white_move(self, row, col):
        if row > 7 or col > 7 or row < 0 or col < 0:
            return 0
        board = self._board_object.get_board()
        piece = board[row][col]
        if piece != 0 and piece % 2 == 1:
            return 1
        elif piece != 0 and piece % 2 == 0:
            return -1
        else:
            return 0

    # Returns -1 if protected, 1 if attacked, 0 otherwise
    def _handle_black_move(self, row, col):
        if row > 7 or col > 7 or row < 0 or col < 0:
            return 0
        board = self._board_object.get_board()
        piece = board[row][col]
        if piece != 0 and piece % 2 == 0:
            return 1
        elif piece != 0 and piece % 2 == 1:
            return -1
        else:
            return 0

    # Returns [#attacked, #protected]
    def _handle_bishop_move(self, col, row, piece):
        current_score = 0
        attacked = 0
        protected = 0
        board = self._board_object.get_board()
        while board[row+1][col+1]:
            if board[row+1][col+1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row + 1, col + 1)
                elif piece == 9:
                    current_score = self._handle_black_move(row + 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            row += 1
            col += 1
        while board[row+1][col-1]:
            if board[row+1][col-1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row + 1, col - 1)
                elif piece == 9:
                    current_score = self._handle_black_move(row + 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            row += 1
            col -= 1
        while board[row-1][col+1]:
            if board[row-1][col+1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row - 1, col + 1)
                elif piece == 9:
                    current_score = self._handle_black_move(row - 1, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            row -= 1
            col += 1
        while board[row-1][col-1]:
            if board[row-1][col-1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row - 1, col - 1)
                elif piece == 9:
                    current_score = self._handle_black_move(row - 1, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            row -= 1
            col -= 1
        return [attacked, protected]


    # Returns [#attacked, #protected]
    def _handle_rook_move(self, col, row, piece):
        current_score = 0
        attacked = 0
        protected = 0
        board = self._board_object.get_board()
        while board[row][col + 1]:
            if board[row][col + 1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row, col + 1)
                elif piece == 9:
                    current_score = self._handle_black_move(row, col + 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            col += 1
        while board[row + 1][col]:
            if board[row + 1][col] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row + 1, col)
                elif piece == 9:
                    current_score = self._handle_black_move(row + 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            row += 1
        while board[row][col - 1]:
            if board[row][col - 1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row, col - 1)
                elif piece == 9:
                    current_score = self._handle_black_move(row, col - 1)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            col -= 1
        while board[row - 1][col]:
            if board[row - 1][col] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row - 1, col)
                elif piece == 9:
                    current_score = self._handle_black_move(row - 1, col)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            row -= 1
        return [attacked, protected]
