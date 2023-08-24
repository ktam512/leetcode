from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        result = [[0] * cols for _ in range(rows)]
        
        queue = deque()
        
        # Initialize the result matrix with large values and enqueue all zeros
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
                else:
                    result[i][j] = float('inf')
        
        # Define the possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Perform BFS to update distances
        while queue:
            row, col = queue.popleft()
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    if result[newRow][newCol] > result[row][col] + 1:
                        result[newRow][newCol] = result[row][col] + 1
                        queue.append((newRow, newCol))
        
        return result