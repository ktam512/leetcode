class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 1
        current = 0
        for i in range(n-1):
            current = first + second
            first = second
            second = current
        
        return current
        

        


    
   

    