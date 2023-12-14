class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        // The number of tests we can perform.
        int tests = minutesToTest / minutesToDie;
        
        // The number of states we can test for (alive, dead in test 1, dead in test 2, etc.).
        int states = tests + 1;
        
        // Number of pigs needed is the number that satisfies states^pigs >= buckets.
        int pigs = 0;
        while (Math.pow(states, pigs) < buckets) {
            pigs++;
        }
        return pigs;
    }
}
