import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(String s, int start, List<String> path, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int end = start + 1; end <= s.length(); end++) {
            String substring = s.substring(start, end);
            if (isPalindrome(substring)) {
                path.add(substring);
                backtrack(s, end, path, result);
                path.remove(path.size() - 1);
            }
        }
    }
    
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.partition("aab"));  // Output: [["a","a","b"],["aa","b"]]
        System.out.println(sol.partition("a"));    // Output: [["a"]]
    }
}
