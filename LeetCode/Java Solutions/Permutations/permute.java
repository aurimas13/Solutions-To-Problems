import java.util.ArrayList;
import java.util.List;

public class Solution {
    
    public List<List<Integer>> permute(int[] nums) {
        // Initialize an ArrayList to store the permutations
        List<List<Integer>> result = new ArrayList<>();
        
        // Call the recursive function to generate permutations starting with an empty list and all elements in nums
        backtrack(nums, new ArrayList<>(), result);
        
        return result;
    }

    private void backtrack(int[] nums, List<Integer> currentPermutation, List<List<Integer>> result) {
        // If the current permutation is of the required length, add it to the result
        if (currentPermutation.size() == nums.length) {
            result.add(new ArrayList<>(currentPermutation));
            return;
        }

        // Iterate through the numbers, and generate permutations by adding each unchosen number
        for (int i = 0; i < nums.length; i++) {
            if (currentPermutation.contains(nums[i])) continue; // Skip numbers already present in the current permutation
            
            // Add the current number to the permutation
            currentPermutation.add(nums[i]);
            // Recursively generate permutations with the remaining numbers
            backtrack(nums, currentPermutation, result);
            // Remove the last added number to explore other possibilities
            currentPermutation.remove(currentPermutation.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.permute(new int[]{1, 2, 3})); // Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        System.out.println(solution.permute(new int[]{0, 1})); // Output: [[0,1],[1,0]]
        System.out.println(solution.permute(new int[]{1}));    // Output: [[1]]
    }
}

