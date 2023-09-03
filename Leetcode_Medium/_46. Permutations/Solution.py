import math
import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
    
  
''' without itertools, recursive, loops'''
def dfs(nums, array, answer):
    if len(array) == len(nums):
        #print(array)
        answer.append(array)
        if len(answer) == 2:
            print(answer)
            return answer
    else:    
        for i in range(0,len(nums)):
            if nums[i] in array:
                continue
            array.append(nums[i])
            dfs(nums, array, answer)
            array.pop()