import java.util.*;
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Check rows
        for (char[] row : board) {
            if (!isValidUnit(row))
                return false;
        }

        // Check columns
        for (int col = 0; col < 9; col++) {
            char[] column = new char[9];
            for (int row = 0; row < 9; row++) {
                column[row] = board[row][col];
            }
            if (!isValidUnit(column))
                return false;
        }

        // Check 3x3 squares
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                char[] square = new char[9];
                int index = 0;
                for (int r = i; r < i + 3; r++) {
                    for (int c = j; c < j + 3; c++) {
                        square[index++] = board[r][c];
                    }
                }
                if (!isValidUnit(square))
                    return false;
            }
        }

        return true;
    }

    private boolean isValidUnit(char[] unit) {
        Set<Character> digits = new HashSet<>();
        for (char cell : unit) {
            if (cell != '.') {
                if (digits.contains(cell))
                    return false;
                digits.add(cell);
            }
        }
        return true;
    }
}
