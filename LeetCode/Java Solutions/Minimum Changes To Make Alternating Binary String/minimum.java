import java.util.Arrays;


class Solution {
    public int minCost(int n, int[] cuts) {
        Arrays.sort(cuts); // Sorts the cuts array in ascending order
        int[] arr = new int[cuts.length + 2]; // Creates a new array 'arr' with length 'cuts.length + 2'
        arr[0] = 0; // Sets the first element of 'arr' to 0
        arr[arr.length - 1] = n; // Sets the last element of 'arr' to 'n'
        for (int i = 0; i < cuts.length; i++) {
            arr[i + 1] = cuts[i]; // Assigns each element of 'cuts' array to 'arr' starting from the second element
        }
        int[][] dp = new int[arr.length][arr.length]; // Creates a 2D array 'dp' with dimensions 'arr.length x arr.length'
        for (int i = 0; i < arr.length - 1; i++) {
            dp[i][i + 1] = 0; // Initializes diagonal elements of 'dp' to 0
        }
        for (int i = 2; i < arr.length; i++) {
            for (int j = 0; j < arr.length - i; j++) {
                int min = Integer.MAX_VALUE; // Initializes 'min' to the maximum possible integer value
                for (int k = j + 1; k < j + i; k++) {
                    min = Math.min(min, dp[j][k] + dp[k][j + i]); // Finds the minimum cost by evaluating different combinations
                }
                dp[j][j + i] = min + arr[j + i] - arr[j]; // Sets the minimum cost for the current subproblem
            }
        }
        return dp[0][arr.length - 1]; // Returns the minimum cost for the entire stick
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        int n1 = 7;
        int[] cuts1 = {1, 3, 4, 5};
        int result1 = solution.minCost(n1, cuts1);
        System.out.println("Minimum cost for test case 1: " + result1); // Expected output: 16

        // Test case 2
        int n2 = 9;
        int[] cuts2 = {5, 6, 1, 4, 2};
        int result2 = solution.minCost(n2, cuts2);
        System.out.println("Minimum cost for test case 2: " + result2); // Expected output: 22

        // Test case 3
        int n3 = 12;
        int[] cuts3 = {2, 3, 7, 9, 10};
        int result3 = solution.minCost(n3, cuts3);
        System.out.println("Minimum cost for test case 3: " + result3); // Expected output: 35
    }
}
