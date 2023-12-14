class Solution:
    def soupServings(self, initialSoupVolume: int) -> float:
        if initialSoupVolume > 4800:  # For larger initial volumes, the probability tends to 1.0
            return 1.0

        soupVolume = (initialSoupVolume + 24) // 25  # Convert the problem into a smaller scale
        dpTable = [[0.0 for _ in range(soupVolume+1)] for _ in range(soupVolume+1)]  # Initializing DP table with 0
        dpTable[0][0] = 0.5  # Probability when both soups are empty at the same time

        for soupBVolume in range(1, soupVolume+1):  # When soup B is not empty but soup A is empty
            dpTable[0][soupBVolume] = 1.0

        for soupAVolume in range(1, soupVolume+1):
            for soupBVolume in range(1, soupVolume+1):
                dpTable[soupAVolume][soupBVolume] = 0.25 * (dpTable[max(0, soupAVolume-4)][soupBVolume] + dpTable[max(0, soupAVolume-3)][max(0, soupBVolume-1)] + 
                                                           dpTable[max(0, soupAVolume-2)][max(0, soupBVolume-2)] + dpTable[max(0, soupAVolume-1)][max(0, soupBVolume-3)])

        return dpTable[soupVolume][soupVolume]
