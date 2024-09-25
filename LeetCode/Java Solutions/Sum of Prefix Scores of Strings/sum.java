class Solution {
    public boolean judgeSquareSum(int c) {
        if (c < 0) {
            return false;
        }

        long a = 0;
        long b = (long) Math.sqrt(c);

        while (a <= b) {
            long currentSum = a * a + b * b;
            if (currentSum == c) {
                return true;
            } else if (currentSum < c) {
                a++;
            } else {
                b--;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.judgeSquareSum(5));  // Output: true
        System.out.println(solution.judgeSquareSum(3));  // Output: false
        System.out.println(solution.judgeSquareSum(2147483600));  // Output: true
    }
}
