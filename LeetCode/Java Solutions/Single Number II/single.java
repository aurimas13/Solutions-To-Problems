class Solution {
    /**
     * Finds the single number in the given array of integers.
     *
     * @param  nums  an array of integers
     * @return       the single number in the array
     */
    public int singleNumber(int[] nums) {
        int once = 0, twice = 0;
        for (int num : nums) {
            once = (once ^ num) & ~twice;
            twice = (twice ^ num) & ~once;
        }
        return once;
    }
}

