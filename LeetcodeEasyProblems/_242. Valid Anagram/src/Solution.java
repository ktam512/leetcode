import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(isAnagram("anagram","nagaram"));

    }

    public static boolean isAnagram(String s, String t) {
        char[] alphabetArr = new char[26];
        char[] originArr = new char[26];
        for (char ch : s.toCharArray()) {
            int index = ch - 'a';
            alphabetArr[index]++;
        }

        for (char ch : t.toCharArray()) {
            int index = ch - 'a';
            alphabetArr[index]--;
        }

        for (char ch : t.toCharArray()){
            int 
        }

        if (Arrays.equals(alphabetArr,originArr)) {
            return true;
        }
        return false;
    }


}