import java.util.HashSet;
import java.util.Set;

public class Solution {
    public static boolean search(int[] nums, int target) {
        // Convert the nums array to a set.
        Set<Integer> setNum = new HashSet<>();
        for (int num : nums) {
            setNum.add(num);
        }

        // Return true if the target exists in the set, otherwise return false.
        return setNum.contains(target);
    }
}


