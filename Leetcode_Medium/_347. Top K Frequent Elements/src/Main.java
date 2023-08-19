public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }

    public int[] topKFrequent(int[] nums, int k) {
        int [] finalArray = new int[k];
        
    }

    public int countElement(int [] nums, int element){
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            if(element == nums[i]){
                count++;
            }
        }

        return count;
    }
}