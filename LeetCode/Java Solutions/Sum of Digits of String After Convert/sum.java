class Solution {
    public int getLucky(String s, int k) {
        // Step 1: Convert the string into the numeric form
        StringBuilder numStr = new StringBuilder();
        for (char c : s.toCharArray()) {
            numStr.append(c - 'a' + 1);
        }
        
        // Step 2: Perform the digit sum transformation k times
        String result = numStr.toString();
        for (int i = 0; i < k; i++) {
            int sum = 0;
            for (char digit : result.toCharArray()) {
                sum += digit - '0';
            }
            result = String.valueOf(sum);
        }
        
        // Convert the final result back to integer
        return Integer.parseInt(result);
    }
}
