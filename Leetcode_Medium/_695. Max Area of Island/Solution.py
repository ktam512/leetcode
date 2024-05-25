class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        
        # Depth First Search (DFS) function to calculate the area of an island
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0  # Mark the cell as visited
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)  # Calculate area recursively
            return 0
        
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:  # If the cell is part of an island
                    max_area = max(max_area, dfs(i, j))  # Update the maximum area
        return max_area
