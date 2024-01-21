import java.util.ArrayList;
import java.util.List;


class Solution {
    /**
     * Given an array of integers sorted in ascending order, returns a list of its
     * summary ranges. A summary range is a contiguous sequence of numbers where
     * the difference between consecutive elements is 1.
     *
     * @param  nums  an array of integers sorted in ascending order
     * @return       a list of summary ranges
     */
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        
        if (nums == null || nums.length == 0) {
            return result;
        }
        
        int start = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1] + 1) {
                if (start == nums[i - 1]) {
                    result.add(Integer.toString(start));
                } else {
                    result.add(start + "->" + nums[i - 1]);
                }
                start = nums[i];
            }
        }
        
        // Handle the last range
        if (start == nums[nums.length - 1]) {
            result.add(Integer.toString(start));
        } else {
            result.add(start + "->" + nums[nums.length - 1]);
        }
        
        return result;
    }

    /**
     * The main function that creates a Solution object, initializes an array of
     * integers, and prints out the summary ranges of the array. 
     *
     * @param  args  the command line arguments
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {0, 1, 2, 4, 5, 7};
        List<String> result = solution.summaryRanges(nums);
        for (String range : result) {
            System.out.println(range);
        }
    }
}

