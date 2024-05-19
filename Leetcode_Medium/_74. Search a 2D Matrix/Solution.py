class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Initialize the two pointers
        m = len(matrix)
        n = len(matrix[0])
        up , down = 0, m - 1
        # The loop keep running until the
        # pointers meet each other
        while (up <= down):
            row_mean = (up + down) // 2
            if (matrix[row_mean][n-1] < target):
                # If the row's last value is smaller than the target
                # then the target is not inside this row and any row 
                # before
                up = row_mean + 1
                # When that happens, update the up pointer
                # to right below row_mean
            elif (matrix[row_mean][0] > target):
                # If the row's first value is bigger than the target
                # then the target is not inside this row and any row 
                # after
                down = row_mean - 1
                # When that happens, update the down pointer
                # to right above row_mean
                
            else :
                # Break out of the loop, found the row that may 
                # include the target
                break
        # If the loop end without finding any row that may contain
        # the target, return False
        if (up > down):
            return False
        # Start to run binary search on the current row
        left, right = 0, n - 1
        while (left <= right):
            row_mean = (up + down) // 2
            col_mean = (left + right)// 2
            if (matrix[row_mean][col_mean] < target):
                left = col_mean + 1
            elif (matrix[row_mean][col_mean] > target):
                right = col_mean - 1
            else: return True
        return False

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(1, matrix, 1))