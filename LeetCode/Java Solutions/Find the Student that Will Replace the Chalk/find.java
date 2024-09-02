class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        long sum = 0;
        for (int c : chalk) {
            sum += c;
        }
        
        k %= sum;  // Reduce k to be within one full cycle
        
        for (int i = 0; i < chalk.length; i++) {
            if (k < chalk[i]) {
                return i;
            }
            k -= chalk[i];
        }
        
        return 0;  // This line should never be reached
    }
}