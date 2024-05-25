class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        
        // Depth First Search (DFS) function to calculate the area of an island
        int dfs(int i, int j) {
            if (i >= 0 && i < grid.length && j >= 0 && j < grid[0].length && grid[i][j] == 1) {
                grid[i][j] = 0; // Mark the cell as visited
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1); // Calculate area recursively
            }
            return 0;
        }
        
        // Iterate through each cell in the grid
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) { // If the cell is part of an island
                    maxArea = Math.max(maxArea, dfs(i, j)); // Update the maximum area
                }
            }
        }
        
        return maxArea;
    }
}
