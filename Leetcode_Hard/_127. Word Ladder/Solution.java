import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        // The middle sequence 
        // (aside from the beginWord and endWord)
        // must be inside the wordList 

        // The endWord must be inside the wordList
        // from the start
        if (!wordList.contains(endWord)){
            //If it's not, return -1
            return -1;
        }

        // Then add the beginWord to the List
        wordList.add(beginWord);

        // We also know that each word
        // that differ only by 1 will be each other's 
        // neighbor, we can then create a graph of 
        // nodes with its adjacent nodes as neighbors

        //Create the hashmap to store each node and 
        // its edge/ connections to other nodes
        HashMap<String, List<String>> wordMap = new HashMap<>();

        //Adding each nodes to the map,
        //leaving the edges list empty for now
        for (String node : wordList){
            wordMap.put(node , new ArrayList<>());
        }

        // Add all the connections / edges 
        // to the graph , using nested loop
        // to compare each nodes to each other
        for(int i = 0; i < wordList.size() ; i++){
            for(int j = i + 1; j < wordList.size(); j++){
                // If they're neighbor, add their connections
                // to each other 
                if (compareDifferByOne(wordList.get(i), wordList.get(i))){
                    wordMap.get(wordList.get(i)).add(wordList.get(j));
                    wordMap.get(wordList.get(j)).add(wordList.get(i));
                }
            }
        }
        // The next step, I think would be
        // build anothe helper method to 
        // calculate the shortest path from the 
        //beginWord and endWord 

        // However, I am out of time and
        // feels like it will take at least 30 min for me 
        // to write something like that. So I will stop here


        // Return -1 for placeholding compile
        return -1;


        
    }
    // Write a helper method comparing each node
    // to see if they only have the differences
    // of 1 character - means they are neighbors in
    // the graph
    private boolean compareDifferByOne(String word1, String word2){
        // Count the number of same character
        int count = 0;
        
        for(int i = 0; i < word1.length(); i++){
            if (word1.charAt(i) == word2.charAt(i)){
                count++;
            }
        }
        // If it's different to 1, return false
        if (count != 1){
            return true;
        }
        return false;
    } 
}