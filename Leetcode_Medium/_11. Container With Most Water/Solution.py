class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize the two pointers
        left, right = 0, len(height) - 1
        max_vol = 0
        # End the loop when two pointers meet
        while(left < right):
            # Width = absolute value between 2 indexes
            cur_width = right - left
            # Height = smaller value of the two elements
            cur_height = min(height[left], height[right])
            # Replace the max volume is the bigger one is found
            max_vol = max(max_vol, cur_width * cur_height)
            if (height[left] < height[right]):
                left+=1
            else:
                right-=1
        return max_vol

    print(maxArea(1,[1,8,6,2]))
                
