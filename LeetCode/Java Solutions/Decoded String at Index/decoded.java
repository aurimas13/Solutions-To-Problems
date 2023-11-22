public class Solution {

    public String decodeAtIndex(String s, int k) {
        long length = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                length *= (c - '0');
            } else {
                length++;
            }
        }

        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                length /= (c - '0');
                k %= length;
            } else {
                if (k == 0 || k == length) {
                    return String.valueOf(c); // Return String instead of char
                }
                length--;
            }
        }

        // This return is only for compilation purposes, the code should never reach here.
        return "-";
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String s1 = "leet2code3";
        int k1 = 10;
        
        String s2 = "ha22";
        int k2 = 5;
        
        String s3 = "a2345678999999999999999";
        int k3 = 1;

        System.out.println(solution.decodeAtIndex(s1, k1)); // Expected output: o
        System.out.println(solution.decodeAtIndex(s2, k2)); // Expected output: h
        System.out.println(solution.decodeAtIndex(s3, k3)); // Expected output: a
    }
}
