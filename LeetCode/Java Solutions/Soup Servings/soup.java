class Solution {
    public double soupServings(int initialSoupVolume) {
        if (initialSoupVolume > 4800) {  // For larger initial volumes, the probability tends to 1.0
            return 1.0;
        }

        int soupVolume = (initialSoupVolume + 24) / 25;  // Convert the problem into a smaller scale
        double[][] dpTable = new double[soupVolume+1][soupVolume+1];  // Initializing DP table with 0
        dpTable[0][0] = 0.5;  // Probability when both soups are empty at the same time

        for (int soupBVolume = 1; soupBVolume <= soupVolume; soupBVolume++) {  // When soup B is not empty but soup A is empty
            dpTable[0][soupBVolume] = 1.0;
        }

        for (int soupAVolume = 1; soupAVolume <= soupVolume; soupAVolume++) {
            for (int soupBVolume = 1; soupBVolume <= soupVolume; soupBVolume++) {
                dpTable[soupAVolume][soupBVolume] = 0.25 * (dpTable[Math.max(0, soupAVolume-4)][soupBVolume] + dpTable[Math.max(0, soupAVolume-3)][Math.max(0, soupBVolume-1)] + 
                                                           dpTable[Math.max(0, soupAVolume-2)][Math.max(0, soupBVolume-2)] + dpTable[Math.max(0, soupAVolume-1)][Math.max(0, soupBVolume-3)]);
            }
        }

        return dpTable[soupVolume][soupVolume];
    }
}

