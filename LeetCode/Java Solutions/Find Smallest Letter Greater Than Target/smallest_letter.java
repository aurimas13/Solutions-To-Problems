import java.util.*;

public class Solution {

    public char nextGreatestLetter(char[] letters, char target) {
        if (target < letters[0] || target >= letters[letters.length - 1]) {
            return letters[0];
        }

        int n = letters.length;
        int lo = 0, hi = n - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            // what we want is on the right side, not in [0...mid]
            if (letters[mid] <= target) {
                lo = mid + 1;
            }
            // mid might or might not be the smallest but it's the right way. Let reduce the searching space to [0...mid]
            else {
                hi = mid;
            }
        }

        return letters[hi];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        char result = sol.nextGreatestLetter(new char[] {'c', 'f', 'j'}, 'a');
        // letters = ['c','f','j'], target = 'a' -> 'c' 
        // letters = ['c','f','j'], target = 'd' -> 'f'
        System.out.println(result);
    }
}

