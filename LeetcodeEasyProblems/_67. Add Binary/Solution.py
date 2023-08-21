class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
    
        while i >= 0 or j >= 0:
            total_sum = carry
            if i >= 0:
             total_sum += int(a[i])
            if j >= 0:
              total_sum += int(b[j])
        
            result.append(str(total_sum % 2))
            carry = total_sum // 2
        
            i -= 1
            j -= 1
    
        if carry != 0:
            result.append(str(carry))
    
        return ''.join(result[::-1])