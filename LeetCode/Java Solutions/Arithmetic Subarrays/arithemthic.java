import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> res = new ArrayList<>();

        for (int i = 0; i < l.length; i++) {
            // Extract the subarray between the left and right indices
            int[] subarray = Arrays.copyOfRange(nums, l[i], r[i] + 1);

            // Sort the subarray in ascending order
            Arrays.sort(subarray);

            // Calculate the common difference between consecutive elements
            int commonDiff = subarray[1] - subarray[0];
            boolean isArithmetic = true;

            for (int j = 2; j < subarray.length; j++) {
                if (subarray[j] - subarray[j - 1] != commonDiff) {
                    isArithmetic = false;
                    break;
                }
            }

            // Append the result to the list of results
            res.add(isArithmetic);
        }

        return res;
    }
}
