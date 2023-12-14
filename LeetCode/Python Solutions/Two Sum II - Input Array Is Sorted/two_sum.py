# Solution
from typing import List


class Solution:
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        dic, m, i = {},  len(numbers), 0
        while i<m:
            t = target - numbers[i]
            if numbers[i] in dic: return [dic[numbers[i]]+1, i+1]
            else: dic[t] = i
            i+=1
        return -1


# Checking in Console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.twoSum(numbers = [2, 3, 4], target = 6 )
    # numbers = [2, 3, 4], target = 6 -> [1, 3]
    # numbers = [2,7,11,15], target = 9 -> [1,2]
    # numbers = [-1,0], target = -1 -> [1,2]
    print(Solve)
