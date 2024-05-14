public class MergeSort {

    // Main function that sorts an array using merge sort
    public static void mergeSort(int[] array) {
        if (array.length < 2) {
            return; // Base case: if array is of length 1 or empty, it's already sorted
        }
        int mid = array.length / 2;
        int[] left = new int[mid];
        int[] right = new int[array.length - mid];

        // Copy the left half of array into left
        for (int i = 0; i < mid; i++) {
            left[i] = array[i];
        }

        // Copy the right half of array into right
        for (int i = mid; i < array.length; i++) {
            right[i - mid] = array[i];
        }

        // Recursively sort the two halves
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted halves
        merge(array, left, right);
    }

    // Function to merge two sorted arrays
    public static void merge(int[] array, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        // Compare elements from left and right arrays and copy the smaller element to array
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                array[k++] = left[i++];
            } else {
                array[k++] = right[j++];
            }
        }

        // Copy the remaining elements from left array, if any
        while (i < left.length) {
            array[k++] = left[i++];
        }

        // Copy the remaining elements from right array, if any
        while (j < right.length) {
            array[k++] = right[j++];
        }
    }

    // Helper function to print the array
    public static void printArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    // Main method to test the merge sort implementation
    public static void main(String[] args) {
        int[] array = { 38, 27, 43, 3, 9, 82, 10 };
        System.out.println("Original array:");
    }
}
    
