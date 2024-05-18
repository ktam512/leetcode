class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        # Intialize the pointers
        left, right = 0, n - 1
        # Keep running until two pointers meat each other
        while left <= right:
            mean = (left + right) // 2
            if nums[mean] > target:
                right = mean - 1
            elif nums[mean] < target:
                left = mean + 1
            else:
                return mean
        return -1