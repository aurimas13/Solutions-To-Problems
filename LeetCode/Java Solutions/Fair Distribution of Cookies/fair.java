public class Solution {

    private int minMaxCookies = Integer.MAX_VALUE;
    private int[] cookieCount;

    // Method to start the backtracking process
    public int distributeCookies(int[] cookies, int k) {
        // Initializing the cookieCount array with zeros
        this.cookieCount = new int[k];

        // Starting the backtracking process from the first cookie
        backtrack(0, cookies, k);

        // Return the minimum of the maximum number of cookies any child got
        return minMaxCookies;
    }

    // Backtrack method to try all possible distributions of cookies
    private void backtrack(int cookieNumber, int[] cookies, int k) {
        // If all cookies have been considered
        if (cookieNumber == cookies.length) {
            // Calculate the maximum number of cookies any child got in this distribution
            int maximum = 0;
            for (int count : cookieCount) {
                maximum = Math.max(maximum, count);
            }
            // Update the answer with the minimum value found so far
            minMaxCookies = Math.min(minMaxCookies, maximum);
            return;
        }

        // Try giving the current cookie to each child
        for (int i = 0; i < k; i++) {
            // Give the current cookie to the i-th child
            cookieCount[i] += cookies[cookieNumber];

            // Recursively try the next cookie
            backtrack(cookieNumber + 1, cookies, k);

            // Undo the choice for backtracking
            cookieCount[i] -= cookies[cookieNumber];

            // If the current child has not received any cookies, break
            // to avoid unnecessary permutations
            if (cookieCount[i] == 0) {
                break;
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] cookies = {8, 15, 10, 20, 8};
        int k = 2;
        System.out.println(solution.distributeCookies(cookies, k)); // Output will vary, it's trying to minimize the maximum number of cookies any child got
    }
}
