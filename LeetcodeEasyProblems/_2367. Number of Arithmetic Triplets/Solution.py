class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        # Dictionary to store the count of elements
        count = {}
        # Dictionary to store the count of arithmetic triplets
        triplets_count = 0

        # Initialize the count dictionary with the elements of nums
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Iterate through the elements of nums
        for num in nums:
            # Calculate the previous numbers in the potential triplets
            prev_num1 = num - diff
            prev_num2 = num - 2 * diff
            
            # Check if both previous numbers exist in count
            if prev_num1 in count and prev_num2 in count:
                # Update triplets_count with the count of valid triplets
                triplets_count += count[prev_num1] * count[prev_num2]

        return triplets_count