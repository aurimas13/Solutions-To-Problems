import java.util.*;

class Solution {
    public String largestNumber(int[] nums) {
        // Convert int array to String array
        String[] strNums = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strNums[i] = String.valueOf(nums[i]);
        }
        
        // Sort the array
        Arrays.sort(strNums, (a, b) -> (b + a).compareTo(a + b));
        
        // If the largest number is 0, the entire number is 0
        if (strNums[0].equals("0")) {
            return "0";
        }
        
        // Build the largest number
        StringBuilder largestNum = new StringBuilder();
        for (String num : strNums) {
            largestNum.append(num);
        }
        
        return largestNum.toString();
    }
}