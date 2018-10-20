class ChessLogic:
    def __init__(self):
        self.black_can_castle_left = True
        self.black_can_castle_right = True
        self.white_can_castle_left = True
        self.white_can_castle_right = True

    # TODO: checks, checkmates, stalemates
    def is_valid_move(self, board, board_dimensions, original_pos, new_pos):
        current_column = original_pos[0]
        current_row = original_pos[1]
        current_piece = board[current_row][current_column]
        new_column = new_pos[0]
        new_row = new_pos[1]
        new_piece = board[new_row][new_column]
        board_size = board_dimensions[0] - 1
        # EMPTY or SAME PLACE or SAME COLOR
        if self._is_empty(current_piece) or \
            (new_column == current_column and new_row == current_row) or \
                (not self._is_empty(new_piece)) and self.is_same_color(current_piece, new_piece):
            return False
        # PAWN
        elif current_piece == 2 or current_piece == 3:
            # if WHITE
            if current_piece == 2:
                return (new_row == current_row - 1) and (new_column == current_column) and self._is_empty(
                    board[new_row, current_column]) or self._not_blocked_or_is_attack(new_row, new_column, current_row,
                                                                                      current_column, current_piece,
                                                                                      board) or (
                               new_row == current_row - 2 and new_column == current_column and self._is_empty(
                           board[new_row, current_column]) and board[board_size - 1][current_column] != 14)
            # if BLACK
            elif current_piece == 3:
                return (new_row == current_row + 1) and (new_column == current_column) and self._is_empty(
                    board[new_row, current_column]) or self._not_blocked_or_is_attack(new_row, new_column, current_row,
                                                                                      current_column, current_piece,
                                                                                      board) or (
                               new_row == current_row + 2 and new_column == current_column and self._is_empty(
                           board[new_row, current_column]) and board[1][current_column] != 14)
        # KNIGHT
        elif current_piece == 12 or current_piece == 13:
            return self._in_bounds(new_row, new_column, board_size) and \
                   (new_column == current_column - 2 and new_row == current_row - 1) or \
                   (new_column == current_column + 2 and new_row == current_row - 1) or \
                   (new_column == current_column - 2 and new_row == current_row + 1) or \
                   (new_column == current_column + 2 and new_row == current_row + 1) or \
                   (new_column == current_column - 1 and new_row == current_row - 2) or \
                   (new_column == current_column - 1 and new_row == current_row + 2) or \
                   (new_column == current_column + 1 and new_row == current_row - 2) or \
                   (new_column == current_column + 1 and new_row == current_row + 2)
        # BISHOP
        elif current_piece == 10 or current_piece == 11:
            return self._in_bounds(new_row, new_column, board_size) and \
                   self._valid_bishop_move(new_row, new_column, current_row, current_column) and \
                   self._not_blocked_or_is_attack(new_row, new_column, current_row, current_column, current_piece,
                                                  board)
        # ROOK
        elif current_piece == 8 or current_piece == 9:
            return self._in_bounds(new_row, new_column, board_size) and \
                   self._valid_rook_move(new_row, new_column, current_row, current_column) and \
                   self._not_blocked_or_is_attack(new_row, new_column, current_row, current_column, current_piece,
                                                  board)
        # QUEEN
        elif current_piece == 6 or current_piece == 7:
            bishop_move = self._valid_bishop_move(new_row, new_column, current_row, current_column)
            rook_move = self._valid_rook_move(new_row, new_column, current_row, current_column)
            return ((bishop_move and not rook_move) or (rook_move and not bishop_move)) and \
                   self._not_blocked_or_is_attack(new_row, new_column, current_row, current_column, current_piece,
                                                  board)
        # KING
        elif current_piece == 4 or current_piece == 5:
            return (self._in_bounds(new_row, new_column, board_size) and
                    ((new_column == current_column + 1 and new_row == current_row) or
                     (new_column == current_column - 1 and new_row == current_row) or
                     (new_column == current_column and new_row == current_row + 1) or
                     (new_column == current_column and new_row == current_row - 1) or
                     (new_column == current_column + 1 and new_row == current_row + 1) or
                     (new_column == current_column - 1 and new_row == current_row + 1) or
                     (new_column == current_column + 1 and new_row == current_row - 1) or
                     (new_column == current_column - 1 and new_row == current_row - 1)))

    # RETURNS TRUE if row, col are inside the board
    @staticmethod
    def _in_bounds(row, col, size):
        return 0 <= row <= size and 0 <= col <= size

    @staticmethod
    def _valid_bishop_move(new_row, new_column, current_row, current_column):
        return (new_column - current_column == new_row - current_row) or \
               (new_column - current_column == current_row - new_row) or \
               (current_column - new_column == new_row - current_row) or \
               (current_column - new_column == current_row - new_row)

    @staticmethod
    def _valid_rook_move(new_row, new_column, current_row, current_column):
        return (new_column == current_column) or (new_row == current_row)

    # RETURNS TRUE if the new location is being attacked by piece in current location
    @staticmethod
    def _is_attacked_by(new_row, new_column, current_row, current_column, current_piece, board):
        return True

    @staticmethod
    def _is_empty(piece):
        return piece == 0 or \
               piece == 14

    # RETURNS TRUE if no pieces are between the current piece and the destination piece
    # only for BISHOP, QUEEN, ROOK
    # IMPORTANT: only VALID MOVES on DIFFERENT COLORED PIECES will be made when this is called!
    def _not_blocked_or_is_attack(self, new_row, new_column, current_row, current_column, current_piece, board):
        # WHITE PAWN
        if current_piece == 2:
            if new_row == current_row - 1:
                if (new_column == current_column - 1) or (new_column == current_column + 1):
                    return not self._is_empty(board[new_row][new_column])
            return False
        # BLACK PAWN
        elif current_piece == 3:
            if new_row == current_row + 1:
                if (new_column == current_column - 1) or (new_column == current_column + 1):
                    return not self._is_empty(board[new_row][new_column])
            return False
        # BISHOP
        elif current_piece == 10 or current_piece == 11:
            return self._is_valid_bishop_attack(new_row, new_column, current_row, current_column, board)
        # ROOK
        elif current_piece == 8 or current_piece == 9:
            return self._is_valid_rook_attack(new_row, new_column, current_row, current_column, board)
        # QUEEN
        elif current_piece == 6 or current_piece == 7:
            bishop_move = self._is_valid_bishop_attack(new_row, new_column, current_row, current_column, board)
            rook_move = self._is_valid_rook_attack(new_row, new_column, current_row, current_column, board)
            return (bishop_move and not rook_move) or (rook_move and not bishop_move)

    @staticmethod
    def is_same_color(current_piece, new_piece):
        return ((current_piece % 2 == 1 and new_piece % 2 == 1) or
                (current_piece % 2 == 0 and new_piece % 2 == 0))

    def _is_valid_bishop_attack(self, new_row, new_column, current_row, current_column, board):
        if new_column > current_column and new_row > current_row:
            while current_row != new_row - 1 and current_column != new_column - 1:
                if not self._is_empty(board[new_row - 1][new_column - 1]):
                    return False
                new_row -= 1
                new_column -= 1
            return True
        elif new_column > current_column and new_row < current_row:
            while current_row != new_row + 1 and current_column != new_column - 1:
                if not self._is_empty(board[new_row + 1][new_column - 1]):
                    return False
                new_row += 1
                new_column -= 1
            return True
        elif new_column < current_column and new_row < current_row:
            while current_row != new_row + 1 and current_column != new_column + 1:
                if not self._is_empty(board[new_row + 1][new_column + 1]):
                    return False
                new_row += 1
                new_column += 1
            return True
        elif new_column < current_column and new_row > current_row:
            while current_row != new_row - 1 and current_column != new_column + 1:
                if not self._is_empty(board[new_row - 1][new_column + 1]):
                    return False
                new_row -= 1
                new_column += 1
            return True

    def _is_valid_rook_attack(self, new_row, new_column, current_row, current_column, board):
        if new_row == current_row:
            if new_column > current_column:
                while current_column != new_column - 1:
                    if not self._is_empty(board[new_row][new_column - 1]):
                        return False
                    new_column -= 1
                return True
            elif new_column < current_column:
                while current_column != new_column + 1:
                    if not self._is_empty(board[new_row][new_column + 1]):
                        return False
                    new_column += 1
                return True
        elif new_column == current_column:
            if new_row > current_row:
                while current_row != new_row - 1:
                    if not self._is_empty(board[new_row - 1][new_column]):
                        return False
                    new_row -= 1
                return True
            elif new_row < current_row:
                while current_row != new_row + 1:
                    if not self._is_empty(board[new_row + 1][new_column]):
                        return False
                    new_row += 1
                return True

    def cannot_castle(self, current_piece, board_dimensions, current_column):
        edge_location = board_dimensions[1] - 1
        if self.white_can_castle_right and self.white_can_castle_left and \
                (current_piece == 4):
            self.white_can_castle_left = False
            self.white_can_castle_right = False
        elif current_piece == 8:
            if self.white_can_castle_right and self.white_can_castle_left:
                if current_column == edge_location:
                    self.white_can_castle_right = False
                elif current_column == 0:
                    self.white_can_castle_left = False
            elif self.white_can_castle_left and not self.white_can_castle_right:
                if current_column == 0:
                    self.white_can_castle_left = False
            elif self.white_can_castle_right and not self.white_can_castle_left:
                if current_column == edge_location:
                    self.white_can_castle_right = False
        elif self.black_can_castle_right and self.black_can_castle_left and \
                (current_piece == 5):
            self.black_can_castle_left = False
            self.black_can_castle_right = False
        elif current_piece == 9:
            if self.black_can_castle_left and self.black_can_castle_right:
                if current_column == edge_location:
                    self.black_can_castle_right = False
                elif current_column == 0:
                    self.black_can_castle_left = False
            elif self.black_can_castle_left and not self.black_can_castle_right:
                if current_column == 0:
                    self.black_can_castle_left = False
            elif self.black_can_castle_right and not self.black_can_castle_left:
                if current_column == edge_location:
                    self.black_can_castle_right = False

    def castled_white(self):
        self.white_can_castle_left = False
        self.white_can_castle_right = False

    def castled_black(self):
        self.black_can_castle_left = False
        self.black_can_castle_right = False

    # TODO: make robust
    def free_to_castle(self, current_column, new_column, new_row, board):
        if new_column > current_column:
            while new_column != current_column:
                if not self._is_empty(board[new_row][new_column]):
                    return False
                new_column -= 1
        elif new_column < current_column:
            while new_column != current_column:
                if not self._is_empty(board[new_row][new_column]):
                    return False
                new_column += 1
        return True
