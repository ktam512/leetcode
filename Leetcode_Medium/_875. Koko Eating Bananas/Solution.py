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
        # After filling the array, choose the 
        # eating speed to be from 1 to the maximum value
        # found above
        res = 1
        for j in range(1, maxVal + 1):
            prev_cur_hour = cur_hour
            for a in range(0, n):
                if (cur_hour > h):
                    break
                if(piles[a] <= j):
                    cur_hour += 1
                else:
                    while(piles[a] >= j):
                        piles[a] -= j 
                        cur_hour += 1
                
            if (cur_hour < prev_cur_hour):
                cur_hour = min(cur_hour, prev_cur_hour)
                res = j

        return res

    print(minEatingSpeed(1, [3,6,7,11], 8))
        




