from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                left = stack.pop()
                ans[left] = i - left
            stack.append(i)
        return ans


# Tests:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
    # temperatures = [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
    # temperatures = [30,40,50,60] -> [1,1,1,0]
    print(Solve)


