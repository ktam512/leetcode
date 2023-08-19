import Solution 
# Test cases
solution = Solution()

    # Test case 1: No palindrome possible
print(solution.longestPalindrome("abc"))  # Output: 1

    # Test case 2: Even length palindrome
print(solution.longestPalindrome("abbccdd"))  # Output: 7

    # Test case 3: Odd length palindrome
print(solution.longestPalindrome("abcbad"))  # Output: 6

    # Test case 4: Mix of upper and lower case characters
print(solution.longestPalindrome("aABbcCD"))  # Output: 4
