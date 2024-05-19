class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        maxVal = 0
        # Length of the array
        n = len(piles)
        for i in range(0,n):
            maxVal = max(maxVal, piles[i])
        
        for j in range(1, maxVal + 1):