from classes.logic.chess_logic import ChessLogic
from classes.models.chess_board import ChessBoard


class VanillaBoardAI:
    def __init__(self):
        self._board_object = ChessBoard()
        self._board_logic = ChessLogic()
        self.turns = 1
        self.random_chance = 0.35  # ** ((self.turns + 9)/ 10)

    def get_best_move(self):
        best_score = 0
        # [piece, old_row, old_col, new_row, new_col]
        best_move = [0, -1, -1, -1, -1]
        board = self._board_object.get_board()
        # iterate across entire board, finding all black pieces
        for row in range(0, 8):
            for col in range(0, 8):
                current_piece = board[row][col]
                # if black piece found, iterate across all possible board states -> enqueue score
                if current_piece != 0 and current_piece % 2 == 1:
                    # PAWN
                    if current_piece == 3:
                        for sub_col in range(col - 1, col + 2):
                            if self._board_logic.is_valid_move(board, [8, 8],
                                                               [col, row], [sub_col, row + 2]):
                                current_score = self.calculate_score(current_piece, sub_col, row + 2, board)
                                if current_score > best_score:
                                    best_score = current_score
                                    best_move = [3, row, col, row + 2, sub_col]
                            if self._board_logic.is_valid_move(board, [8, 8],
                                                               [col, row], [sub_col, row + 1]):
                                current_score = self.calculate_score(current_piece, sub_col, row + 1, board)
                                if current_score > best_score:
                                    best_score = current_score
                                    best_move = [3, row, col, row + 1, sub_col]
                    # KING
                    elif current_piece == 5:
                        for sub_col in range(col - 1, col + 2):
                            if self._board_logic.is_valid_move(board, [8, 8],
                                                               [col, row], [sub_col, row - 1]):
                                current_score = self.calculate_score(current_piece, sub_col, row - 1, board)
                                if current_score > best_score:
                                    best_score = current_score
                                    best_move = [5, row, col, row - 1, sub_col]
                        for sub_col in range(col - 1, col + 2):
                            if self._board_logic.is_valid_move(board, [8, 8],
                                                               [col, row], [sub_col, row + 1]):
                                current_score = self.calculate_score(current_piece, sub_col, row + 1, board)
                                if current_score > best_score:
                                    best_score = current_score
                                    best_move = [5, row, col, row + 1, sub_col]
                        if self._board_logic.is_valid_move(board, [8, 8],
                                                           [col, row], [col - 1, row]):
                            current_score = self.calculate_score(current_piece, col - 1, row, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [5, row, col, row, col - 1]
                        if self._board_logic.is_valid_move(board, [8, 8],
                                                           [col, row], [col + 1, row]):
                            current_score = self.calculate_score(current_piece, col + 1, row, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [5, row, col, row, col + 1]
                    # QUEEN
                    elif current_piece == 7:
                        rook_score = self._get_rook_score(board, row, col, best_score, 7)
                        if rook_score != 0:
                            best_score = rook_score[0]
                            best_move = [7, row, col, rook_score[1], rook_score[2]]
                        bishop_score = self._get_bishop_score(board, row, col, best_score, 7)
                        if bishop_score != 0:
                            best_score = bishop_score[0]
                            best_move = [7, row, col, bishop_score[1], bishop_score[2]]
                    # ROOK
                    elif current_piece == 9:
                        rook_score = self._get_rook_score(board, row, col, best_score, 9)
                        if rook_score != 0:
                            best_score = rook_score[0]
                            best_move = [9, row, col, rook_score[1], rook_score[2]]
                    # BISHOP
                    elif current_piece == 11:
                        bishop_score = self._get_bishop_score(board, row, col, best_score, 11)
                        if bishop_score != 0:
                            best_score = bishop_score[0]
                            best_move = [11, row, col, bishop_score[1], bishop_score[2]]
                    # KNIGHT
                    elif current_piece == 13:
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col - 2, row - 1]):
                            current_score = self.calculate_score(current_piece, col - 2, row - 1, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row - 1, col - 2]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col + 2, row - 1]):
                            current_score = self.calculate_score(current_piece, col + 2, row - 1, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row - 1, col + 2]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col - 2, row + 1]):
                            current_score = self.calculate_score(current_piece, col - 2, row + 1, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row + 1, col - 2]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col + 2, row + 1]):
                            current_score = self.calculate_score(current_piece, col + 2, row + 1, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row + 1, col + 2]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col - 1, row - 2]):
                            current_score = self.calculate_score(current_piece, col - 1, row - 2, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row - 2, col - 1]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col - 1, row + 2]):
                            current_score = self.calculate_score(current_piece, col - 1, row + 2, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row + 2, col - 1]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col + 1, row - 2]):
                            current_score = self.calculate_score(current_piece, col + 1, row - 2, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row - 2, col + 1]
                        if self._board_logic.is_valid_move(board, [8, 8], [col, row], [col + 1, row + 2]):
                            current_score = self.calculate_score(current_piece, col + 1, row + 2, board)
                            if current_score > best_score:
                                best_score = current_score
                                best_move = [13, row, col, row + 2, col + 1]
        return best_move

    # DOES NOT CHECK against valid moves!
    def calculate_score(self, piece, new_col, new_row, board):
        return self.calculate_attacks_and_protects_score(piece, new_col, new_row) \
               + self.calculate_heuristic_score(new_col, new_row, board, piece)

    def calculate_attacks_and_protects_score(self, piece, col, row):
        attack_protect_scores = self.number_pieces_attacked_and_protected(piece, col, row)
        return attack_protect_scores[0] + attack_protect_scores[1]

    # Heuristic based on (simply) proximity to king, a consideration for the future is to change as game progresses
    def calculate_heuristic_score(self, new_col, new_row, board, piece):
        if piece % 2 == 1:
            for col in range(7, -1, -1):
                for row in range(7, -1, -1):
                    if board[row, col] == 4:
                        king_row = row
                        king_col = col
                        return 8 - (abs(king_row - new_row) + abs(king_col - new_col))
        else:
            for col in range(0, 8):
                for row in range(0, 8):
                    if board[row, col] == 5:
                        king_row = row
                        king_col = col
                        return 8 - (abs(king_row - new_row) + abs(king_col - new_col))

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
                current_score = self._handle_white_move(row - 1, col - 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 1, col + 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col - 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 1, col + 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 2, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row + 2, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 2, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_white_move(row - 2, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
            elif piece == 13:
                current_score = self._handle_black_move(row - 1, col - 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 1, col + 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col - 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 1, col + 2, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 2, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row + 2, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 2, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                    else:
                        protected += 1
                current_score = self._handle_black_move(row - 2, col + 1, board)
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
        while col + 1 < 8 and row + 1 < 8:
            if board[row + 1][col + 1] != 0:
                if piece == 10 or piece == 6:
                    current_score = self._handle_white_move(row + 1, col + 1, board)
                elif piece == 11 or piece == 7:
                    current_score = self._handle_black_move(row + 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            row += 1
            col += 1
        row = orig_row
        col = orig_col
        while row + 1 < 8 and col - 1 > -1:
            if board[row + 1][col - 1] != 0:
                if piece == 10 or piece == 6:
                    current_score = self._handle_white_move(row + 1, col - 1, board)
                elif piece == 11 or piece == 7:
                    current_score = self._handle_black_move(row + 1, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            row += 1
            col -= 1
        row = orig_row
        col = orig_col
        while row - 1 > -1 and col + 1 < 8:
            if board[row - 1][col + 1] != 0:
                if piece == 10 or piece == 6:
                    current_score = self._handle_white_move(row - 1, col + 1, board)
                elif piece == 11 or piece == 7:
                    current_score = self._handle_black_move(row - 1, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            row -= 1
            col += 1
        row = orig_row
        col = orig_col
        while row - 1 > -1 and col - 1 > -1:
            if board[row - 1][col - 1] != 0:
                if piece == 10 or piece == 6:
                    current_score = self._handle_white_move(row - 1, col - 1, board)
                elif piece == 11 or piece == 7:
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
                if piece == 8 or piece == 6:
                    current_score = self._handle_white_move(row, col + 1, board)
                elif piece == 9 or piece == 7:
                    current_score = self._handle_black_move(row, col + 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            col += 1
        row = orig_row
        col = orig_col
        while row + 1 < 8:
            if board[row + 1][col] != 0:
                if piece == 8 or piece == 6:
                    current_score = self._handle_white_move(row + 1, col, board)
                elif piece == 9 or piece == 7:
                    current_score = self._handle_black_move(row + 1, col, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            row += 1
        row = orig_row
        col = orig_col
        while col - 1 > -1:
            if board[row][col - 1] != 0:
                if piece == 8 or piece == 6:
                    current_score = self._handle_white_move(row, col - 1, board)
                elif piece == 9 or piece == 7:
                    current_score = self._handle_black_move(row, col - 1, board)
                if current_score != 0:
                    if current_score == 1:
                        attacked += 1
                        break
                    else:
                        protected += 1
                        break
            col -= 1
        row = orig_row
        col = orig_col
        while row - 1 > -1:
            if board[row - 1][col] != 0:
                if piece == 8 or piece == 6:
                    current_score = self._handle_white_move(row - 1, col, board)
                elif piece == 9 or piece == 7:
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

    def _get_rook_score(self, board, row, col, best_score, piece):
        best_move_and_score = 0
        orig_row = row
        orig_col = col
        while col + 1 < 8:
            if board[row][col + 1] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col + 1, row]):
                    current_score = self.calculate_score(piece, col + 1, row, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row, col + 1]
            col += 1
        row = orig_row
        col = orig_col
        while row + 1 < 8:
            if board[row + 1][col] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col, row + 1]):
                    current_score = self.calculate_score(piece, col, row + 1, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row + 1, col]
            row += 1
        row = orig_row
        col = orig_col
        while col - 1 > -1:
            if board[row][col - 1] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col - 1, row]):
                    current_score = self.calculate_score(piece, col - 1, row, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row, col - 1]
            col -= 1
        row = orig_row
        col = orig_col
        while row - 1 > -1:
            if board[row - 1][col] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col, row - 1]):
                    current_score = self.calculate_score(piece, col, row - 1, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row - 1, col]
            row -= 1
        return best_move_and_score

    def _get_bishop_score(self, board, row, col, best_score, piece):
        best_move_and_score = 0
        orig_row = row
        orig_col = col
        while col + 1 < 8 and row + 1 < 8:
            if board[row + 1][col + 1] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col + 1, row + 1]):
                    current_score = self.calculate_score(piece, col + 1, row + 1, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row + 1, col + 1]
            row += 1
            col += 1
        row = orig_row
        col = orig_col
        while row + 1 < 8 and col - 1 > -1:
            if board[row + 1][col - 1] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col - 1, row + 1]):
                    current_score = self.calculate_score(piece, col - 1, row + 1, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row + 1, col - 1]
            row += 1
            col -= 1
        row = orig_row
        col = orig_col
        while row - 1 > -1 and col + 1 < 8:
            if board[row - 1][col + 1] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col + 1, row - 1]):
                    current_score = self.calculate_score(piece, col + 1, row - 1, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row - 1, col + 1]
            row -= 1
            col += 1
        row = orig_row
        col = orig_col
        while row - 1 > -1 and col - 1 > -1:
            if board[row - 1][col - 1] != 0:
                if self._board_logic.is_valid_move(board, [8, 8],
                                                   [orig_col, orig_row], [col - 1, row - 1]):
                    current_score = self.calculate_score(piece, col - 1, row - 1, board)
                    if current_score > best_score:
                        best_score = current_score
                        best_move_and_score = [best_score, row - 1, col - 1]
            row -= 1
            col -= 1
        return best_move_and_score
