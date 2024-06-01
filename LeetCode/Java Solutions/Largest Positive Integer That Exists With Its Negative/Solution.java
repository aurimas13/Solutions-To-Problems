import java.util.*;

public class Solution {
    public int findMaxK(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        int maxK = -1;
        for (int num : nums) {
            if (num > 0 && numSet.contains(-num)) {
                maxK = Math.max(maxK, num);
            }
        }
        
        return maxK;
    }
}
