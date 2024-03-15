class Solution {
    public int minimumLength(String s) {
        int left = 0, right = s.length() - 1;
        
        while (left < right && s.charAt(left) == s.charAt(right)) {
            char ch = s.charAt(left);
            // Move left pointer to the right past all characters equal to ch
            while (left <= right && s.charAt(left) == ch) {
                left++;
            }
            // Move right pointer to the left past all characters equal to ch
            while (right >= left && s.charAt(right) == ch) {
                right--;
            }
        }
        
        // Return the length of the remaining string
        return right - left + 1;
    }
}
