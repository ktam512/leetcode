class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            #Shift the inital bit number to the right
            #i times so that its LSB got changed
            n = n >> 1
            if (n & 1) == 1:
                count+= 1
        
        return count


        


        


    
