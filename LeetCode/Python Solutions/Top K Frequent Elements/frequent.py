# Solution
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict = {}
        for i in nums:
            if i not in Dict:
                Dict[i] = [1, i]
            else:
                Dict[i][0] += 1

        Srtd = sorted(Dict.values(), key=lambda x: x[0])[::-1]

        return [Srtd[k][1] for k in range(k)]



# Instantiation to check values
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.topKFrequent(nums = [1,1,1,2,2,3], k = 2)  # nums = [1,1,1,2,2,3], k = 2 -> [1,2]
    print(Solve)