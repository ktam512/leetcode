import java.util.*;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // Create a TreeMap to store position and time-to-reach pairs
        TreeMap<Integer, Double> map = new TreeMap<>();
        
        // Populate the TreeMap with position and time-to-reach pairs
        for (int i = 0; i < position.length; i++) {
            map.put(-position[i], (double)(target - position[i]) / speed[i]);
        }
        
        // Initialize fleet count and previous arrival time
        int fleets = 0;
        double prevTime = 0;
        
        // Iterate through the TreeMap
        for (double time : map.values()) {
            // If the current car takes more time to reach, it forms a new fleet
            if (time > prevTime) {
                fleets++;
                prevTime = time;
            }
        }
        
        return fleets;
    }
}
