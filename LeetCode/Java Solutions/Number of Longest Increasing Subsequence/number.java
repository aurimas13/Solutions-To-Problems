import java.util.Arrays;

public class Solution {
    public int findNumberOfLIS(int[] nums) {
        // get the length of the array
        int n = nums.length;
        
        // if the length is zero, return 0
        if (n == 0) {
            return 0;
        }
        
        // lengths[i] = longest ending in nums[i]
        int[] lengths = new int[n];  
        Arrays.fill(lengths, 0);

        // count[i] = number of longest ending in nums[i]
        int[] counts = new int[n];   
        Arrays.fill(counts, 1);
        
        // loop through each number in the array
        for (int i = 0; i < n; i++) {
            // for each number, check the numbers before it
            for (int j = 0; j < i; j++) {
                // if the current number is larger than the previous one
                if (nums[j] < nums[i]) {
                    // if the length of the longest increasing subsequence ending with nums[j] is larger or equal to that with nums[i]
                    if (lengths[j] >= lengths[i]) {
                        lengths[i] = 1 + lengths[j]; // set the length of the longest increasing subsequence ending with nums[i] to that of nums[j] plus 1
                        counts[i] = counts[j]; // set the count of the longest increasing subsequence ending with nums[i] to that of nums[j]
                    } else if (lengths[j] + 1 == lengths[i]) { // else if the length of the longest increasing subsequence ending with nums[j] plus 1 equals to that of nums[i]
                        counts[i] += counts[j]; // add the count of the longest increasing subsequence ending with nums[j] to that of nums[i]
                    }
                }
            }
        }

        // find the maximum length
        int longest = 0;
        for (int length : lengths) {
            longest = Math.max(longest, length);
        }

        // find the number of longest increasing subsequence
        int total = 0;
        for (int i = 0; i < n; i++) {
            if (lengths[i] == longest) {
                total += counts[i];
            }
        }
        return total;
    }

    // tests
    public static void main(String[] args) {
        Solution solution = new Solution();
        assert solution.findNumberOfLIS(new int[] {1,3,5,4,7}) == 2;
        assert solution.findNumberOfLIS(new int[] {2,2,2,2,2}) == 5;
        assert solution.findNumberOfLIS(new int[] {1,2,4,3,5,4,7,2}) == 3;
        System.out.println("All Passed!");
    }
}
