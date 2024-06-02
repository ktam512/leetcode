class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        # Initialize a 3x3 grid with empty cells
        grid = [[' ' for row in range(3)] for col in range(3)]

        # Iterate through the moves and fill the grid accordingly
        for i, move in enumerate(moves):
            # Alternate between player A ('X') and player B ('O')
            player = 'X' if i % 2 == 0 else 'O'
            row, col = move
            # Place the player's symbol in the corresponding cell
            grid[row][col] = player

        # Check if any player has won
        def check_winner(player):
            # Check rows and columns for three consecutive symbols
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
                    return True
            # Check diagonals for three consecutive symbols
            if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
                return True
            return False

        # Check if player A or player B wins
        if check_winner('X'):
            return "A"
        elif check_winner('O'):
            return "B"
        # If all cells are filled and no winner is found, return "Draw"
        elif all(cell != ' ' for row in grid for cell in row):
            return "Draw"
        # If there are still movements to play, return "Pending"
        else:
            return "Pending"