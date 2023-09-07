public class Main {
    public static int longestPalindrome(String s) {
        int lowerArr[] = new int[26];
        int upperArr[] = new int[26];
        for (int i = 0; i<s.length();i++){
            char currentChar = s.charAt(i);
            if(Character.isUpperCase(currentChar)){
                upperArr[currentChar - 'A']++;
            } else {
                lowerArr[currentChar - 'a']++;
            }

            
        }

        int currentLength = 0;
        boolean haveOddValue = false;

        for (int i = 0; i < 26; i++){
            if(lowerArr[i] % 2 == 0){
                currentLength += lowerArr[i];
            } else{
                currentLength += lowerArr[i] - 1;
                haveOddValue = true;
            }

            if(upperArr[i] % 2 == 0){
                currentLength += upperArr[i];
            } else{
                currentLength += upperArr[i] - 1;
                haveOddValue = true;
            }
        }

        if (haveOddValue){
            currentLength++;
        }
        return currentLength;
    }

    
}


