public class Main {
    public static void main(String[] args) {
        System.out.println(romanToInt("LVIII"));
    }

    public static int romanToInt(String s) {
        int finalNum = 0;
        for (int i = 0; i< s.length(); i++){
            if(i != s.length()-1){
                if(s.charAt(i) == s.charAt(i+1)){
                    finalNum +=
                            turnSingleCharToNum(s.charAt(i));
                } else {
                    if(special2ComToNum(s.substring(i,i+2)) != 0){
                        finalNum += special2ComToNum(s.substring(i,i+2));
                        i+=1;
                    } else{
                        finalNum +=
                                turnSingleCharToNum(s.charAt(i));
                    }
                }
            } else {
                finalNum += turnSingleCharToNum(s.charAt(s.length()-1));
                break;
            }
        }


        return finalNum;

    }

    public static int  turnSingleCharToNum (char ch){
        switch (ch){
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }

    public static int special2ComToNum(String s) {
        //First we call the memories of 6 special 6 2-char
        //instances to identify them when they appear
        if(s.length()!= 2){
            return 0;
        }

        if(s.equals("IV")){
            return 4;
        } else if(s.equals("IX")) {
            return 9;
        } else if(s.equals("XL")) {
            return 40;
        } else if(s.equals("XC")) {
            return 90;
        } else if(s.equals("CD")) {
            return 400;
        } else if(s.equals("CM")) {
            return 900;
        }

        return 0;
    }
}
// random comment
