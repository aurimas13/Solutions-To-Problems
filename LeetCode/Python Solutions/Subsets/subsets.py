from typing import List


class Solution:
    def subsets(nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
    

# Tests
if __name__ == "__main__":
    s = Solution()
    assert s.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    assert s.subsets([0]) == [[],[0]]
    print("All tests passed!")