
public class Main {
    public static void main(String[] args) {
        System.out.println(canConstruct("aab","eeeeeeeeaabeeeeeee"));
    }

    public static boolean canConstruct(String ransomNote, String magazine) {
        int [] charCounts = new int[26];
        for(int i = 0; i < magazine.length(); i++){
            int index = magazine.charAt(i) - 'a';
            charCounts[index]++;
        }
        for(int i = 0; i < ransomNote.length();i++){
            int index = ransomNote.charAt(i) - 'a';
            if(charCounts[index] == 0){
                return false;
            }

            charCounts[index]--;
        }

        return true;


    }
}