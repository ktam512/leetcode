class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        upper_arr = [0] * 26
        lower_arr = [0] * 26
        for i in s:
            if ord(i) - ord('a') < 0:
                upper_arr[ord(i) - ord('A')]+= 1
            else:
                lower_arr[ord(i) - ord('a')]+= 1
        
        final_length = 0
        haveOdd = False
        for i in range (26):
            if upper_arr[i] % 2 == 0 :
                final_length += upper_arr[i]
            else:
                final_length += upper_arr[i] - 1
                haveOdd = True

            if lower_arr[i] % 2 == 0 :
                final_length += lower_arr[i]
            else:
                final_length += lower_arr[i] - 1
                haveOdd = True

        
        if haveOdd:
            final_length += 1
        
        return final_length
    

# Create an instance of the Solution class
solution_instance = Solution()

# Test cases
print(solution_instance.longestPalindrome("abc"))      # Output: 1
print(solution_instance.longestPalindrome("abbccdd"))  # Output: 7
print(solution_instance.longestPalindrome("abcbad"))   # Output: 6
print(solution_instance.longestPalindrome("aABbcCD"))  # Output: 4

    

    