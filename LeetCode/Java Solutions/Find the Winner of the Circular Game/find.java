class Solution {
    public int findTheWinner(int n, int k) {
        // Solving Josephus problem
        int winner = 0;  // The position of the winner in 0-based index
        for (int i = 1; i <= n; i++) {
            winner = (winner + k) % i;
        }
        return winner + 1;  // Convert to 1-based index
    }
}
