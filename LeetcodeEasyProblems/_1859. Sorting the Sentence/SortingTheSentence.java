import java.util.Arrays;

public class SortingTheSentence {

    public static String sortSentence(String s) {
        
        String[] words = s.split(" ");
        
        String[] sortedWords = new String[words.length];
        
        
        for (String word : words) {
            
            int position = Character.getNumericValue(word.charAt(word.length() - 1));
            
            sortedWords[position - 1] = word.substring(0, word.length() - 1);
        }
        
        
        return String.join(" ", sortedWords);
    }

    
}
