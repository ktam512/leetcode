public class Main {
    public static void main(String[] args) {
        String [] strs = {"flower","flow","flight"};
        System.out.println(
                longestCommonPrefix(strs)
        );
    }

    public static String longestCommonPrefix(String[] strs) {
        String curCmnPrefix = "";
        if(strs.length == 0){
            return curCmnPrefix;
        } else if(strs.length == 1){
            return strs[0];
        } else{
            curCmnPrefix = commonPrefixOfTwoStr(strs[0],
                    strs[1]);
        }
        for(int i = 2; i< strs.length - 1; i++){
            curCmnPrefix = commonPrefixOfTwoStr(curCmnPrefix,strs[i]);
        }

        return curCmnPrefix;

    }

    public static String commonPrefixOfTwoStr(String str1, String str2){
        String cmnPrefix = "";
        if(str1 == null
        || str2 == null ||
        str1.length() == 0 ||
        str2.length() == 0){
            return cmnPrefix;
        }
        int endIndexCmnPrefix = 0;
        int finalPossibleIndex = 0;
        //Identify what's the final index that we can reach
        if(str1.length()>=str2.length()){
            finalPossibleIndex = str2.length();
        } else {
            finalPossibleIndex = str1.length() ;
        }
        while(true) {
            if(endIndexCmnPrefix != finalPossibleIndex){
                if (str1.substring(0, endIndexCmnPrefix + 1).equals(
                        str2.substring(0, endIndexCmnPrefix + 1))
                ) {
                    cmnPrefix =
                            str1.substring(0, endIndexCmnPrefix + 1);
                    endIndexCmnPrefix++;
                } else {
                    break;
                }
            } else{
                return str1.substring(0, finalPossibleIndex);
            }


        }

        return cmnPrefix;
    }
}