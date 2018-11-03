from classes.logic.chess_logic import ChessLogic
from classes.models.chess_board import ChessBoard


class VanillaBoardAI:
    def __init__(self):
        self._board_object = ChessBoard()
        self._board_logic = ChessLogic()
        self.turns = 1
        self.random_chance = 0.35  # ** ((self.turns + 9)/ 10)
        print(self.number_pieces_attacked_and_protected(10, 3, 3))
        print(self.number_pieces_attacked_and_protected(10, 0, 0))
        print(self.number_pieces_attacked_and_protected(10, 7, 7))
        print(self.number_pieces_attacked_and_protected(10, 3, 2))
        print(self.number_pieces_attacked_and_protected(10, 3, 6))
        print(self.number_pieces_attacked_and_protected(10, 10, 0))
        print(self.number_pieces_attacked_and_protected(10, 0, -1))

    # needs best score between current location, new location(s)
    def calculate_score(self, piece, new_col, new_row):

        return self.calculate_attacks_and_protects_score(piece, new_col, new_row) \
               + self.calculate_heuristic_score(piece, new_col, new_row)

    def calculate_attacks_and_protects_score(self, piece, col, row):
        attack_protect_scores = self.number_pieces_attacked_and_protected(piece, col, row)
        return attack_protect_scores[0] + attack_protect_scores[1]

    # Heuristic based on (simply) proximity to king, a consideration for the future is to change as game progresses
    def calculate_heuristic_score(self, piece, new_col, new_row):
        board = self._board_object.get_board()
        for col in range(7, 0, -1):
            for row in range(7, 0, -1):
                if board[row, col] == 4:
                    king_row = row
                    king_col = col
                    return king_row - new_row + king_col - new_col

    # Note: checkmates only checked for AI moves. Player has to find them themselves!
    def is_checkmate(self):
        return False

    def is_check(self):
        return False

    # Returns [#attacked, #protected]
    def number_pieces_attacked_and_protected(self, piece, col, row):
        board = self._board_object.get_board()
        if col > 7 or col < 0 or row > 7 or row < 0:
            return [0, 0]
        attacked = 0
        protected = 0
        # PAWN
        if piece == 2 or piece == 3:
            if piece == 2:
                current_score = self._handle_white_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 3:
                current_score = self._handle_black_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
        # KING
        elif piece == 4 or piece == 5:
            if piece == 4:
                current_score = self._handle_white_move(row - 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 5:
                current_score = self._handle_black_move(row - 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
        # QUEEN
        elif piece == 6 or piece == 7:
            bishop_score = self._handle_bishop_move(col, row, piece, board)
            attacked += bishop_score[0]
            protected += bishop_score[1]
            rook_score = self._handle_rook_move(col, row, piece, board)
            attacked += rook_score[0]
            protected += rook_score[1]
        # ROOK
        elif piece == 8 or piece == 9:
            rook_score = self._handle_rook_move(col, row, piece, board)
            attacked += rook_score[0]
            protected += rook_score[1]
        # BISHOP
        elif piece == 10 or piece == 11:
            bishop_score = self._handle_bishop_move(col, row, piece, board)
            attacked += bishop_score[0]
            protected += bishop_score[1]
        # KNIGHT
        elif piece == 12 or piece == 13:
            if piece == 12:
                current_score = self._handle_white_move(row, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 13:
                current_score = self._handle_black_move(row, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
        return [attacked, protected]

    # Returns -1 if protected, 1 if attacked, 0 otherwise
    @staticmethod
    def _handle_white_move(row, col, board):
        if row > 7 or col > 7 or row < 0 or col < 0:
            return 0
        piece = board[row][col]
        if piece != 0 and piece % 2 == 1:
            return 1
        elif piece != 0 and piece % 2 == 0:
            return -1
        else:
            return 0

    # Returns -1 if protected, 1 if attacked, 0 otherwise
    @staticmethod
    def _handle_black_move(row, col, board):
        if row > 7 or col > 7 or row < 0 or col < 0:
            return 0
        piece = board[row][col]
        if piece != 0 and piece % 2 == 0:
            return 1
        elif piece != 0 and piece % 2 == 1:
            return -1
        else:
            return 0

    # Returns [#attacked, #protected]
    def _handle_bishop_move(self, col, row, piece, board):
        orig_row = row
        orig_col = col
        current_score = 0
        attacked = 0
        protected = 0
        while col+1 < 8 and row+1 < 8:
            if board[row + 1][col + 1] != 0:
                if piece == 10:
                    current_score = self._handle_white_move(row + 1, col + 1, board)
                elif piece == 11:
                    current_score = self._handle_black_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        row = orig_row
                        col = orig_col
                        break
                    else:
                        protected += 1
                        row = orig_row
                        col = orig_col
                        break
            row += 1
            col += 1
        while row+1 < 8 and col-1 > 0:
            if board[row + 1][col - 1] != 0:
                if piece == 10:
                    current_score = self._handle_white_move(row + 1, col - 1, board)
                elif piece == 11:
                    current_score = self._handle_black_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        row = orig_row
                        col = orig_col
                        break
                    else:
                        protected += 1
                        row = orig_row
                        col = orig_col
                        break
            row += 1
            col -= 1
        while row-1>0 and col+1 < 8:
            if board[row - 1][col + 1] != 0:
                if piece == 10:
                    current_score = self._handle_white_move(row - 1, col + 1, board)
                elif piece == 11:
                    current_score = self._handle_black_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        row = orig_row
                        col = orig_col
                        break
                    else:
                        protected += 1
                        row = orig_row
                        col = orig_col
                        break
            row -= 1
            col += 1
        while row-1 > 0 and col-1 > 0 :
            if board[row - 1][col - 1] != 0:
                if piece == 10:
                    current_score = self._handle_white_move(row - 1, col - 1, board)
                elif piece == 11:
                    current_score = self._handle_black_move(row - 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            row -= 1
            col -= 1
        return [attacked, protected]

    # Returns [#attacked, #protected]
    def _handle_rook_move(self, col, row, piece, board):
        orig_row = row
        orig_col = col
        current_score = 0
        attacked = 0
        protected = 0
        while col + 1 < 8:
            if board[row][col + 1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row, col + 1, board)
                elif piece == 9:
                    current_score = self._handle_black_move(row, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        row = orig_row
                        col = orig_col
                        break
                    else:
                        protected += 1
                        row = orig_row
                        col = orig_col
                        break
            col += 1
        while row + 1 < 8:
            if board[row + 1][col] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row + 1, col, board)
                elif piece == 9:
                    current_score = self._handle_black_move(row + 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        row = orig_row
                        col = orig_col
                        break
                    else:
                        protected += 1
                        row = orig_row
                        col = orig_col
                        break
            row += 1
        while col - 1 > 0:
            if board[row][col - 1] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row, col - 1, board)
                elif piece == 9:
                    current_score = self._handle_black_move(row, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        row = orig_row
                        col = orig_col
                        break
                    else:
                        protected += 1
                        row = orig_row
                        col = orig_col
                        break
            col -= 1
        while row - 1 > 0:
            if board[row - 1][col] != 0:
                if piece == 8:
                    current_score = self._handle_white_move(row - 1, col, board)
                elif piece == 9:
                    current_score = self._handle_black_move(row - 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            row -= 1
        return [attacked, protected]
