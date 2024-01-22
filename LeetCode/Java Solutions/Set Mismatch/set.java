class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;  // Length of the input array
        boolean[] seen = new boolean[n + 1];  // Boolean array to keep track of seen numbers
        int duplicated = -1;  // Variable to store the duplicated number

        // Iterate over the array to find the duplicated number
        for (int num : nums) {
            if (seen[num]) {
                duplicated = num;  // Found the duplicated number
            } else {
                seen[num] = true;  // Mark the number as seen
            }
        }

        // Iterate from 1 to n to find the missing number
        for (int i = 1; i <= n; i++) {
            if (!seen[i]) {
                return new int[] {duplicated, i};  // Return the duplicated and missing number
            }
        }
        return new int[] {-1, -1};  // Placeholder return statement
    }
}
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;  // Length of the input array
        boolean[] seen = new boolean[n + 1];  // Boolean array to keep track of seen numbers
        int duplicated = -1;  // Variable to store the duplicated number

        // Iterate over the array to find the duplicated number
        for (int num : nums) {
            if (seen[num]) {
                duplicated = num;  // Found the duplicated number
            } else {
                seen[num] = true;  // Mark the number as seen
            }
        }

        // Iterate from 1 to n to find the missing number
        for (int i = 1; i <= n; i++) {
            if (!seen[i]) {
                return new int[] {duplicated, i};  // Return the duplicated and missing number
            }
        }
        return new int[] {-1, -1};  // Placeholder return statement
    }
}
