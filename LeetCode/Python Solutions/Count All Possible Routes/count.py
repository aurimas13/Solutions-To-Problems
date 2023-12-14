from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """
        This function takes a list of locations, start, finish and fuel as input and returns the number of possible routes from start to finish.
        The function accepts four parameters:
            1. locations (List[int]): A list of integers representing the locations.
            2. start (int): An integer representing the starting location.
            3. finish (int): An integer representing the finishing location.
            4. fuel (int): An integer representing the initial amount of fuel.
        The function returns an integer representing the number of possible routes from start to finish.
        """
        mod = 10**9 + 7
        n = len(locations)
        dp = [[0]*n for _ in range(fuel+1)]
        for f in range(fuel+1):
            dp[f][finish] = 1
        
        for f in range(fuel, -1, -1):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    d = abs(locations[j] - locations[k])
                    if f + d <= fuel:
                        dp[f][j] = (dp[f][j] + dp[f + d][k]) % mod
        return dp[0][start]

