class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
     
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1  # Increment l
            elif nums[i] == 2:
                swap(i, r)
                r -= 1  # Decrement r
                i -= 1  # Decrement i to recheck the swapped value
            i += 1
            

        


    