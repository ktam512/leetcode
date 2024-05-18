class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # The edge cases when s1 is a longer
        # string than s2
        if (len(s1) > len(s2)):
            return False
        # Create a hashmap/ hashset to store the 
        # character in s1 and s2
        s1Count, s2Count = [0] * 26, [0] * 26
        

        map1 = {}
