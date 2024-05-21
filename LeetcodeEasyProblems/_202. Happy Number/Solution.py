class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.squareOfDigit(n)
        if n == 1:
            return True
        return False
    
    def squareOfDigit(self, number):
        sum = 0
        while number:
            sum +=  pow((number%10),2)
            number //= 10
        return sum


        