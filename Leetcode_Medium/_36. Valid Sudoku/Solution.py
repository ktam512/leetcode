class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        for row in board:
            if not self.is_valid_unit(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_unit(column):
                return False
        
        # Check 3x3 squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                if not self.is_valid_unit(square):
                    return False
        
        return True

    def is_valid_unit(self, unit):
        # Check if all elements in the unit are digits from 1 to 9
        digits = set()
        for cell in unit:
            if cell != '.':
                if cell in digits:
                    return False
                digits.add(cell)
        return True
