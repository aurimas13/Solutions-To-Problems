class Solution {
    public int findTheLongestSubstring(String s) {
        int[] first = new int[32];
        Arrays.fill(first, -1);
        first[0] = 0;
        
        int state = 0, maxLen = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case 'a': state ^= 1; break;
                case 'e': state ^= 2; break;
                case 'i': state ^= 4; break;
                case 'o': state ^= 8; break;
                case 'u': state ^= 16; break;
            }
            if (first[state] >= 0) {
                maxLen = Math.max(maxLen, i + 1 - first[state]);
            } else {
                first[state] = i + 1;
            }
        }
        return maxLen;
    }
}