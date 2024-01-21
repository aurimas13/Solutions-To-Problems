public class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder result = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber -= 1;
            char ch = (char)(columnNumber % 26 + 'A');
            result.insert(0, ch);
            columnNumber /= 26;
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.convertToTitle(28));  // Outputs AB
    }
}
