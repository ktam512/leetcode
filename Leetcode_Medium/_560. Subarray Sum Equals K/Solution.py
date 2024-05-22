class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Solve this problem using 1 nested loop
        # (brute-force)

        # Initialize the number of subarray to 0
        count = 0
        n = len(nums)

        # Use the loop to calculate the sum
        for i in range(n):
            # Initialize the current sum to 0
            # to keep track of the sum of each
            # element inside the subarray
            cur_sum = 0
            for j in range(i, n):
                # Add the element to the sum
                cur_sum += nums[j]
                # If the sum equals k, then increment the count
                if cur_sum == k:
                    count+= 1
                
        return count



        
    print(subarraySum(1, [1,-1,0], 0))