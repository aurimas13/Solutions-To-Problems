import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.Arrays;

public class Solution {
    public int minExtraChar(String s, String[] dictionaryArray) {
        // Convert the String array to a List
        List<String> dictionary = Arrays.asList(dictionaryArray);
        
        // Initialize the maximum possible value for dp
        int maxVal = s.length() + 1;
        
        // Create a dp array initialized with maxVal
        int[] dp = new int[s.length() + 1];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = maxVal;
        }
        
        // Base case: 0 characters from s have 0 extra characters
        dp[0] = 0;
        
        // Convert the dictionary list to a set for O(1) lookups
        Set<String> dictionarySet = new HashSet<>(dictionary);

        // Iterate through the string s
        for (int i = 1; i <= s.length(); i++) {
            // By default, assume we add an extra character for position i
            dp[i] = dp[i - 1] + 1;

            // Check all possible lengths of words ending at position i
            for (int l = 1; l <= i; l++) {
                // If the substring is in the dictionary
                if (dictionarySet.contains(s.substring(i - l, i))) {
                    // Update the dp value for position i
                    dp[i] = Math.min(dp[i], dp[i - l]);
                }
            }
        }
        
        // Return the dp value for the entire string
        return dp[s.length()];
    }
}
