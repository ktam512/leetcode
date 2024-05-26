class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_length = 0
    
        # Iterate through the array
        for num in nums:
            if num - 1 not in num_set:  # Check if the current number is the start of a sequence
                current_num = num
                current_length = 1
            
                # Count consecutive elements
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)  # Update max length
    
        return max_length
        