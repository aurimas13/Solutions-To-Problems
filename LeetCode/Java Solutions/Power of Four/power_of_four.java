public class Solution {
    public boolean isPowerOfFour(int n) {
        if (n <= 0) {
            return false;
        }

        // Calculate the logarithm base 4 of n
        double logN = Math.log(n) / Math.log(4);

        // Check if logN is an integer. We do this by comparing logN with its nearest integer value.
        // The Math.rint function returns the double value that is closest in value to the argument and is equal to a mathematical integer.
        return Math.abs(logN - Math.rint(logN)) <= 1e-10; // where 1e-10 is a very small tolerance value
    }
}
