class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # The farthest index that can be reached
        max_reachable = 0
        
        # Iterate through each index in the array
        for i in range(len(nums)):
            # If the current index is beyond the maximum reachable index, return False
            if i > max_reachable:
                return False
            # Update the maximum reachable index if the current index plus its value is greater
            max_reachable = max(max_reachable, i + nums[i])
            # If the maximum reachable index is beyond or at the last index, return True
            if max_reachable >= len(nums) - 1:
                return True
        
        # If the loop finishes without reaching the last index, return False
        return False

