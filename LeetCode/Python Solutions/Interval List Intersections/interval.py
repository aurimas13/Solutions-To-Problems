from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        combined = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            low_ints = max(firstList[i][0], secondList[j][0])
            high_ints = min(firstList[i][1], secondList[j][1])
            if low_ints <= high_ints:
                combined.append([low_ints, high_ints])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return combined


# Checking in console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])  # Output -> [[1, 2], [5, 5], [8, 10], 15, 23], [24, 24], [25, 25]]
    print(Solve)
