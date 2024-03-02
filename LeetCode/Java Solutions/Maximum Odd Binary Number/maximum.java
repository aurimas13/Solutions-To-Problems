class Solution {
    public String maximumOddBinaryNumber(String s) {
        // Count the number of 1s and 0s
        int ones = 0, zeros = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') ones++;
            else zeros++;
        }
        
        // Ensure at least one '1' is at the end to make it odd, adjust counts
        ones--;
        
        // The maximum odd binary number: all remaining '1's, followed by all '0's, ending with a '1'
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ones; i++) sb.append('1');
        for (int i = 0; i < zeros; i++) sb.append('0');
        sb.append('1');
        
        return sb.toString();
    }
}
