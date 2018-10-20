class ChessLogic:

    # TODO: checks, checkmates, ATTACKS, replace pawn with queen
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
                return (new_row >= 0) and (new_row == current_row - 1) and (new_column == current_column)
            # if BLACK
            elif current_piece == 3:
                return (new_row <= board_size) and (new_row == current_row + 1) and (new_column == current_column)
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
            return self._valid_bishop_move(new_row, new_column, current_row, current_column) or \
                   self._valid_rook_move(new_row, new_column, current_row, current_column) and \
                   self._not_blocked_or_is_attack(new_row, new_column, current_row, current_column, current_piece,
                                                  board)
        # KING
        elif current_piece == 4 or current_piece == 5:
            return self._in_bounds(new_row, new_column, board_size) and \
                   ((new_column == current_column + 1 and new_row == current_row) or
                    (new_column == current_column - 1 and new_row == current_row) or
                    (new_column == current_column and new_row == current_row + 1) or
                    (new_column == current_column and new_row == current_row - 1) or
                    (new_column == current_column + 1 and new_row == current_row + 1) or
                    (new_column == current_column - 1 and new_row == current_row + 1) or
                    (new_column == current_column + 1 and new_row == current_row - 1) or
                    (new_column == current_column - 1 and new_row == current_row - 1))

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
               piece == 14 or \
               piece == 15 or \
               piece == 16

    # RETURNS TRUE if no pieces are between the current piece and the destination piece
    # only for BISHOP, QUEEN, ROOK
    def _not_blocked_or_is_attack(self, new_row, new_column, current_row, current_column, current_piece, board):
        # BISHOP
        if current_piece == 10 or current_piece == 11:
            if new_column > current_column and new_row > current_row:
                while current_row != new_row-1 and current_column != new_column-1:
                    if not self._is_empty(board[new_row-1][new_column-1]):
                        return False
                    new_row -= 1
                    new_column -= 1
                return True
            elif new_column > current_column and new_row < current_row:
                while current_row != new_row+1 and current_column != new_column-1:
                    if not self._is_empty(board[new_row+1][new_column-1]):
                        return False
                    new_row += 1
                    new_column -= 1
                return True
            elif new_column < current_column and new_row < current_row:
                while current_row != new_row+1 and current_column != new_column+1:
                    if not self._is_empty(board[new_row+1][new_column+1]):
                        return False
                    new_row += 1
                    new_column += 1
                return True
            elif new_column < current_column and new_row > current_row:
                while current_row != new_row-1 and current_column != new_column+1:
                    if not self._is_empty(board[new_row-1][new_column+1]):
                        return False
                    new_row -= 1
                    new_column += 1
                return True
        return True

    @staticmethod
    def is_same_color(current_piece, new_piece):
        return ((current_piece % 2 == 1 and new_piece % 2 == 1) or
                (current_piece % 2 == 0 and new_piece % 2 == 0))
