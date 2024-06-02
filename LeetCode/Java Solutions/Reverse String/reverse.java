class Solution {
    public void reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        char[] s1 = {'h', 'e', 'l', 'l', 'o'};
        sol.reverseString(s1);
        System.out.println(s1);  // Output: ["o","l","l","e","h"]

        char[] s2 = {'H', 'a', 'n', 'n', 'a', 'h'};
        sol.reverseString(s2);
        System.out.println(s2);  // Output: ["h","a","n","n","a","H"]
    }
}
