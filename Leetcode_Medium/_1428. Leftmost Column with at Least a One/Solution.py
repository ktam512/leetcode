class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get the dimensions of the binary matrix
        dimensions = binaryMatrix.dimensions()
        rows, cols = dimensions[0], dimensions[1]
        
        # Initialize pointers for binary search
        leftmost = 0
        rightmost = cols - 1
        result = -1  # Initialize result to -1 (default if no column with 1s found)
        
        # Perform binary search on columns
        while leftmost <= rightmost:
            mid = leftmost + (rightmost - leftmost) // 2  # Calculate midpoint
            
            found_one = False
            
            # Check each row in the current column `mid`
            for row in range(rows):
                if binaryMatrix.get(row, mid) == 1:
                    found_one = True
                    break
            
            # If `1` is found in current column `mid`, update `result` and adjust search range
            if found_one:
                result = mid
                rightmost = mid - 1  # Look for earlier `1`s in columns left of `mid`
            else:
                leftmost = mid + 1  # Search in columns right of `mid`
        
        return result  # Return the leftmost column index with at least one `1`, or `-1` if not found