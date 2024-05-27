class Solution:
    def carFleet(self, target , position, speed):
        # Create a list of tuples to store position and time-to-reach pairs
        cars = sorted(zip(position, speed), reverse=True)
        
        # Initialize fleet count and previous arrival time
        fleets = 0
        prevTime = 0
        
        # Iterate through the cars
        for pos, spd in cars:
            # Calculate time to reach the target
            time = (target - pos) / spd
            
            # If the current car takes more time to reach, it forms a new fleet
            if time > prevTime:
                fleets += 1
                prevTime = time
        
        return fleets
