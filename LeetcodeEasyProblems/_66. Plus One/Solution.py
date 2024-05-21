class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        # Iterate from the last digit to the first
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Set the current digit to 0 if it is 9
            digits[i] = 0
        
        # If all digits are 9, we need an extra digit at the beginning
        return [1] + digits
