import java.util.*;

public class Solution {
    // Initialize an ArrayList to store the combinations
    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> combine(int n, int k) {
        // Call the recursive function to generate combinations starting from 1
        backtrack(1, n, k, new ArrayList<Integer>());
        return result;
    }

    // Define a recursive function to generate combinations
    private void backtrack(int start, int n, int k, List<Integer> currentCombination) {
        // If the current combination is of the required length, add it to the result
        if (currentCombination.size() == k) {
            result.add(new ArrayList<>(currentCombination));
            return;
        }

        // Iterate through the remaining numbers and generate combinations
        for (int i = start; i <= n; i++) {
            // Add the current number to the combination
            currentCombination.add(i);
            // Recursively generate combinations with the remaining numbers
            backtrack(i + 1, n, k, currentCombination);
            // Remove the last added number to explore other possibilities
            currentCombination.remove(currentCombination.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test cases
        System.out.println(solution.combine(4, 2)); // Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        System.out.println(solution.combine(1, 1)); // Output: [[1]]
        System.out.println(solution.combine(4, 4)); // Output: [[1, 2, 3, 4]]
    }
}

