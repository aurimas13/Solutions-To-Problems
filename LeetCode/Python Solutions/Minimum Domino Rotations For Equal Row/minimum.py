from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        validNumbers = (tops[0], bottoms[0])
        for x in validNumbers:
            countTops = 0
            countBottoms = 0
            for i in range(n):
                countTops += (x == tops[i])
                countBottoms += (x == bottoms[i])
                if x != bottoms[i] and x != tops[i]:
                    break
            if i == n-1:
                return n - max(countTops,countBottoms)
        return -1

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2])  # tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2] -> 2 | tops = [3,5,1,2,3], bottoms = [3,6,3,3,4] -> -1
    print(Solve)
