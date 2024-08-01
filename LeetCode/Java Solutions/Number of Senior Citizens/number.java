class Solution {
    public int countSeniors(String[] details) {
        int count = 0;
        for (String detail : details) {
            int age = Integer.parseInt(detail.substring(11, 13));
            if (age > 60) {
                count++;
            }
        }
        return count;
    }
}

// Example usage:
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] details1 = {"7868190130M7522", "5303914400F9211", "9273338290F4010"};
        String[] details2 = {"1313579440F2036", "2921522980M5644"};
        System.out.println(sol.countSeniors(details1));  // Output: 2
        System.out.println(sol.countSeniors(details2));  // Output: 0
    }
}
