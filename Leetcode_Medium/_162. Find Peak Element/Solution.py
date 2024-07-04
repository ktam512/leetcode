class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check if mid is a peak
            if nums[mid] > nums[mid + 1]:
                right = mid  # Peak is in the left half including mid
            else:
                left = mid + 1  # Peak is in the right half excluding mid
        
        # At the end of the loop, left == right and it's the peak element
        return left