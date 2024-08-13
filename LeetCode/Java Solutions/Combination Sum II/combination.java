import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<>();
        Arrays.sort(candidates);  // Sort to handle duplicates
        backtrack(candidates, target, 0, new ArrayList<>(), results);
        return results;
    }
    
    private void backtrack(int[] candidates, int remain, int start, List<Integer> current, List<List<Integer>> results) {
        if (remain == 0) {
            results.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i-1]) continue;  // Skip duplicates
            if (candidates[i] > remain) break;  // No need to continue as array is sorted
            
            current.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i + 1, current, results);
            current.remove(current.size() - 1);
        }
    }
}