class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:  # Base case: when the length of the string is equal to 2*n
                result.append(s)
                return
            if left < n:  # If the count of '(' is less than n, we can add '('
                backtrack(s + '(', left + 1, right)
            if right < left:  # If the count of ')' is less than the count of '(' already added, we can add ')'
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack()
        return result

        