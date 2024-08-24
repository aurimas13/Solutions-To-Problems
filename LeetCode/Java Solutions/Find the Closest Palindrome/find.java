class Solution {
    public String nearestPalindromic(String n) {
        if (n.length() == 1) {
            return String.valueOf(Integer.parseInt(n) - 1);
        }
        
        long num = Long.parseLong(n);
        int l = n.length();
        List<Long> candidates = new ArrayList<>();
        candidates.add((long)Math.pow(10, l-1) - 1);  // Edge case: 9...9
        candidates.add((long)Math.pow(10, l) + 1);    // Edge case: 10...01
        
        long prefix = Long.parseLong(n.substring(0, (l+1)/2));
        for (long i = prefix-1; i <= prefix+1; i++) {
            long candidate;
            if (l % 2 == 0) {
                candidate = generatePalindrome(i, false);
            } else {
                candidate = generatePalindrome(i, true);
            }
            candidates.add(candidate);
        }
        
        long closest = candidates.get(0);
        for (long candidate : candidates) {
            if (candidate != num) {
                if (Math.abs(candidate - num) < Math.abs(closest - num) ||
                    (Math.abs(candidate - num) == Math.abs(closest - num) && candidate < closest)) {
                    closest = candidate;
                }
            }
        }
        
        return String.valueOf(closest);
    }
    
    private long generatePalindrome(long prefix, boolean odd) {
        long result = prefix;
        if (odd) {
            prefix /= 10;
        }
        while (prefix > 0) {
            result = result * 10 + prefix % 10;
            prefix /= 10;
        }
        return result;
    }
}