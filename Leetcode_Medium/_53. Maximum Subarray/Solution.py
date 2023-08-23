class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0         # Current sum of subarray
        maxSum = float('-inf')  # Overall maximum sum
        
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)
        
        return maxSum