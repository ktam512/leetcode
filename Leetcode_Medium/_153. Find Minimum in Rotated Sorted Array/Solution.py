class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:  # If mid element is greater than last, pivot lies to right of mid
                left = mid + 1
            else:  # Otherwise, pivot lies to left of or at mid
                right = mid
        return nums[left]  # Return element at left index as minimum