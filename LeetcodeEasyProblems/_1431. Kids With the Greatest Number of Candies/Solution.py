class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
         # Find the maximum number of candies among all kids
        max_candies = max(candies)
        
        # Initialize a list to store the result indicating whether each kid can have the greatest number of candies
        result = []
        
        # Iterate through the number of candies each kid has
        for num_candies in candies:
            # Check if the current kid can have the greatest number of candies if given extra candies
            if num_candies + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        # Return the result list
        return result