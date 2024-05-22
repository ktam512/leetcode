class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Check the case when s is null or empty
        if s == None or len(s) == 0:
            return 0
        # Remove the leading whitespace (if it exists)
        s = s.lstrip()
        # Then check if the string is empty now
        # (Meaning it only contains white space)
        if len(s) == 0:
            return 0
        # Check the sign of the string
        # Intialize it as 1 
        sign = 1
        # When the next char is '-'
        # update the sign to -1
        if s[0] == '-':
            sign = -1
            # update the string without the '-'
            s = s[1:]
        # When the next char is '+'
        # only up the string
        # since the default sign is 1 already
        elif s[0] == '+':
            s = s[1:]

        # Intialize the upper and lower
        # case of the 32-bit integer
        max_num = 2**31 - 1
        min_num = -2**31
        # Initialize the final result as 0
        result = 0
        # Loop through each character in the remaning
        # string, and stop it when it meet a non-digit
        for ch in s:
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)
            # Check if result is out of bound
            if result * sign > max_num:
                return max_num
            elif result * sign < min_num:
                return min_num
        return result * sign
            

    