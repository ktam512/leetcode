public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // Initialize the two pointers
        int m = matrix.length;
        int n = matrix[0].length;
        int up = 0, down = m - 1;

        // The loop keeps running until the pointers meet each other
        while (up <= down) {
            int rowMean = (up + down) / 2;
            if (matrix[rowMean][n - 1] < target) {
                // If the row's last value is smaller than the target,
                // then the target is not inside this row and any row before
                up = rowMean + 1;
                // When that happens, update the up pointer to right below rowMean
            } else if (matrix[rowMean][0] > target) {
                // If the row's first value is bigger than the target,
                // then the target is not inside this row and any row after
                down = rowMean - 1;
                // When that happens, update the down pointer to right above rowMean
            } else {
                // Break out of the loop, found the row that may include the target
                break;
            }
        }

        // If the loop ends without finding any row that may contain the target, return false
        if (up > down) {
            return false;
        }

        // Start to run binary search on the current row
        int left = 0, right = n - 1;
        while (left <= right) {
            int rowMean = (up + down) / 2;
            int colMean = (left + right) / 2;
            if (matrix[rowMean][colMean] < target) {
                left = colMean + 1;
            } else if (matrix[rowMean][colMean] > target) {
                right = colMean - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
