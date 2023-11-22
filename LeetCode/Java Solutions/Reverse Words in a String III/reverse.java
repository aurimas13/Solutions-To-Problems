public class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        
        for (int i = 0; i < words.length; i++) {
            words[i] = new StringBuilder(words[i]).reverse().toString();
        }
        
        return String.join(" ", words);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String s1 = "Let's take LeetCode contest";
        String s2 = "God Ding";
        
        System.out.println(solution.reverseWords(s1)); // Expected output: "s'teL ekat edoCteeL tsetnoc"
        System.out.println(solution.reverseWords(s2)); // Expected output: "doG gniD"
    }
}
