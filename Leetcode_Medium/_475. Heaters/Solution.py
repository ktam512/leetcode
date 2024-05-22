class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # We first sort the two array so 
        # that we can search through it more easily
        houses.sort()
        heaters.sort()
        # The smaller one will be the radius we need
        # Intialize the i index to indicate
        # the current heater position
        # and the current radius
        i, radius = 0, 0
        for house in houses:
            # Move to the headers that's on the right side
            # or at the exact position of the house
            while i < len(heaters) and heaters[i] <= house:
                i+= 1
            # The left indicate the distance to the 
            # nearest left side heater
            left = house - heaters[i-1]
            # The right indicate the distance to the 
            # nearest right side heater
            right = heaters[i] - house

            # Update the radius to become the bigger value
            # between the previous radius and the smaller 
            # distance to reach the current house
            radius = max(radius, min(left,right))
        return radius

        
        

            
        