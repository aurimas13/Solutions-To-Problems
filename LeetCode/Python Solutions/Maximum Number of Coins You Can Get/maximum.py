import java.util.Arrays;

public class Solution {
    public int maxCoins(int[] piles) {
        // Sort the array in descending order
        Arrays.sort(piles);
        
        int totalCoins = 0;
        int n = piles.length;
        
        // Start from the second element and iterate until two-thirds of the array
        for (int i = n / 3; i < n; i += 2) {
            totalCoins += piles[i];
        }
        
        return totalCoins;
    }
}
