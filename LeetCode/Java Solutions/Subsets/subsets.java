import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>()); // Add the empty subset
        
        for (int num : nums) {
            List<List<Integer>> newSubsets = new ArrayList<>();
            for (List<Integer> subset : result) {
                List<Integer> newSubset = new ArrayList<>(subset);
                newSubset.add(num);
                newSubsets.add(newSubset);
            }
            result.addAll(newSubsets);
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.subsets(new int[]{1, 2, 3}));
        // Expected output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        System.out.println(s.subsets(new int[]{0}));
        // Expected output: [[], [0]]
    }
}
