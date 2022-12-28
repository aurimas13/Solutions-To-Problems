from typing import List


class Solution:
    @staticmethod
    def checkIfExist(arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if float(num) / 2 in s or num * 2 in s:
                return True
            s.add(num)
        return False


# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.checkIfExist(arr = [10,2,5,3])
    # arr = [10,2,5,3] -> true
    # arr = [3, 1, 7, 11] -> false
    print(Solve)
