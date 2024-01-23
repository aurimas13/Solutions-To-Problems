import java.util.List;

class Solution {
    public int maxLength(List<String> arr) {
        // List to store unique bitmasks (only strings with unique characters)
        List<Integer> uniqueBitmasks = new ArrayList<>();
        
        for (String s : arr) {
            int bitmask = 0;
            for (char ch : s.toCharArray()) {
                int bit = 1 << (ch - 'a');
                // If bit is already set, skip this string
                if ((bitmask & bit) != 0) {
                    bitmask = 0;
                    break;
                }
                bitmask |= bit;
            }
            if (bitmask != 0) {
                uniqueBitmasks.add(bitmask);
            }
        }

        return backtrack(uniqueBitmasks, 0, 0);
    }

    private int backtrack(List<Integer> uniqueBitmasks, int index, int currentBitmask) {
        if (index == uniqueBitmasks.size()) {
            return Integer.bitCount(currentBitmask);
        }

        int maxLength = backtrack(uniqueBitmasks, index + 1, currentBitmask);
        int nextBitmask = uniqueBitmasks.get(index);

        // Only combine if there's no overlap
        if ((currentBitmask & nextBitmask) == 0) {
            maxLength = Math.max(maxLength, backtrack(uniqueBitmasks, index + 1, currentBitmask | nextBitmask));
        }

        return maxLength;
    }
}
