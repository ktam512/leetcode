class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        normal_hashmap = dict.fromkeys(range(n), range(n))
        for i in range(n):
            if nums[i] in normal_hashmap:
                normal_hashmap.pop(i)
        
        return normal_hashmap.values()[0]


