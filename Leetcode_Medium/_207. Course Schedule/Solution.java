import java.util.*;
class Solution {
  public boolean canFinish(int numCourses, int[][] prerequisites) {
    // Create a map to store each nodes and its
    // connection (edges to other nodes)
    HashMap<Integer , List<Integer>> graph = new HashMap<>();
    // Fill the map with the value and position 
    // of each courses
    for (int i = 0; i < numCourses;i++){
      graph.put(i, new ArrayList<>());
    }
    // At each position, pass in the prerequisite
    // array to show the connectionss to other
    for (int[] prerequisite : prerequisites) {
      int courseIndex = prerequisite[0];
      int prerequisiteCourse = prerequisite[1];
      graph.get(courseIndex).add(prerequisiteCourse);
    }
    // I'm pretty much stuck now 

  }
}