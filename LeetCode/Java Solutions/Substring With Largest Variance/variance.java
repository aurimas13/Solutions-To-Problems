import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

class Solution {
    public int largestVariance(String s) {
        int maxDiff = 0;
        HashMap<Character, Integer> charCounter = new HashMap<>();

        for(char c: s.toCharArray()) {
            charCounter.put(c, charCounter.getOrDefault(c, 0) + 1);
        }

        for(char char1: new HashSet<>(charCounter.keySet())) {
            if(charCounter.get(char1) == 1) {
                continue;
            }
            for(char char2: charCounter.keySet()) {
                if(char1 == char2) {
                    continue;
                }
                int substrCount = 0, diff = -s.length();
                for(char c: s.toCharArray()) {
                    if(c == char1) {
                        substrCount += 1;
                        diff += 1;
                    }
                    else if(c == char2) {
                        substrCount -= 1;
                        diff = substrCount;
                        if(substrCount < 0) {
                            substrCount = 0;
                        }
                    }
                    if(maxDiff < diff) {
                        maxDiff = diff;
                    }
                }
            }
        }
        return maxDiff;
    }
}
