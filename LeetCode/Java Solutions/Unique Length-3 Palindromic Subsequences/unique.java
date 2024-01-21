import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int countPalindromicSubsequence(String s) {
        int count = 0;
        Set<Character> uniqueChars = new HashSet<>();

        // Add all unique characters to the set
        for (int i = 0; i < s.length(); i++) {
            uniqueChars.add(s.charAt(i));
        }

        // Iterate over each unique character
        for (char ch : uniqueChars) {
            int first = s.indexOf(ch);  // Find the first occurrence
            int last = s.lastIndexOf(ch);  // Find the last occurrence

            if (first != last) {  // Ensure there are characters in between
                Set<Character> middleChars = new HashSet<>();
                // Count unique characters in between
                for (int i = first + 1; i < last; i++) {
                    middleChars.add(s.charAt(i));
                }
                count += middleChars.size();
            }
        }

        return count;
    }
}
