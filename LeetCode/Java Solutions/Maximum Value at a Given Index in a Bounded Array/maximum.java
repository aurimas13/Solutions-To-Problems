class Solution {
    /**
     * Finds the maximum value of an integer array by performing binary search.
     *
     * @param  n         the length of the array
     * @param  index     the index of the starting element
     * @param  maxSum    the maximum sum of the array
     * @return           the maximum value of the array
     */
    public int maxValue(int n, int index, int maxSum) {
        maxSum -= n;
        int left = 0, right = maxSum, mid;
        while (left < right) {
            mid = (left + right + 1) / 2;
            if (test(n, index, mid) <= maxSum)
                left = mid;
            else
                right = mid - 1;
        }
        return left + 1;
    }

    /**
     * Calculates and returns a long value based on the given parameters. 
     *
     * @param  n     an int representing a number
     * @param  index an int representing an index
     * @param  a     an int representing a value
     * @return       a long value calculated based on the given parameters
     */
    private long test(int n, int index, int a) {
        int b = Math.max(a - index, 0);
        long res = (long)(a + b) * (a - b + 1) / 2;
        b = Math.max(a - ((n - 1) - index), 0);
        res += (long)(a + b) * (a - b + 1) / 2;
        return res - a;
    }
}
