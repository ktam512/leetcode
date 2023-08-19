class Main{
    public static int climbStairs(int n){
        if (n ==1 ){
            return 1;
        }
        if (n ==2){
            return 2;
        }

        int firstNum = 1;
        int secondNum = 2;
        int currentNum = 0;

        for (int i = 3; i < n; i++){
            currentNum = firstNum + secondNum;
            firstNum = secondNum;
            secondNum = currentNum;
        }

        return currentNum;
    }
    public static void main(String[] args) {
        System.out.println(climbStairs(24));
        
}

}

