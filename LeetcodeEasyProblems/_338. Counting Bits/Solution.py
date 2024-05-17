class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Create an array to store the number of 1 bits 
        # in each array
        dp = [0] * (n+1)
        # The offset is the number we have to get to that
        # make the number have the new most signifcant bit
        # At first it's 1 because 01 is when it first got new 
        # MSB
        offset = 1

        # A for loop through each element from 1 to n
        # We know that 0 have 0 1 bit already
        for i in range(1+ n+1):
            # if 2*offset equals to the current number
            # then that means we moved to a new MSB
            if offset * 2 == i:
                offset = i 
            # The pattern we recognized that only when 
            # we changed to a new MSB that the offset changes
            # 0 - 0000 0
            # 1 - 0001 1 + dp[i - offset] / offset = 1
            # 2 - 0010 1 + dp[i - offset] / offset = 2
            # 3 - 0011 1 + dp[i - offset] / offset = 2
            # 4 - 0100 1 + dp[i - offset] / offset = 4
            # 5 - 0101 1 + dp[i - offset] / offset = 4
            # 6 - 0110 1 + dp[i - offset] / offset = 4
            # 7 - 0111 1 + dp[i - offset] / offset = 4
            # 8 - 1000 1 + dp[i - offset] / offset = 8
            dp[i] = 1 + dp[i-offset]
        
        return dp
            
            
            


            
            



