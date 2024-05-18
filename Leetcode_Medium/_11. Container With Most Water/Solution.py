class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize the two index
        i1, i2 = 0, 1
        cur_max = 0
        # Using 2 for loops to sort through each 
        # value of volume
        n = len(height)
        for i1 in range(0, n-1):
            for i2 in range(i1+1, n):
                # the width is the absolute value between 
                # two indexes
                cur_width = abs(i2 - i1)
                # the height is the smaller value of the two element
                cur_height = min(height[i1], height[i2])
                # the current volume is the product of the 
                # current height and width
                cur_vol = cur_width * cur_height
                # the current max volume is updated if 
                # a bigger current volume is found
                cur_max = max(cur_vol, cur_max)
                
        return cur_max
    print(maxArea(1,[1,8,6,2]))
                
