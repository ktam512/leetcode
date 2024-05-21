class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Create a hashset to keep track of 
        # all visited number
        visit = set()
        # The loop runs until there's a duplicate
        while n not in visit:
            # Add the number into the hashset
            visit.add(n)
            # Update the number to the sum
            # of its digit squared
            n = self.squareOfDigit(n)
        # After the loop, if n == 1, return True
        if n == 1:
            return True
        # Else, return False
        return False
    
    def squareOfDigit(self, number):
        # Initialize the sum of the digit squared
        sum = 0
        # The loop runs until the number == 0
        while number:
            sum +=  pow((number%10),2)
            # After adding the digit squared, update
            # the number
            number //= 10
        return sum


        