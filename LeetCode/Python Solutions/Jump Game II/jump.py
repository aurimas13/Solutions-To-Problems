from typing import List


class Solution:
    @staticmethod
    def jump(nums: List[int]) -> int:
        n = len(nums)
        c = {n - 1: 0}
        i = n - 2
        while 0 <= i < n:
            if nums[i] == 0:
                c[i] = float('inf')
                i -= 1
                continue
            jump = i + nums[i]
            if jump >= n:
                jump = n - 1
            c[i] = c[jump] + 1
            for j in range(i + 1, jump):
                if j > n - 2:
                    break
                if c[i] < c[j]:
                    c[j] = c[i]
                else:
                    break
            i -= 1
        return c[0]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.jump([2, 3, 1, 1, 4])
    # nums = [2,3,1,1,4] -> 2
    # nums = [2,3,0,1,4] -> 2
    print(Solve)
