from typing import List
class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        answer = []

        for i in range(2**len(nums)):
            subset = [nums[j] for j in range(len(nums)) if (1 << j) & i]
            answer.append(subset)

        return answer


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.subsets(nums = [1,2,3]) # nums = [1,2,3] ->
    # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] | nums = [0] -> [[],[0]]
    print(Solve)
