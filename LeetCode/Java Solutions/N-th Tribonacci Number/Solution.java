public class Solution {
    public int tribonacci(int n) {
        if (n == 0) return 0;
        if (n < 3) return 1;
        
        // Initialize base cases
        int a = 0, b = 1, c = 1;
        
        // Compute tribonacci starting from T_3
        for (int i = 3; i <= n; i++) {
            // Compute the next number in the sequence
            int next = a + b + c;
            // Slide the window
            a = b;
            b = c;
            c = next;
        }
        
        return c;
    }
}
