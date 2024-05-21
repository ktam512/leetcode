class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use the exclusive OR bitwise operations
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

                




