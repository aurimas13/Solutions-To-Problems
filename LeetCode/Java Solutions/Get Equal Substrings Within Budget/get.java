class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int maxLength = 0;
        int currentCost = 0;
        int left = 0;
        
        // Use a sliding window to find the maximum length of valid substring
        for (int right = 0; right < s.length(); right++) {
            currentCost += Math.abs(s.charAt(right) - t.charAt(right));
            
            // If current cost exceeds maxCost, move the left pointer
            while (currentCost > maxCost) {
                currentCost -= Math.abs(s.charAt(left) - t.charAt(left));
                left++;
            }
            
            // Update maxLength if we found a longer valid substring
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.equalSubstring("abcd", "bcdf", 3));  // Output: 3
        System.out.println(sol.equalSubstring("abcd", "cdef", 3));  // Output: 1
        System.out.println(sol.equalSubstring("abcd", "acde", 0));  // Output: 1
    }
}
