class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # The number of tests we can perform.
        tests = minutesToTest // minutesToDie
        
        # The number of states we can test for (alive, dead in test 1, dead in test 2, etc.).
        states = tests + 1
        
        # Number of pigs needed is the number that satisfies states^pigs >= buckets.
        pigs = 0
        while (states ** pigs < buckets):
            pigs += 1
        return pigs
