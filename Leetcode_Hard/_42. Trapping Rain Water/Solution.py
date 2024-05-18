class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # Initialize the pointer and the left and right
        # max value
        left, right = 0, n -1
        leftMax, rightMax = height[left], height[right]
        trapped_water = 0
        # Running the loop until the pointer meet
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                trapped_water += leftMax - height[left]
            else :
                right -= 1
                rightMax = max(rightMax, height[right])
                trapped_water += rightMax - height[right]

        return trapped_water


