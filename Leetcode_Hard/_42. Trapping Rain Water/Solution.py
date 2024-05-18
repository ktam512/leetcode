class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxLeft, maxRight = [0]* n, [0]* n
        trapped_water = 0
        # Fill maxLeft array
        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        # Fill maxRight array
        for i in range(n - 2, 0, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])
        # At each position, the ammount of water trapped
        # is found by choosing the smaller value and reduce it
        # by the height
        for i in range(n):
            cur_water = min(maxLeft[i], maxRight[i]) - height[i]
            if (cur_water > 0):
                # Only when the cur_water value
                # is positive that we add to the 
                # total trapped water value
                trapped_water+=cur_water
        return trapped_water


