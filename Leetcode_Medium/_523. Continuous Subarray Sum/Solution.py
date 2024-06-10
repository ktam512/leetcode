class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_index = {0: -1}  # Initialize with running sum 0 at index -1
        running_sum = 0
        
    
        for i, num in enumerate(nums):
            running_sum += num
            if k != 0:
                running_sum %= k  # Remainder to handle negative numbers
        
            if running_sum in sum_index:
                if i - sum_index[running_sum] > 1:
                    return True
            else:
                sum_index[running_sum] = i
            
        return False
        