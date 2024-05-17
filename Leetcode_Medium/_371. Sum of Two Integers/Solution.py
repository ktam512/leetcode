class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        return a
        