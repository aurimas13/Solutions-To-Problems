public class Solution {
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder uniqueStr = new StringBuilder();

        // Iterate through each string in nums
        for (int i = 0; i < nums.length; i++) {
            // Flip the ith bit of the ith string
            uniqueStr.append(nums[i].charAt(i) == '0' ? '1' : '0');
        }

        return uniqueStr.toString();
    }
}
