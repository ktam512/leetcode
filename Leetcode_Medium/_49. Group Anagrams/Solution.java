import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();
        
        // Iterate through each word in the array of strings
        for (String word : strs) {
            // Convert the word to a character array, sort it, and convert it back to a string
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);
            
            // If the sorted word already exists as a key in the anagrams map, append the word to its list
            // Otherwise, create a new key with the sorted word and initialize its list with the current word
            if (anagrams.containsKey(sortedWord)) {
                anagrams.get(sortedWord).add(word);
            } else {
                List<String> newList = new ArrayList<>();
                newList.add(word);
                anagrams.put(sortedWord, newList);
            }
        }
        
        // Return the values (lists of anagrams) from the map as the result
        return new ArrayList<>(anagrams.values());
    }
}
