class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            #Shift the inital bit number to the right
            #i times so that its LSB got changed
            if (n & 1) == 1:
                count+= 1
            n = n >> 1
        
        return count


        


        


    
