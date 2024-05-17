class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a hashmap (dictionary) to store each
        # element of the nums inside it
        num_set = set()
        # Add each element in nums to the hashmap
        for num in nums:
            num_set.add(num)
        # Go through the hashmap and return 
        # the values which isn't present there
        for i in range(0,len(nums)+1):
            if i not in num_set:
                return i
                




