import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution { 
    // Using a HashMap to store the results of subproblems
    Map<Pair<Integer, Integer>, Integer> dp = new HashMap<>();

    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        // Sort the second array to allow for binary search
        Arrays.sort(arr2);

        // Start the helper method with the first index and a previous value of -1
        int answer = helper(0, -1, arr1, arr2);

        // Return the answer if it is less than the maximum integer value, else return -1
        return answer < Integer.MAX_VALUE-100 ? answer : -1;
    }

    private int helper(int i, int prev, int[] arr1, int[] arr2) {
        // If we have traversed the entire arr1, return 0 as no more operations are needed
        if (i == arr1.length) {
            return 0;
        }

        // Create a pair object once and reuse it
        Pair<Integer, Integer> currentPair = new Pair<>(i, prev);
        if (dp.containsKey(currentPair)) {
            return dp.get(currentPair);
        }

        int operation = Integer.MAX_VALUE-100;

        // If the current element in arr1 is greater than the previous value, 
        // then keep it and move to the next element
        if (arr1[i] > prev) {
            operation = helper(i + 1, arr1[i], arr1, arr2);
        }

        // Find the first element in arr2 that is greater than prev
        int idx = binarySearch(arr2, prev);

        // If such an element exists, replace the current element in arr1 with this element
        if (idx < arr2.length) {
            operation = operation < (1 + helper(i + 1, arr2[idx], arr1, arr2)) ? operation : 1 + helper(i + 1, arr2[idx], arr1, arr2);
        }

        // Store the result in the dp table
        dp.put(currentPair,operation);
        return operation;
    }

    // Binary search function to find the first element that is greater than the given value
    private static int binarySearch(int[] arr, int value) {
        int left = 0, right = arr.length-1;
        while (left <= right) {
            int mid = left+(right-left) / 2;
            if (arr[mid] <= value) {
                left = mid + 1;
            } else {
                right = mid-1;
            }
        }
        return left;
    } 
}
