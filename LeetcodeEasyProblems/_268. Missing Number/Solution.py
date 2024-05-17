class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This solution use the exclusive OR bitwise operations
        # to solve it
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

                




