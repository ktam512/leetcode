class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Determine the group of numbers (1-9, 10-99, 100-999, etc.)
        size = 1
        count = 9
        start = 1
        
        while n > size * count:
            n -= size * count
            size += 1
            count *= 10
            start *= 10
        
        #Find the actual number where the nth digit is located
        num = start + (n - 1) // size
        
        #Find the digit within the number
        return int(str(num)[(n - 1) % size])
