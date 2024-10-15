class Solution {
    public long minimumSteps(String s) {
        long steps = 0;
        int blackCount = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                blackCount++;
            } else {
                steps += blackCount;
            }
        }
        
        return steps;
    }
}
