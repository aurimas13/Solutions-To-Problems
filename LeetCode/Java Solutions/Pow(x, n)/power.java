class Solution {
    public double myPow(double x, int n) {
        long N = n;
        // if n is negative, change the problem to x^-n to 1/x^n
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        // Initialize answer to 1.0 as any number raised to the power of 0 is 1
        double ans = 1.0;
        
        // current_product represents the current base that is used to compute the power
        double current_product = x;

        // We will now start reducing the power N towards 0
        for (long i = N; i > 0; i /= 2) {
            // If the current power is odd, we multiply the answer with the current base
            if ((i % 2) == 1) {
                ans *= current_product;
            }
            // Now we square the current base for the next iteration
            current_product *= current_product;
        }
        return ans;
    }
}
