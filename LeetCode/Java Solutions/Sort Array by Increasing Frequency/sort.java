import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] frequencySort(int[] nums) {
        // Convert int array to Integer array
        Integer[] numsInteger = Arrays.stream(nums).boxed().toArray(Integer[]::new);

        // Count the frequency of each number
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Sort the array using a custom comparator
        Arrays.sort(numsInteger, (a, b) -> {
            int freqA = freqMap.get(a);
            int freqB = freqMap.get(b);
            if (freqA == freqB) {
                return b - a; // If frequencies are the same, sort by value in descending order
            }
            return freqA - freqB; // Otherwise, sort by frequency in ascending order
        });

        // Convert Integer array back to int array
        for (int i = 0; i < nums.length; i++) {
            nums[i] = numsInteger[i];
        }

        return nums;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.frequencySort(new int[]{1,1,2,2,2,3})));  // Output: [3, 1, 1, 2, 2, 2]
        System.out.println(Arrays.toString(sol.frequencySort(new int[]{2,3,1,3,2})));    // Output: [1, 3, 3, 2, 2]
        System.out.println(Arrays.toString(sol.frequencySort(new int[]{-1, 1, -6, 4, 5, -6, 1, 4, 1})));  // Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]
    }
}
