import java.util.ArrayList;
import java.util.List;

class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        return backtrack(nums, k, 0, new ArrayList<>()); // Start counting from empty subset
    }
    
    private int backtrack(int[] nums, int k, int start, List<Integer> current) {
        if (start == nums.length) {
            return current.isEmpty() ? 0 : 1;
        }
        int count = 0;
        count += backtrack(nums, k, start + 1, current); // Skip current element
        boolean canAdd = true;
        for (int num : current) {
            if (Math.abs(num - nums[start]) == k) {
                canAdd = false;
                break;
            }
        }
        if (canAdd) {
            current.add(nums[start]);
            count += backtrack(nums, k, start + 1, current);
            current.remove(current.size() - 1);
        }
        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.beautifulSubsets(new int[]{2, 4, 6}, 2));  // Output: 4
        System.out.println(sol.beautifulSubsets(new int[]{1}, 1));        // Output: 1
    }
}
