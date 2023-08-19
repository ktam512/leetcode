public class Main {
    public static void main(String[] args) {
        System.out.println(countPrimes(30));
    }

    public static int countPrimes(int n) {
        int count = 0;
        for(int i = 2; i < n;i++ ){
            if(identifyPrimes(i)){
                count++;
            }
        }
        return count;
    }

    public static boolean identifyPrimes(int num){
        if(num == 2){
            return true;
        }
        for(int i = 2; i < num ; i++){
            // If num is not divisible by 2,
            //then when i reach halfway from 2 to num,
            //num is already a prime
            if(num % i == 0){
                return false;
            }
        }

        return true;
    }
}
