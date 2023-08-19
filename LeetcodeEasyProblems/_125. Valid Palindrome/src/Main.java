public class Main {
    public static void main(String[] args) {
        System.out.println(isPalindrome("0P"));

    }

    public static boolean isPalindrome(String s) {
        String fixedString = "";
        for ( char ch : s.toCharArray()){
            if(Character.isDigit(ch) || Character.isLetter(ch)){
                fixedString += ch;
            }
        }

        fixedString = fixedString.toLowerCase();
        int firstPointer = 0;
        int secondPointer = fixedString.length() - 1;
        while(firstPointer <= secondPointer){
            if(fixedString.charAt(firstPointer) != fixedString.charAt(secondPointer)){
                return false;
            }
            firstPointer++;
            secondPointer--;
        }

        return true;

    }
}