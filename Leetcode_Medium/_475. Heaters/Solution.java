import java.util.Arrays;

public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        // Sort the houses and heaters arrays
        Arrays.sort(houses);
        Arrays.sort(heaters);
        
        int radius = 0;
        int i = 0; // index for houses
        int j = 0; // index for heaters
        
        // Iterate through each house
        while (i < houses.length) {
            // Find the closest heater to the current house
            while (j < heaters.length - 1 &&
                   Math.abs(heaters[j] - houses[i]) >= Math.abs(heaters[j + 1] - houses[i])) {
                j++;
            }
            // Update the radius to cover the current house
            radius = Math.max(radius, Math.abs(heaters[j] - houses[i]));
            i++;
        }
        
        return radius;
    }
}
