class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a hashmap to store the cumulative sum and its corresponding index
        max_length = 0
        count = 0
        hash_map = {}
        n = len(nums)

        for i in range(n):
            # If the current number is 0, decrement count by 1
            # If the current number is 1, increment count by 1
            count = count + 1 if nums[i] == 1 else count - 1
            
            # If the count becomes 0, it means equal number of 0s and 1s from start till current index
            if count == 0:
                max_length = i + 1
            
            # If the count value is already present in the hash map
            if count in hash_map:
                max_length = max(max_length, i - hash_map[count])
            else:
                # If the count value is not present, store the count value with its index
                hash_map[count] = i
        
        return max_length