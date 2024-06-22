class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int totalSatisfied = 0;
        int additionalSatisfied = 0;
        int maxAdditionalSatisfied = 0;

        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 0) {
                totalSatisfied += customers[i];
            } else {
                additionalSatisfied += customers[i];
            }

            if (i >= minutes) {
                if (grumpy[i - minutes] == 1) {
                    additionalSatisfied -= customers[i - minutes];
                }
            }

            maxAdditionalSatisfied = Math.max(maxAdditionalSatisfied, additionalSatisfied);
        }

        return totalSatisfied + maxAdditionalSatisfied;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxSatisfied(new int[]{1,0,1,2,1,1,7,5}, new int[]{0,1,0,1,0,1,0,1}, 3));  // Output: 16
        System.out.println(sol.maxSatisfied(new int[]{1}, new int[]{0}, 1));  // Output: 1
    }
}
