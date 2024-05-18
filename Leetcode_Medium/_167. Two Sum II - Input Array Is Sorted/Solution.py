class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize two pointer at the 
        # start and the end of the list
        left, right = 0 , len(numbers) - 1
        while (left < right):
            sum_number = numbers[left] + numbers[right]
            if (sum_number < target):
                left += 1
            elif(sum_number == target):
                return [left + 1, right + 1]
            else:
                right -= 1
