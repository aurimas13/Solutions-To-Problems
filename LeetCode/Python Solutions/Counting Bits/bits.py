from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Creating an empty list:
        ones_list = []
        # Looping over digits that make n:
        for i in range(n+1):
            cnt = list(map(str, bin(i))).count('1')
            ones_list.append(cnt)
        return ones_list

# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countBits(2)  # for 2 - [0,1,1] | for 5 - [0,1,1,2,1,2]
    print(Solve)
