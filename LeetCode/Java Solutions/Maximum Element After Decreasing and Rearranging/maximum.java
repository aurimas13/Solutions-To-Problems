import java.util.Arrays;

class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr); // Step 1: Sort the array
        arr[0] = 1; // Step 2: Set the first element to 1

        // Step 3: Adjust subsequent elements
        for (int i = 1; i < arr.length; i++) {
            if (Math.abs(arr[i] - arr[i - 1]) > 1) {
                arr[i] = arr[i - 1] + 1;
            }
        }

        // Step 4: The last element is the maximum value possible
        return arr[arr.length - 1];
    }
}
