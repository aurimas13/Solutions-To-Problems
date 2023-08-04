import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // Check if wordDict is empty
        if (wordDict.isEmpty()) {
            return false;
        }

        // Create list of intervals where words in wordDict are found in s
        List<int[]> intervals = new ArrayList<>();
        for (String word : wordDict) {
            int startIndex = 0;
            while (true) {
                int index = s.indexOf(word, startIndex);
                if (index == -1) {
                    break;
                }
                intervals.add(new int[] { index, index + word.length() - 1 });
                startIndex = index + 1;
            }
        }

        // Sort intervals by start index
        intervals.sort((a, b) -> Integer.compare(a[0], b[0]));

        // Use set to keep track of possible start indices of remaining words
        Set<Integer> possibleStarts = new HashSet<>();
        possibleStarts.add(0);
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            // Check if current interval starts at a possible start index
            if (possibleStarts.contains(start)) {
                // Check if current interval ends at the end of s
                if (end == s.length() - 1) {
                    return true;
                }
                // Add end index of current interval as a possible start index
                possibleStarts.add(end + 1);
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.wordBreak("leetcode", Arrays.asList("leet", "code"))); // Output: true
    }
}


