class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x  # Calculate the target sum to find the subarray
        
        if target < 0:  # If the sum of all elements is less than x, it's impossible
            return -1
        
        max_subarray = -1  # Maximum length of subarray
        current_sum = 0  # Current sum of the sliding window
        left = 0  # Left pointer of the sliding window

        for right, num in enumerate(nums):
            current_sum += num
            
            while current_sum > target:  # Shrink the window if the sum is greater than the target
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_subarray = max(max_subarray, right - left + 1)  # Update the maximum subarray length
        
        if max_subarray == -1:  # If no subarray found, return -1
            return -1
        return len(nums) - max_subarray  # Return the minimum number of operations
