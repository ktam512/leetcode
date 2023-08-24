import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[][] result = new int[rows][cols];
        
        Queue<int[]> queue = new LinkedList<>();
        
        // Initialize the result matrix with large values and enqueue all zeros
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 0) {
                    result[i][j] = 0;
                    queue.offer(new int[]{i, j});
                } else {
                    result[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        
        // Define the possible directions (up, down, left, right)
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        // Perform BFS to update distances
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0];
            int col = cell[1];
            
            for (int[] direction : directions) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];
                
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
                    if (result[newRow][newCol] > result[row][col] + 1) {
                        result[newRow][newCol] = result[row][col] + 1;
                        queue.offer(new int[]{newRow, newCol});
                    }
                }
            }
        }

        return result;
    }
}